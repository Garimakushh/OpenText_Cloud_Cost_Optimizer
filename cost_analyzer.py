import json
import re
from llm_client import call_llm


def analyze_cost():
    # Load inputs
    with open("project_profile.json", "r", encoding="utf-8") as f:
        profile = json.load(f)

    with open("mock_billing.json", "r", encoding="utf-8") as f:
        billing = json.load(f)

    # Prompt for LLM

    prompt = f"""
You are an AI cloud cost optimization system.

Generate a COST OPTIMIZATION REPORT as STRICT JSON with the following structure:

{{
  "project_name": string,
  "analysis": {{
    "total_monthly_cost_inr": number,
    "budget_inr": number,
    "budget_variance_inr": number,
    "is_over_budget": boolean,
    "service_costs": {{ service_name: cost }},
    "high_cost_services": {{ service_name: cost }}
  }},
  "recommendations": [
    {{
      "title": string,
      "service": string,
      "current_cost": number,
      "potential_savings": number,
      "recommendation_type": string,
      "description": string,
      "implementation_effort": "low|medium|high",
      "risk_level": "low|medium|high",
      "cloud_providers": ["AWS", "Azure", "GCP", "OpenSource"]
    }}
  ],
  "summary": {{
    "total_potential_savings": number,
    "savings_percentage": number,
    "recommendations_count": number
  }}
}}

STRICT RULES:
- Output ONLY valid JSON
- NO markdown
- NO explanations
- NO headings
- 6–10 recommendations
- Recommendations must be multi-cloud (AWS, Azure, GCP, open-source/free-tier)

PROJECT PROFILE:
{json.dumps(profile, indent=2, ensure_ascii=False)}

BILLING DATA:
{json.dumps(billing, indent=2, ensure_ascii=False)}
"""

    # Call LLM
    response = call_llm(prompt, max_new_tokens=1400)

    # Extract JSON safely

    match = re.search(r"\{[\s\S]*\}", response)

    if not match:
        raise ValueError(
            "No valid JSON object found in LLM response.\n"
            f"Raw response:\n{response}"
        )

    json_text = match.group(0)

    try:
        data = json.loads(json_text)
    except json.JSONDecodeError:
        raise ValueError(
            "Failed to parse JSON from LLM response.\n"
            f"Extracted JSON:\n{json_text}"
        )


    # Save output
    with open("cost_optimization_report.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("✔ Cost optimization report generated successfully.")
