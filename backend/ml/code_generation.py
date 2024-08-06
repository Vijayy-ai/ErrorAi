# backend/ml/code_generation.py

from .import model_loader
import torch

async def generate_code(prompt):
    _, _, pipe = model_loader.load_model("codegen")

    with torch.no_grad():
        output = pipe(prompt, max_length=150, num_return_sequences=1)

    generated_code = output[0]['generated_text']
    return generated_code

# Unload model after use to free up memory
model_loader.unload_model("codegen")