
# # backend/ml/code_explanation.py

# from . import model_loader
# import torch

# async def explain_code(prompt):
#     _, _, pipe = model_loader.load_model("codebert")

#     with torch.no_grad():
#         output = pipe(prompt, max_length=150, num_return_sequences=1)

#     explanation = output[0]['generated_text']
#     return explanation

# # Unload model after use to free up memory
# model_loader.unload_model("codebert")



# backend/ml/code_explanation.py
from utils.model_loader import model_loader
import torch
from common.error_handler import error_handler

@error_handler.handle_error
async def explain_code(prompt):
    _, _, pipe = await model_loader.load_model("codebert")

    async with torch.no_grad():
        output = await pipe(prompt, max_length=150, num_return_sequences=1)

    explanation = output[0]['generated_text']
    
    await model_loader.unload_model("codebert")
    return explanation