from django.shortcuts import render

MODULE_TITLE = 'IoT Integration'

def index(request):
    return render(request, 'iot_integration/index.html', {'title': MODULE_TITLE})
