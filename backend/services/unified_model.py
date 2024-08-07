
# # backend/ml/unified_model.py

# import re
# from transformers import pipeline
# import torch
# from utils.model_loader import ModelLoader
# # from common import error_handler
# from common.error_handler import error_handler
# # from common import response_cache
# from common.cache import response_cache

# class UnifiedModel:
#     def __init__(self):
#         self.model_loader = ModelLoader()
#         self.models = {}
#         self.task_classifier = pipeline("text-classification", 
#                                         model="distilbert-base-uncased-finetuned-sst-2-english", 
#                                         device=0 if torch.cuda.is_available() else -1)

#     @error_handler.handle_error
#     async def process_input(self, user_input):
#         cache_key = f"response_{hash(user_input)}"
#         cached_response = response_cache.get(cache_key)
#         if cached_response:
#             return cached_response

#         task = self.determine_task(user_input)
#         model_name = self.get_model_for_task(task)
#         model, tokenizer, pipe = await self.model_loader.load_model(model_name)

#         async with torch.no_grad():
#             if task in ["generate_code", "fix_code", "generate_response"]:
#                 output = await pipe(user_input, max_length=150, num_return_sequences=1)
#                 response = output[0]['generated_text']
#             elif task == "explain_code":
#                 inputs = tokenizer(user_input, return_tensors="pt", truncation=True, max_length=512)
#                 inputs = {k: v.to(model.device) for k, v in inputs.items()}
#                 features = await model(**inputs).last_hidden_state
#                 response = self.convert_features_to_explanation(features)

#         response_cache.set(cache_key, response)
#         return response

#     def get_model_for_task(self, task):
#         task_model_mapping = {
#             "generate_code": "codegen",
#             "fix_code": "codet5",
#             "explain_code": "codebert",
#             "generate_response": "jamba"
#         }
#         return task_model_mapping.get(task, "jamba")

#     def convert_features_to_explanation(self, features):
#         explanation = "The code performs the following tasks:\n"
#         for i, feature in enumerate(features[0]):
#             explanation += f"Step {i+1}: {self.interpret_feature(feature)}\n"
#         return explanation

#     def interpret_feature(self, feature):
#         return "This part of the code does something important."

# unified_model = UnifiedModel()




































#service/unified_model.py
import torch
from transformers import pipeline
from utils.model_loader import model_loader
from common.error_handler import error_handler
from common.cache import response_cache
from ml.code_explanation import explain_code
from ml.code_fixing import fix_code
from ml.code_generation import generate_code
from ml.conversation import generate_response

class UnifiedModel:
    def __init__(self):
        self.task_classifier = pipeline("text-classification", 
                                        model="distilbert-base-uncased-finetuned-sst-2-english", 
                                        device=0 if torch.cuda.is_available() else -1)

    @error_handler.handle_error
    async def process_input(self, user_input):
        cache_key = f"response{hash(user_input)}"
        cached_response = await response_cache.get(cache_key)
        if cached_response:
            return cached_response

        task = await self.determine_task(user_input)
        
        if task == "generate_code":
            response = await generate_code(user_input)
        elif task == "fix_code":
            response = await fix_code(user_input)
        elif task == "explain_code":
            response = await explain_code(user_input)
        else:
            response = await generate_response(user_input)

        await response_cache.set(cache_key, response)
        return response

    async def determine_task(self, user_input):
        result = await self.task_classifier(user_input)
        label = result[0]['label']
        if 'code' in label.lower():
            if 'generate' in label.lower():
                return 'generate_code'
            elif 'fix' in label.lower():
                return 'fix_code'
            elif 'explain' in label.lower():
                return 'explain_code'
        return 'generate_response'

unified_model = UnifiedModel()