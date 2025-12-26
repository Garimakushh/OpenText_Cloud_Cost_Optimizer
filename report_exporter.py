import json

def export_html():
    data = json.load(open("cost_optimization_report.json"))
    html = f"<h1>{data['project_name']}</h1><pre>{json.dumps(data, indent=2)}</pre>"
    open("cost_report.html", "w").write(html)
