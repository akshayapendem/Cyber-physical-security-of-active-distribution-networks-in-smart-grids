import os

root = os.path.dirname(os.path.abspath(__file__))

apps = [
    ('device_security', 1),
    ('communication_standards', 2),
    ('application_drivers', 3),
    ('industry_solutions', 4),
    ('research_outcomes', 5)
]

for app, col_idx in apps:
    view_path = os.path.join(root, app, 'views.py')
    with open(view_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We replace the generation part
    new_imports = "from django.shortcuts import render\nimport random\nimport pandas as pd\nfrom adn_operations.models import UploadedDataset"
    
    logic = f"""    labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    data_values = [random.randint(10, 90) for _ in range(6)]
    
    # Try fetching latest dataset
    latest_dataset = UploadedDataset.objects.order_by('-uploaded_at').first()
    if latest_dataset:
        try:
            df = pd.read_csv(latest_dataset.file.path)
            numeric_cols = df.select_dtypes(include='number').columns
            if len(numeric_cols) > {col_idx}:
                vals = df[numeric_cols[{col_idx}]].dropna().head(6).tolist()
                if len(vals) > 0:
                    data_values = vals
                    while len(data_values) < 6:
                        data_values.append(random.randint(10, 90))
        except Exception as e:
            pass # fallback

    predictions = [val + random.randint(-10, 20) for val in data_values]"""

    content = content.replace("from django.shortcuts import render\nimport random", new_imports)
    old_logic = "    labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']\n    data_values = [random.randint(10, 90) for _ in range(6)]\n    predictions = [val + random.randint(-10, 20) for val in data_values]"
    content = content.replace(old_logic, logic)

    with open(view_path, 'w', encoding='utf-8') as f:
        f.write(content)
print("Updated all views!")
