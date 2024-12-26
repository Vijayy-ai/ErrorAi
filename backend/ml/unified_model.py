import os
import aiohttp
from typing import Dict, Any
from common.error_handler import error_handler
import re

class UnifiedModelService:
    def __init__(self):
        self.api_key = os.getenv('HUGGINGFACE_API_KEY')
        self.api_base = "https://api-inference.huggingface.co/models"
        self.models = {
            "code_generation": "Salesforce/codegen-350M-mono",
            "code_explanation": "microsoft/codebert-base",
            "error_fixing": "microsoft/codebert-base",
            "conversation": "facebook/blenderbot-400M-distill"
        }

    async def process_input(self, message: str, task_type: str = None) -> Dict[str, Any]:
        if not task_type:
            task_type = self._detect_task_type(message)

        try:
            model = self.models.get(task_type, self.models["conversation"])
            headers = {"Authorization": f"Bearer {self.api_key}"}
            payload = self._prepare_payload(message, task_type)

            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.api_base}/{model}",
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
                    formatted_response = self._format_response(result, task_type)
                    return {
                        'response': formatted_response,
                        'task_type': task_type,
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
        if any(word in message for word in ["error", "fix", "debug"]):
            return "error_fixing"
        elif any(word in message for word in ["explain", "what", "how", "why"]):
            return "code_explanation"
        elif any(word in message for word in ["generate", "create", "write"]):
            return "code_generation"
        return "conversation"

    def _format_response(self, response: list, task_type: str) -> str:
        if not response:
            return "I couldn't generate a response. Please try again."
            
        if task_type in ["code_generation", "error_fixing"]:
            if isinstance(response, list) and response:
                return self._format_code_response(response[0])
            return response[0].get('generated_text', '')
        
        return response[0].get('generated_text', 'I apologize, but I couldn\'t process your request properly.')
    
    def _format_code_response(self, response: Dict) -> str:
        """Format code responses with proper indentation and syntax"""
        if isinstance(response, dict) and 'generated_text' in response:
            code = response['generated_text']
            # Clean up the code
            code = code.strip()
            # Remove extra blank lines
            code = re.sub(r'\n\s*\n', '\n\n', code)
            return f"```python\n{code}\n```"
        return str(response) 

    def _prepare_payload(self, message: str, task_type: str) -> Dict[str, Any]:
        """Prepare model-specific payloads"""
        base_payload = {"inputs": message}
        
        if task_type == "code_generation":
            base_payload["parameters"] = {
                "max_length": 500,
                "temperature": 0.7,
                "top_p": 0.95
            }
        elif task_type == "error_fixing":
            base_payload["parameters"] = {
                "max_length": 300,
                "temperature": 0.3
            }
        
        return base_payload 