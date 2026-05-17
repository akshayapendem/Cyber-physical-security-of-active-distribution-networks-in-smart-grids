from django.shortcuts import render

MODULE_TITLE = 'Monitoring and Reporting'

def index(request):
    return render(request, 'monitoring/index.html', {'title': MODULE_TITLE})
