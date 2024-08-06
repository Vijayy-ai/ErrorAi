
# backend/ml/code_explanation.py

from . import model_loader
import torch

async def explain_code(prompt):
    _, _, pipe = model_loader.load_model("codebert")

    with torch.no_grad():
        output = pipe(prompt, max_length=150, num_return_sequences=1)

    explanation = output[0]['generated_text']
    return explanation

# Unload model after use to free up memory
model_loader.unload_model("codebert")
