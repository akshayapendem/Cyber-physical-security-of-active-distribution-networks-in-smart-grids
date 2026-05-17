import os
import shutil

root = os.path.dirname(os.path.abspath(__file__))

old_apps = [
    'infrastructure', 'iot_integration', 'cybersecurity', 
    'ai_module', 'blockchain', 'sdn', 'threat_simulation', 'monitoring'
]

# 1. Delete old apps
for app in old_apps:
    app_path = os.path.join(root, app)
    if os.path.exists(app_path):
        shutil.rmtree(app_path)
    tpl_path = os.path.join(root, 'templates', app)
    if os.path.exists(tpl_path):
        shutil.rmtree(tpl_path)

new_apps = [
    ('adn_operations', 'ADN Critical Operations Module', 
     'Varying load profiles and prediction of grid stability under cyber-physical stress.'),
    ('device_security', 'Device Security Module', 
     'Known vulnerabilities (CVEs) on smart meters and compromise probability prediction.'),
    ('communication_standards', 'Communication & Standards Module',
     'Packet loss, protocol spoofing attack rates, and network intrusion likelihood.'),
    ('application_drivers', 'Application Drivers & Enablers Module',
     'EV charging point vulnerabilities and prediction of cascading failure.'),
    ('industry_solutions', 'Industry Solutions Module',
     'Enterprise firewalls, IDS/IPS efficiency, and mitigation success predictions against zero-days.'),
    ('research_outcomes', 'Research Outcomes & Future Directions Module',
     'Overall cyber-physical resilience scores and future trend predictions for ADN security.')
]

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

for app, title, desc in new_apps:
    write(os.path.join(root, app, '__init__.py'), '')
    write(os.path.join(root, app, 'apps.py'), f"""from django.apps import AppConfig

class {app.capitalize().replace('_','')}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{app}'
""")
    # We will pass mock data directly to context
    write(os.path.join(root, app, 'views.py'), f"""from django.shortcuts import render
import random

MODULE_TITLE = '{title}'
MODULE_DESC = '{desc}'

def index(request):
    # Mock data generation for Chart.js
    labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    data_values = [random.randint(10, 90) for _ in range(6)]
    predictions = [val + random.randint(-10, 20) for val in data_values]

    context = {{
        'title': MODULE_TITLE,
        'description': MODULE_DESC,
        'labels': labels,
        'data_values': data_values,
        'predictions': predictions,
    }}
    return render(request, '{app}/index.html', context)
""")
    write(os.path.join(root, app, 'urls.py'), f"""from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='{app}_index'),
]
""")

    # We add Chart.js setup in the template
    template = f"""{{% extends 'base.html' %}}
{{% block content %}}
<div class="card p-5 mb-4 shadow-sm border-0" style="background: rgba(255, 255, 255, 0.85); backdrop-filter: blur(10px);">
    <h1 class="display-5 fw-bold text-primary mb-3">{{{{ title }}}}</h1>
    <p class="lead text-muted">{{{{ description }}}}</p>
    <hr class="my-4">
    <div class="row align-items-center">
        <div class="col-md-4 mb-3">
            <h4 class="fw-semibold">Module Details</h4>
            <ul class="list-group list-group-flush bg-transparent">
                <li class="list-group-item bg-transparent"><strong>Status:</strong> Active Analysis</li>
                <li class="list-group-item bg-transparent"><strong>Data Source:</strong> Simulated</li>
                <li class="list-group-item bg-transparent"><strong>Confidence:</strong> 92%</li>
            </ul>
        </div>
        <div class="col-md-8">
            <canvas id="moduleChart" height="120"></canvas>
        </div>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
    document.addEventListener("DOMContentLoaded", function() {{
        const ctx = document.getElementById('moduleChart').getContext('2d');
        const gradientBlue = ctx.createLinearGradient(0, 0, 0, 400);
        gradientBlue.addColorStop(0, 'rgba(13, 110, 253, 0.5)');
        gradientBlue.addColorStop(1, 'rgba(13, 110, 253, 0.05)');

        const gradientGreen = ctx.createLinearGradient(0, 0, 0, 400);
        gradientGreen.addColorStop(0, 'rgba(26, 188, 156, 0.5)');
        gradientGreen.addColorStop(1, 'rgba(26, 188, 156, 0.05)');

        new Chart(ctx, {{
            type: 'line',
            data: {{
                labels: {{{{ labels|safe }}}},
                datasets: [
                    {{
                        label: 'Current Values',
                        data: {{{{ data_values|safe }}}},
                        borderColor: '#0d6efd',
                        backgroundColor: gradientBlue,
                        borderWidth: 3,
                        tension: 0.4,
                        fill: true
                    }},
                    {{
                        label: 'Predicted Trend',
                        data: {{{{ predictions|safe }}}},
                        borderColor: '#1abc9c',
                        backgroundColor: gradientGreen,
                        borderWidth: 3,
                        borderDash: [5, 5],
                        tension: 0.4,
                        fill: true
                    }}
                ]
            }},
            options: {{
                responsive: true,
                plugins: {{
                    legend: {{ position: 'top' }},
                    tooltip: {{ mode: 'index', intersect: false }}
                }},
                scales: {{
                    x: {{ grid: {{ display: false }} }},
                    y: {{ grid: {{ color: 'rgba(0,0,0,0.05)' }} }}
                }}
            }}
        }});
    }});
</script>
{{% endblock %}}
"""
    write(os.path.join(root, 'templates', app, 'index.html'), template)

print('New apps scaffolded and old apps deleted.')
