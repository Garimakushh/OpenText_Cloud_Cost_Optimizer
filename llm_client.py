import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_ID = "meta-llama/Meta-Llama-3-8B-Instruct"

print("Loading Meta-Llama tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

# Required for Meta-Llama
tokenizer.pad_token = tokenizer.eos_token

print("Loading Meta-Llama model (may take several minutes)...")
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto"
)

model.eval()
print("Meta-Llama model loaded successfully")


def call_llm(prompt: str, max_new_tokens: int = 600) -> str:
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        padding=True
    )

    input_ids = inputs["input_ids"].to(model.device)
    attention_mask = inputs["attention_mask"].to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_new_tokens=max_new_tokens,
            do_sample=False,  # deterministic
            pad_token_id=tokenizer.eos_token_id
        )

    generated_tokens = outputs[0][input_ids.shape[-1]:]

    return tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True
    ).strip()
