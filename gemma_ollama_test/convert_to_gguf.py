from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load your fine-tuned model
model_path = "./gemma-qa-finetuned"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16)

# Save in a clean format
model.save_pretrained("./gemma-qa-clean")
tokenizer.save_pretrained("./gemma-qa-clean")
print("✅ Model converted to clean format")
