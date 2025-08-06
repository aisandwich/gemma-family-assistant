# ayurveda_qa.py - Simple Q&A like education_qa.py

import requests
from pathlib import Path

class AyurvedaQASystem:
    def __init__(self, base_path: str = "datasets/ayurveda"):
        self.base_path = Path(base_path)
        self.model_url = "http://localhost:11434/api/generate"
        
    def ask_remedy(self, question: str) -> str:
        """Simple question to fine-tuned model"""
        payload = {
            "model": "gemma-family:latest",
            "prompt": question,
            "stream": False,
            "options": {
                "num_predict": 300,
                "temperature": 0.7
            }
        }
        
        try:
            response = requests.post(self.model_url, json=payload, timeout=60)
            return response.json().get('response', '')
        except Exception as e:
            return f"Error: {e}"