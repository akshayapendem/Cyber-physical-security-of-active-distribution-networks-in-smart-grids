from django.shortcuts import render

MODULE_TITLE = 'Threat Simulation'

def index(request):
    return render(request, 'threat_simulation/index.html', {'title': MODULE_TITLE})
