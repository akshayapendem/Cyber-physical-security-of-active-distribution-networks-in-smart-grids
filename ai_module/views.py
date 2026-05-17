from django.shortcuts import render

MODULE_TITLE = 'Artificial Intelligence'

def index(request):
    return render(request, 'ai_module/index.html', {'title': MODULE_TITLE})
