from django.shortcuts import render

MODULE_TITLE = 'Blockchain Security'

def index(request):
    return render(request, 'blockchain/index.html', {'title': MODULE_TITLE})
