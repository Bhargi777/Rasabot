from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = "G:\\Sem1\\actualchatbotrasa\\models\\openhermes-2-mistral-7b.Q4_K_M.gguf"
model = AutoModelForCausalLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

print("Model loaded successfully!")
