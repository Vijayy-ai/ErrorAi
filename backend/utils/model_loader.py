#backend/utils/model_loader.py
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM, pipeline
import torch
from functools import lru_cache

class ModelLoader:
    def __init__(self):
        self.models = {}
        self.tokenizers = {}
        self.pipelines = {}

    @lru_cache(maxsize=None)
    def load_model(self, model_name):
        if model_name not in self.models:
            model_config = {
                "codegen": ("Salesforce/codegen-16B-multi", AutoModelForCausalLM, "text-generation"),
                "codet5": ("Salesforce/codet5p-16b", AutoModelForSeq2SeqLM, "text2text-generation"),
                "codebert": ("microsoft/codebert-base", AutoModelForSeq2SeqLM, "feature-extraction"),
                "jamba": ("ai21labs/Jamba-tiny-random", AutoModelForCausalLM, "text-generation")
            }

            if model_name in model_config:
                model_path, model_class, pipeline_task = model_config[model_name]
                
                # Load tokenizer
                self.tokenizers[model_name] = AutoTokenizer.from_pretrained(model_path)

                # Load model with quantization
                self.models[model_name] = model_class.from_pretrained(
                    model_path,
                    torch_dtype=torch.float16,  # Use float16 for quantization
                    device_map="auto",  # Automatically choose the best device
                    low_cpu_mem_usage=True,  # Optimize for lower CPU memory usage
                )

                # Move model to appropriate device
                device = 'cuda' if torch.cuda.is_available() else 'cpu'
                self.models[model_name].to(device)

                # Create pipeline
                self.pipelines[model_name] = pipeline(
                    pipeline_task,
                    model=self.models[model_name],
                    tokenizer=self.tokenizers[model_name],
                    device=device
                )

        return self.models[model_name], self.tokenizers[model_name], self.pipelines[model_name]

    def unload_model(self, model_name):
        if model_name in self.models:
            del self.models[model_name]
            del self.tokenizers[model_name]
            del self.pipelines[model_name]
            torch.cuda.empty_cache()  # Clear CUDA cache to free up memory

model_loader = ModelLoader()