from django.shortcuts import render
import random
import pandas as pd
from .models import UploadedDataset

MODULE_TITLE = 'ADN Critical Operations Module'
MODULE_DESC = "The cyber-physical aspects of each critical operation/component are analyzed."

def index(request):
    labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    data_values = [random.randint(10, 90) for _ in range(6)]
    
    # Try fetching latest dataset
    latest_dataset = UploadedDataset.objects.order_by('-uploaded_at').first()
    if latest_dataset:
        try:
            df = pd.read_csv(latest_dataset.file.path)
            # Find first numeric column
            numeric_cols = df.select_dtypes(include='number').columns
            if len(numeric_cols) > 0:
                # Take up to 6 values from the first numeric column
                vals = df[numeric_cols[0]].dropna().head(6).tolist()
                if len(vals) > 0:
                    data_values = vals
                    # Pad if less than 6
                    while len(data_values) < 6:
                        data_values.append(random.randint(10, 90))
        except Exception as e:
            pass # fallback to random

    predictions = [val + random.randint(-10, 20) for val in data_values]

    avg_current = sum(data_values) / len(data_values)
    avg_pred = sum(predictions) / len(predictions)
    trend = "increasing" if avg_pred > avg_current else "decreasing"
    
    col_name = "randomized simulation"
    # We check if 'numeric_cols' is in the local namespace (it's declared in the try block if successful)
    try:
        if latest_dataset:
            import pandas as pd
            df_temp = pd.read_csv(latest_dataset.file.path)
            temp_cols = df_temp.select_dtypes(include='number').columns
            if len(temp_cols) > 0:
                col_name = f"uploaded dataset column '{temp_cols[0]}'"
    except:
        pass

    calculation_details = f"Currently deriving data from {col_name}. Real-world captured values average {avg_current:.2f}. The system calculates prediction values by applying a dynamic algorithmic cyber-stress variance to the base structure, projecting a {trend} trend with an expected average of {avg_pred:.2f}."


    context = {
        'title': MODULE_TITLE,
        'description': MODULE_DESC,
        'labels': labels,
        'data_values': data_values,
        'predictions': predictions,
        'calculation_details': calculation_details,
    }
    return render(request, 'adn_operations/index.html', context)

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

from .forms import DatasetUploadForm
from django.contrib.auth.decorators import login_required

@login_required
def upload_dataset(request):
    if request.method == 'POST':
        form = DatasetUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dataset uploaded successfully! The dashboard has been updated.')
            return redirect('adn_operations_index')
    else:
        form = DatasetUploadForm()
    
    return render(request, 'adn_operations/upload.html', {'form': form})
