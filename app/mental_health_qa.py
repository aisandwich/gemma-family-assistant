# mental_health_qa.py - Simple Q&A system for mental health support

import json
import requests
from typing import Dict, List
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MentalHealthQASystem:
    def __init__(self, base_path: str = "datasets/depression"):
        """Initialize Simple Mental Health Q&A System"""
        self.base_path = Path(base_path)
        
        # Load structured data (optional, for context)
        self.structured_data = self._load_json("depression_structured_data_extract.json")
        
        # Ollama API configuration
        self.model_url = "http://localhost:11434/api/generate"
        self.model = "gemma-family:latest"  # Your fine-tuned model
        
        logger.info(f"✅ Mental Health system ready!")
        logger.info(f"💙 Loaded {len(self.structured_data)} depression support topics")
    
    def _load_json(self, filename: str) -> list:
        """Load JSON file with error handling"""
        try:
            file_path = self.base_path / filename
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                logger.info(f"✅ Loaded {filename}")
                return data if isinstance(data, list) else []
            else:
                logger.warning(f"⚠️ File not found: {filename}")
                return []
        except Exception as e:
            logger.error(f"❌ Error loading {filename}: {e}")
            return []
    
    def get_support(self, question: str) -> str:
        """Get mental health support response from fine-tuned model"""
        payload = {
            "model": self.model,
            "prompt": question,
            "stream": False,
            "options": {
                "num_predict": 400,  # Longer responses for mental health
                "temperature": 0.6,  # Slightly lower for more consistent support
                "top_p": 0.9,
                "top_k": 40
            }
        }
        
        try:
            logger.info(f"💙 Mental health question: {question[:50]}...")
            
            response = requests.post(self.model_url, json=payload, timeout=60)
            response.raise_for_status()
            
            answer = response.json().get('response', '').strip()
            logger.info(f"✅ Got support response: {len(answer)} chars")
            
            return answer
            
        except requests.exceptions.ConnectionError:
            logger.error("❌ Connection error - is Ollama running?")
            return "I'm having trouble connecting right now. Please ensure you have support from friends, family, or a mental health professional. If this is an emergency, please call a crisis hotline immediately."
            
        except requests.exceptions.Timeout:
            logger.warning("⏰ Request timeout")
            return "I'm taking longer than usual to respond. If you need immediate support, please reach out to a mental health professional or crisis hotline."
            
        except Exception as e:
            logger.error(f"❌ Error: {e}")
            return "I'm experiencing some difficulties right now. Please don't hesitate to reach out to a mental health professional, trusted friend, or crisis hotline for support."
    
    def get_sample_questions(self) -> List[str]:
        """Get sample mental health questions for demo"""
        return [
            "I've been feeling sad and empty lately. Could this be depression?",
            "What are the main symptoms of depression I should know about?",
            "How is depression different from just feeling down sometimes?",
            "What treatment options are available for depression?",
            "How can I support a friend who seems depressed?",
            "Where can I find help if I think I'm depressed?",
            "What should I do if someone mentions thoughts of suicide?",
            "How does depression affect women differently than men?"
        ]
    
    def check_ollama_status(self) -> bool:
        """Check if Ollama is running and model is available"""
        try:
            # Check if Ollama is running
            response = requests.get("http://localhost:11434/api/tags", timeout=5)
            if response.status_code != 200:
                return False
            
            # Check if our model is available
            models = response.json().get('models', [])
            model_names = [model.get('name', '') for model in models]
            
            return self.model in model_names
            
        except Exception:
            return False

# Simple test function
def test_mental_health_qa():
    """Test the Mental Health QA system"""
    qa_system = MentalHealthQASystem()
    
    if not qa_system.check_ollama_status():
        print("❌ Ollama not running or gemma-family model not available")
        return
    
    test_questions = [
        "I've been feeling really sad lately. What should I do?",
        "How can I help a friend who seems depressed?",
        "What are the signs of depression?"
    ]
    
    for question in test_questions:
        print(f"\nQ: {question}")
        answer = qa_system.get_support(question)
        print(f"A: {answer}")
        print("-" * 50)

if __name__ == "__main__":
    test_mental_health_qa()