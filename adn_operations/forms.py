from django import forms
from .models import UploadedDataset

class DatasetUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedDataset
        fields = ['file']
        widgets = {
            'file': forms.FileInput(attrs={'class': 'form-control', 'accept': '.csv'})
        }
