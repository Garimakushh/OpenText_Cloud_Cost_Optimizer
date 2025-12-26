import json
from llm_client import call_llm


def extract_profile(description: str):
    prompt = f"""
You are an AI system that extracts structured project requirements.

Generate ONLY a valid JSON object with the following fields:
- name (string)
- budget_inr_per_month (number)
- description (string)
- tech_stack (object)
- non_functional_requirements (array of strings)

Rules:
- Return STRICT JSON ONLY
- No markdown
- No explanation
- No extra text
- End the response with a closing brace }}
- Use INR for budget

PROJECT_DESCRIPTION:
{description}
"""

    response_text = call_llm(prompt)

    
    start = response_text.find("{")
    end = response_text.rfind("}")

    if start != -1 and end != -1:
        response_text = response_text[start:end + 1]

    try:
        data = json.loads(response_text)
    except json.JSONDecodeError:
        raise ValueError(
            "LLM returned invalid JSON for project profile.\n"
            f"Raw response:\n{response_text}"
        )

    #Basic Validation
    required_fields = [
        "name",
        "budget_inr_per_month",
        "description",
        "tech_stack",
        "non_functional_requirements"
    ]

    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field in project profile: {field}")

    # Output
    with open("project_profile.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
