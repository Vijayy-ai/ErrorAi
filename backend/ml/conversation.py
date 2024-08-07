# # backend/ml/conversation.py

# from . import model_loader
# import torch

# async def generate_response(prompt):
#     _, _, pipe = model_loader.load_model("jamba")

#     with torch.no_grad():
#         output = pipe(prompt, max_length=150, num_return_sequences=1)

#     response = output[0]['generated_text']
#     return response

# # Unload model after use to free up memory
# model_loader.unload_model("jamba")


# backend/ml/conversation.py
from utils.model_loader import model_loader
import torch
from common.error_handler import error_handler

@error_handler.handle_error
async def generate_response(prompt):
    _, _, pipe = await model_loader.load_model("jamba")

    async with torch.no_grad():
        output = await pipe(prompt, max_length=150, num_return_sequences=1)

    response = output[0]['generated_text']
    
    await model_loader.unload_model("jamba")
    return response