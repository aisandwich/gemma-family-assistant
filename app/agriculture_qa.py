# agriculture_qa.py - Following the correct architecture
# 1. Ask gemma-family first
# 2. Then do RAG search  
# 3. Then ask gemma3:latest to summarize + process images

import json
import re
from typing import Dict, List, Tuple, Optional
import requests
import base64
from pathlib import Path
from PIL import Image
import streamlit as st

class AgricultureQASystem:
    def __init__(self, base_path: str = "../datasets/rice_diseases"):
        """Initialize Agriculture Q&A System"""
        self.base_path = Path(base_path)
        
        # Load structured agriculture data
        self.structured_data = self._load_json("rice_diseases_structured_data_extract.json")
        
        # Load Q&A results if available
        self.qa_results = self._load_json("rice_disease_qa_results.json")
        
        # Ollama API endpoints
        self.text_model_url = "http://localhost:11434/api/generate"
        self.multimodal_model_url = "http://localhost:11434/api/generate"
        
        print(f"✅ Agriculture system ready!")
        print(f"📚 Loaded {len(self.structured_data)} sections")
        print(f"🎯 Loaded {len(self.qa_results)} Q&A pairs")
    
    def _load_json(self, filename: str):
        """Load JSON file"""
        try:
            file_path = self.base_path / filename
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return []
        except Exception as e:
            print(f"Error loading {filename}: {e}")
            return []
    
    def ask_gemma_family_first(self, question: str) -> str:
        """Step 1: Always ask gemma-family first"""
        print(f"🤖 Step 1: Asking gemma-family fine-tuned model")
        
        prompt = f"Question: {question}\n\nAnswer:"
        
        payload = {
            "model": "gemma-family:latest",
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_predict": 500,
                "temperature": 0.7,
                "top_p": 0.9
            }
        }
        
        try:
            response = requests.post(self.text_model_url, json=payload, timeout=60)
            response.raise_for_status()
            answer = response.json().get('response', '')
            
            print(f"✅ Gemma-family response: {len(answer)} characters")
            return answer
            
        except Exception as e:
            print(f"❌ Gemma-family failed: {e}")
            return f"Error getting initial response: {e}"
    
    def rag_search_top_1(self, question: str) -> Optional[Dict]:
        """Step 2: Do RAG search to get top 1 match"""
        print(f"🔍 Step 2: RAG search for top 1 match")
        
        question_lower = question.lower()
        best_match = None
        best_score = 0
        
        # Search in structured data
        for section in self.structured_data:
            if not isinstance(section, dict):
                continue
                
            # Score based on keyword matches
            content = f"{section.get('main_heading', '')} {section.get('sub_heading', '')} {section.get('content', '')}"
            content_lower = content.lower()
            
            score = 0
            # Check for rice disease keywords
            disease_keywords = ['brown spot', 'blast', 'blight', 'disease', 'rice', 'leaf', 'grain', 'water', 'management']
            for keyword in disease_keywords:
                if keyword in question_lower and keyword in content_lower:
                    score += 10
            
            # General keyword matching
            question_words = question_lower.split()
            for word in question_words:
                if len(word) > 3 and word in content_lower:
                    score += 1
            
            if score > best_score:
                best_score = score
                best_match = section
        
        if best_match and best_score > 3:  # Lower threshold
            print(f"✅ RAG found match with score {best_score}: {best_match.get('main_heading', 'Unknown')}")
            return best_match
        
        print(f"⚠️ RAG: No good match found (best score: {best_score})")
        return None
    
    def ask_gemma3_for_content_summary(self, content: str, question: str) -> str:
        """Step 3a: Ask gemma3:latest to summarize RAG content"""
        print("🤖 Step 3a: Asking gemma3:latest to summarize content")
        
        prompt = f"""Content from knowledge base: {content}

Original question: {question}

Summarize the content above to answer the farmer's question about rice diseases or farming. Be practical and specific."""
        
        payload = {
            "model": "gemma3:latest",
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_predict": 400,
                "temperature": 0.7
            }
        }
        
        try:
            response = requests.post(self.text_model_url, json=payload, timeout=60)
            response.raise_for_status()
            summary = response.json().get('response', '')
            
            print(f"✅ Gemma3 content summary: {len(summary)} characters")
            return summary
            
        except Exception as e:
            print(f"❌ Gemma3 content summarization failed: {e}")
            return content[:500] + "..."
    
    def encode_image_to_base64(self, image_path: str) -> str:
        """Encode image to base64"""
        try:
            # Try multiple path combinations
            full_path = Path(image_path)
            if not full_path.exists():
                full_path = self.base_path / image_path
            if not full_path.exists():
                full_path = self.base_path / "images" / Path(image_path).name
                
            if full_path.exists():
                with open(full_path, "rb") as image_file:
                    return base64.b64encode(image_file.read()).decode('utf-8')
            return ""
        except Exception as e:
            print(f"Error encoding {image_path}: {e}")
            return ""
    
    def ask_gemma3_for_images(self, images: List[str]) -> List[Dict]:
        """Step 3b: Ask gemma3:latest to process images"""
        print(f"🖼️ Step 3b: Asking gemma3:latest to process {len(images)} images")
        
        image_analyses = []
        
        for image_path in images[:3]:  # Max 3 images
            print(f"🖼️ Processing image: {Path(image_path).name}")
            
            image_base64 = self.encode_image_to_base64(image_path)
            if not image_base64:
                continue
            
            prompt = "Describe what you see in this rice farming image. Focus on diseases, pests, or farming techniques shown."
            
            payload = {
                "model": "gemma3:latest",
                "prompt": prompt,
                "images": [image_base64],
                "stream": False,
                "options": {
                    "num_predict": 300,
                    "temperature": 0.7
                }
            }
            
            try:
                response = requests.post(self.multimodal_model_url, json=payload, timeout=60)
                response.raise_for_status()
                explanation = response.json().get('response', '')
                
                image_analyses.append({
                    'image_path': image_path,
                    'explanation': explanation
                })
                print(f"✅ Image analyzed: {len(explanation)} characters")
                
            except Exception as e:
                print(f"❌ Image analysis failed: {e}")
        
        return image_analyses
    
    def load_image_for_display(self, image_path: str):
        """Load image for Streamlit display"""
        try:
            # Try multiple path combinations
            full_path = Path(image_path)
            if not full_path.exists():
                full_path = self.base_path / image_path
            if not full_path.exists():
                full_path = self.base_path / "images" / Path(image_path).name
                
            if full_path.exists():
                return Image.open(full_path)
            return None
        except Exception as e:
            print(f"Error loading image {image_path}: {e}")
            return None
    
    def process_farming_question(self, question: str) -> Dict:
        """Main method following the correct architecture"""
        print(f"\n🎯 Processing farming question: {question}")
        print("="*60)
        
        # STEP 1: Always ask gemma-family first
        gemma_family_answer = self.ask_gemma_family_first(question)
        
        # STEP 2: Do RAG search for top 1 match
        rag_match = self.rag_search_top_1(question)
        
        if not rag_match:
            # No RAG match - return gemma-family answer only
            print("✅ Final result: gemma-family answer only (no RAG match)")
            return {
                'answer': gemma_family_answer,
                'type': 'gemma_family_only',
                'sources': 'Fine-tuned model knowledge',
                'images': []
            }
        
        # STEP 3a: Ask gemma3:latest to summarize RAG content
        rag_content = f"{rag_match.get('main_heading', '')} - {rag_match.get('sub_heading', '')}\n\n{rag_match.get('content', '')}"
        rag_summary = self.ask_gemma3_for_content_summary(rag_content, question)
        
        # STEP 3b: Ask gemma3:latest to process images (if any)
        images = rag_match.get('images', [])
        image_analyses = []
        if images:
            image_analyses = self.ask_gemma3_for_images(images)
        
        # STEP 4: Combine all results
        final_answer = f"**From fine-tuned model:**\n{gemma_family_answer}\n\n**From knowledge base:**\n{rag_summary}"
        
        if image_analyses:
            final_answer += "\n\n**Related Images Show:**\n"
            for i, img_analysis in enumerate(image_analyses, 1):
                final_answer += f"\n{i}. {img_analysis['explanation']}"
        
        print("✅ Final result: Combined gemma-family + RAG + images")
        return {
            'answer': final_answer,
            'type': 'full_pipeline',
            'sources': f"Fine-tuned model + {rag_match.get('main_heading', 'Knowledge base')}",
            'images': image_analyses,
            'rag_match': rag_match,
            'gemma_family_answer': gemma_family_answer
        }

# Simple test
def test_architecture():
    """Test the correct architecture"""
    qa_system = AgricultureQASystem("../datasets/rice_diseases")
    
    print("="*50)
    print("TESTING CORRECT ARCHITECTURE")
    print("="*50)
    result = qa_system.process_farming_question("What role does water management play in Brown Spot disease control?")
    print(f"\nFinal Answer: {result['answer']}")
    print(f"Type: {result['type']}")
    print(f"Images: {len(result.get('images', []))}")

if __name__ == "__main__":
    test_architecture()