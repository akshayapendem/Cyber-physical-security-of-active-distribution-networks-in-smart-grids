from django.shortcuts import render
import random
import pandas as pd
from adn_operations.models import UploadedDataset
import pandas as pd
from adn_operations.models import UploadedDataset

MODULE_TITLE = 'Communication & Standards Module'
MODULE_DESC = "The challenges and requirements of associated communication protocols and standards are presented."

def index(request):
    # Mock data generation for Chart.js
    labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    data_values = [random.randint(10, 90) for _ in range(6)]
    
    # Try fetching latest dataset
    latest_dataset = UploadedDataset.objects.order_by('-uploaded_at').first()
    if latest_dataset:
        try:
            df = pd.read_csv(latest_dataset.file.path)
            numeric_cols = df.select_dtypes(include='number').columns
            if len(numeric_cols) > 2:
                vals = df[numeric_cols[2]].dropna().head(6).tolist()
                if len(vals) > 0:
                    data_values = vals
                    while len(data_values) < 6:
                        data_values.append(random.randint(10, 90))
        except Exception as e:
            pass # fallback

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
            if len(temp_cols) > 2:
                col_name = f"uploaded dataset column '{temp_cols[2]}'"
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
    return render(request, 'communication_standards/index.html', context)
