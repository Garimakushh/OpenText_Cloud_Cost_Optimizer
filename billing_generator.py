import json
import re
from llm_client import call_llm


def generate_billing():
    # Load project profile
    with open("project_profile.json", "r", encoding="utf-8") as f:
        profile = json.load(f)

    prompt = f"""
You are a cloud cost simulator.

Generate 12–20 realistic, cloud-agnostic billing records
for the following project.

STRICT RULES:
- Output ONLY JSON
- Each record MUST contain EXACTLY these fields:
  month, service, resource_id, region,
  usage_type, usage_quantity, unit, cost_inr, desc
- Use services like: EC2, RDS, Object Storage, Load Balancer, Monitoring
- Months like 2025-01, 2025-02
- Costs must be realistic and budget-aware
- NO explanations
- NO markdown
- NO headings

PROJECT PROFILE:
{json.dumps(profile, indent=2, ensure_ascii=False)}

FORMAT:
[
  {{
    "month": "2025-01",
    "service": "EC2",
    "resource_id": "i-food-web-01",
    "region": "ap-south-1",
    "usage_type": "Linux/UNIX (on-demand)",
    "usage_quantity": 720,
    "unit": "hours",
    "cost_inr": 900,
    "desc": "Food delivery web server"
  }}
]
"""

    response = call_llm(prompt, max_new_tokens=900)

    # Extract ALL JSON arrays from LLM output
    arrays = re.findall(r"\[[\s\S]*?\]", response)

    records = []

    for arr in arrays:
        try:
            parsed = json.loads(arr)
            if isinstance(parsed, list):
                records.extend(parsed)
        except json.JSONDecodeError:
            continue

    # Remove duplicates (same month + resource_id)
    unique = {}
    for r in records:
        key = (r.get("month"), r.get("resource_id"))
        unique[key] = r

    records = list(unique.values())

    # Save it
    with open("mock_billing.json", "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)

    # Warning if less records
    if len(records) < 12:
        print(
            f"Only {len(records)} billing records generated "
            "File saved successfully."
        )
    else:
        print(f"✔ {len(records)} billing records generated successfully.")
