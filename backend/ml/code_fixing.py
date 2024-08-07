# # backend/ml/code_fixing.py

# from . import model_loader
# import torch

# async def fix_code(prompt):
#     _, _, pipe = model_loader.load_model("codet5")

#     with torch.no_grad():
#         output = pipe(prompt, max_length=150, num_return_sequences=1)

#     fixed_code = output[0]['generated_text']
#     return fixed_code

# # Unload model after use to free up memory
# model_loader.unload_model("codet5")




# backend/ml/code_fixing.py
from utils.model_loader import model_loader
import torch
from common.error_handler import error_handler

@error_handler.handle_error
async def fix_code(prompt):
    _, _, pipe = await model_loader.load_model("codet5")

    async with torch.no_grad():
        output = await pipe(prompt, max_length=150, num_return_sequences=1)

    fixed_code = output[0]['generated_text']
    
    await model_loader.unload_model("codet5")
    return fixed_code


