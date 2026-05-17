from django.shortcuts import render

MODULE_TITLE = 'SDN'

def index(request):
    return render(request, 'sdn/index.html', {'title': MODULE_TITLE})
