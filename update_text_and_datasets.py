import os

root = os.path.dirname(os.path.abspath(__file__))

descriptions = {
    'adn_operations': "The cyber-physical aspects of each critical operation/component are analyzed.",
    'device_security': "Cybersecurity of ADN devices and sensors including Phasor Measurement Units (PMUs), smart meters, advanced metering infrastructure and protection relays are discussed in detail.",
    'communication_standards': "The challenges and requirements of associated communication protocols and standards are presented.",
    'application_drivers': "A thorough study of ADNs application drivers and enablers including microgrids, Electric Vehicles (EVs), Internet-of-Things (IoT) and smart homes is conducted.",
    'industry_solutions': "Potential and existing solutions by industry are highlighted.",
    'research_outcomes': "Survey outcomes and directions for future work are presented to highlight emerging avenues of research."
}

# Update views
for app, desc in descriptions.items():
    view_path = os.path.join(root, app, 'views.py')
    with open(view_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple regex or string slice to replace MODULE_DESC
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('MODULE_DESC ='):
            lines[i] = f'MODULE_DESC = "{desc}"'
    
    with open(view_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

print("Updated text descriptions in all views.")

# Generate datasets
import pandas as pd
import numpy as np

os.makedirs(os.path.join(root, 'datasets'), exist_ok=True)

# Dataset 1: Normal Operation Baseline
df1 = pd.DataFrame({
    'timestamp': pd.date_range(start='2024-01-01', periods=12, freq='M'),
    'critical_operations_load_mw': np.random.normal(50, 5, 12),
    'device_vulnerabilities_cve': np.random.randint(2, 10, 12),
    'protocol_packet_loss_pct': np.random.uniform(0.1, 0.5, 12),
    'ev_microgrid_integration_index': np.linspace(40, 80, 12) + np.random.normal(0, 2, 12),
    'industry_firewall_efficiency': np.random.uniform(95.0, 99.9, 12),
    'overall_resilience_score': np.linspace(70, 85, 12) + np.random.normal(0, 3, 12)
})
df1.to_csv(os.path.join(root, 'datasets', '1_normal_baseline.csv'), index=False)

# Dataset 2: Mass Cyber Attack Simulation
df2 = pd.DataFrame({
    'timestamp': pd.date_range(start='2024-01-01', periods=12, freq='M'),
    'critical_operations_load_mw': np.random.normal(120, 20, 12), # Stressed
    'device_vulnerabilities_cve': np.random.randint(15, 45, 12), # High CVEs
    'protocol_packet_loss_pct': np.random.uniform(15.0, 45.0, 12), # Massive packet loss
    'ev_microgrid_integration_index': np.linspace(30, 10, 12) - np.random.normal(0, 5, 12), # Cascading failure
    'industry_firewall_efficiency': np.random.uniform(40.0, 65.0, 12), # Breached
    'overall_resilience_score': np.linspace(45, 20, 12) - np.random.normal(0, 5, 12) # Plummeting
})
df2.to_csv(os.path.join(root, 'datasets', '2_cyber_attack_simulation.csv'), index=False)

# Dataset 3: Future Hardware/Standard Implementation
df3 = pd.DataFrame({
    'timestamp': pd.date_range(start='2024-01-01', periods=12, freq='M'),
    'critical_operations_load_mw': np.random.normal(45, 2, 12), # Ultra stable
    'device_vulnerabilities_cve': np.zeros(12), # Zero day mitigated
    'protocol_packet_loss_pct': np.random.uniform(0.01, 0.05, 12), # Negligible
    'ev_microgrid_integration_index': np.linspace(85, 99, 12) + np.random.normal(0, 1, 12), # Perfect integration
    'industry_firewall_efficiency': np.random.uniform(99.9, 100.0, 12), # Flawless
    'overall_resilience_score': np.linspace(90, 99, 12) + np.random.normal(0, 1, 12) # Peak resilience
})
df3.to_csv(os.path.join(root, 'datasets', '3_future_standards_forecast.csv'), index=False)

print("Generated 3 new CSV dataset variants in /datasets/")
