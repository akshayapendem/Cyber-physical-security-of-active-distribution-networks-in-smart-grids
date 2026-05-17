from django.shortcuts import render

MODULE_TITLE = 'Cybersecurity Analysis'

def index(request):
    return render(request, 'cybersecurity/index.html', {'title': MODULE_TITLE})
