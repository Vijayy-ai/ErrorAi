# backend/ml/conversation.py

from . import model_loader
import torch

async def generate_response(prompt):
    _, _, pipe = model_loader.load_model("jamba")

    with torch.no_grad():
        output = pipe(prompt, max_length=150, num_return_sequences=1)

    response = output[0]['generated_text']
    return response

# Unload model after use to free up memory
model_loader.unload_model("jamba")
