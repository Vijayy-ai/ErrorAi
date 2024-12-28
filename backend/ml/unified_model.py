import os
import aiohttp
from typing import Dict, Any
from common.error_handler import error_handler
import re

class UnifiedModelService:
    def __init__(self):
        self.api_key = os.getenv('HUGGINGFACE_API_KEY')
        if not self.api_key:
            raise ValueError("HUGGINGFACE_API_KEY environment variable is not set")
        self.api_base = "https://api-inference.huggingface.co/models"
        self.model = "mistralai/Mixtral-8x7B-Instruct-v0.1"

    async def process_input(self, message: str, task_type: str = None) -> Dict[str, Any]:
        try:
            headers = {"Authorization": f"Bearer {self.api_key}"}
            
            # Format the prompt based on task type
            prompt = self._format_prompt(message, task_type)
            
            payload = {
                "inputs": prompt,
                "parameters": {
                    "max_length": 2048,
                    "temperature": 0.7,
                    "top_p": 0.95,
                    "return_full_text": False
                }
            }

            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.api_base}/{self.model}",
                    headers=headers,
                    json=payload
                ) as response:
                    if response.status != 200:
                        error = await response.text()
                        return {
                            'error': f"API Error: {error}",
                            'status': response.status,
                            'success': False
                        }
                    
                    result = await response.json()
                    formatted_response = self._format_response(result)
                    return {
                        'response': formatted_response,
                        'task_type': task_type or self._detect_task_type(message),
                        'success': True
                    }
                    
        except Exception as e:
            error_result = error_handler(e)
            return {
                'error': error_result['error'],
                'status': error_result['status'],
                'success': False
            }

    def _detect_task_type(self, message: str) -> str:
        message = message.lower()
        if any(word in message for word in ["error", "fix", "debug", "solve"]):
            return "error_fixing"
        elif any(word in message for word in ["explain", "what", "how", "why"]):
            return "code_explanation"
        elif any(word in message for word in ["generate", "create", "write", "implement"]):
            return "code_generation"
        return "conversation"

    def _format_prompt(self, message: str, task_type: str = None) -> str:
        """Format the prompt based on task type for Mixtral"""
        if not task_type:
            task_type = self._detect_task_type(message)

        if task_type == "error_fixing":
            return f"""<s>[INST] You are an expert programmer. Fix the following error or issue:

{message}

Provide a detailed solution with code examples if necessary. [/INST]</s>"""
        
        elif task_type == "code_generation":
            return f"""<s>[INST] You are an expert programmer. Generate code for the following request:

{message}

Provide well-commented, production-ready code. [/INST]</s>"""
        
        elif task_type == "code_explanation":
            return f"""<s>[INST] You are an expert programmer. Explain the following code or concept:

{message}

Provide a detailed explanation with examples if helpful. [/INST]</s>"""
        
        else:
            return f"""<s>[INST] You are Error.AI, a helpful programming assistant.

{message} [/INST]</s>"""

    def _format_response(self, response: list) -> str:
        """Format the model's response"""
        if not response:
            return "I couldn't generate a response. Please try again."
            
        if isinstance(response, list):
            text = response[0].get('generated_text', '')
        else:
            text = str(response)
            
        # Clean up the response
        text = text.strip()
        
        # If response contains code, format it properly
        if '```' in text:
            return text
        
        # Detect if response is code
        if any(indicator in text for indicator in ['def ', 'class ', 'function', 'var ', 'const ']):
            lang = 'python' if any(py in text for py in ['def ', 'class ']) else 'javascript'
            return f"```{lang}\n{text}\n```"
            
        return text 