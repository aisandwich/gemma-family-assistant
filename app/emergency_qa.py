# emergency_qa.py - Simple Q&A for emergency management

import requests

class EmergencyQASystem:
    def __init__(self):
        self.model_url = "http://localhost:11434/api/generate"
        self.model = "gemma-family:latest"
    
    def get_emergency_guidance(self, question: str) -> str:
        payload = {
            "model": self.model,
            "prompt": question,
            "stream": False,
            "options": {
                "num_predict": 350,
                "temperature": 0.7
            }
        }
        
        try:
            response = requests.post(self.model_url, json=payload, timeout=60)
            response.raise_for_status()
            return response.json().get('response', '').strip()
        except Exception as e:
            return f"For immediate emergencies, call 112. Error: {e}"