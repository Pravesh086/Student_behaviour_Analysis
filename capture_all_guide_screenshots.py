import subprocess
import os
import time

edge_paths = [
    r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
    r'C:\Program Files\Microsoft\Edge\Application\msedge.exe',
    r'C:\Program Files\Google\Chrome\Application\chrome.exe'
]

browser = None
for p in edge_paths:
    if os.path.exists(p):
        browser = p
        break

if not browser:
    raise RuntimeError("No Chromium/Edge browser found.")

os.makedirs('figures', exist_ok=True)

screenshots = [
    ('figures/guide_step1_registration.png', 'http://localhost:8080/student_portal.html?view=register', 1440, 960),
    ('figures/guide_step2_assessment.png', 'http://localhost:8080/student_portal.html?view=test', 1440, 960),
    ('figures/guide_step3_kundali.png', 'http://localhost:8080/student_portal.html?view=kundali', 1440, 1100),
    ('figures/guide_step4_admin_portal.png', 'http://localhost:8080/student_portal.html?view=admin', 1440, 960),
    ('figures/guide_step5_main_overview.png', 'http://localhost:8080/?tab=overview', 1440, 960),
    ('figures/guide_step6_counselor_triage.png', 'http://localhost:8080/?tab=admin-portal', 1440, 960),
    ('figures/guide_step7_diagnostics.png', 'http://localhost:8080/?tab=diagnostics', 1440, 960),
    ('figures/guide_step8_counseling_center.png', 'http://localhost:8080/?tab=counseling', 1440, 960),
    ('figures/guide_step9_255_questions.png', 'http://localhost:8080/?tab=questions', 1440, 960),
    ('figures/guide_step10_correlation_heatmap.png', 'http://localhost:8080/?tab=correlations', 1440, 960),
    ('figures/guide_step11_ccro_recourse.png', 'http://localhost:8080/ccro_dashboard.html?view=mentor', 1440, 960)
]

for out_rel, url, w, h in screenshots:
    out_abs = os.path.abspath(out_rel)
    cmd = [
        browser,
        '--headless=new',
        '--disable-gpu',
        '--virtual-time-budget=3500',
        f'--window-size={w},{h}',
        f'--screenshot={out_abs}',
        url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    size = os.path.getsize(out_abs) if os.path.exists(out_abs) else 0
    print(f"Captured {out_rel} -> Exists: {os.path.exists(out_abs)}, Size: {size} bytes")

print("All screenshots generated successfully.")
