# education_qa.py - Simplified version
# No RAG for general questions, multimodal for page-based questions

import json
import re
from typing import Dict, List, Tuple, Optional
import requests
import base64
from pathlib import Path
from PIL import Image
import streamlit as st

class EducationQASystem:
    def __init__(self, base_path: str = "../datasets/education"):
        """Initialize simplified Education Q&A System"""
        self.base_path = Path(base_path)
        
        # Load structured data for page-based questions
        self.structured_data = self._load_json("education_structured_data_extract.json")
        
        # Ollama API endpoints
        self.text_model_url = "http://localhost:11434/api/generate"
        self.multimodal_model_url = "http://localhost:11434/api/generate"
        
        print(f"✅ Education system ready! Loaded {len(self.structured_data)} sections")
    
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
    
    def is_page_based_question(self, question: str) -> Tuple[bool, Optional[int]]:
        """Check if question mentions a specific page"""
        page_patterns = [
            r'(?:in|on|from|at)\s+page\s+(\d+)',
            r'page\s+(\d+)',
            r'p\.?\s*(\d+)',
            r'pg\.?\s*(\d+)'
        ]
        
        question_lower = question.lower()
        for pattern in page_patterns:
            match = re.search(pattern, question_lower)
            if match:
                return True, int(match.group(1))
        return False, None
    
    def answer_general_question(self, question: str) -> Dict:
        """Answer general question using fine-tuned model only"""
        print(f"🤖 General question: Using fine-tuned model directly")
        
        # Simple prompt for fine-tuned model
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
            
            print(f"✅ Fine-tuned model response: {len(answer)} characters")
            
            return {
                'answer': answer,
                'type': 'general',
                'sources': 'Fine-tuned model knowledge',
                'images': []
            }
            
        except Exception as e:
            return {
                'answer': f"Error: {e}",
                'type': 'general',
                'sources': [],
                'images': []
            }
    
    def get_page_info(self, page_number: int) -> Dict:
        """Get content and images for a specific page"""
        print(f"📖 Looking for page {page_number} content")
        
        matching_sections = []
        all_images = []
        
        if isinstance(self.structured_data, list):
            for section in self.structured_data:
                if not isinstance(section, dict):
                    continue
                
                page_start = section.get('page_start', 0)
                page_end = section.get('page_end', 0)
                
                if page_start <= page_number <= page_end:
                    matching_sections.append(section)
                    
                    # Get images for this page
                    section_images = section.get('images', [])
                    for img in section_images:
                        if isinstance(img, dict):
                            img_page = img.get('page', 0)
                            img_path = img.get('path', '')
                            if img_page == page_number and img_path:
                                all_images.append(img_path)
        
        if matching_sections:
            combined_text = "\n\n".join([
                f"{section.get('main_heading', '')} - {section.get('sub_heading', '')}\n{section.get('content', '')}"
                for section in matching_sections
            ])
            
            print(f"✅ Found {len(matching_sections)} sections, {len(all_images)} images")
            
            return {
                'text': combined_text,
                'images': all_images[:3],  # Max 3 images
                'sections': matching_sections
            }
        
        return {
            'text': f"No content found for page {page_number}",
            'images': [],
            'sections': []
        }
    
    def encode_image_to_base64(self, image_path: str) -> str:
        """Encode image to base64"""
        try:
            full_path = Path(image_path)
            if full_path.exists():
                with open(full_path, "rb") as image_file:
                    return base64.b64encode(image_file.read()).decode('utf-8')
            return ""
        except Exception as e:
            print(f"Error encoding {image_path}: {e}")
            return ""
    
    def answer_page_based_question(self, question: str, page_number: int) -> Dict:
        """Answer page-based question using multimodal model"""
        print(f"📖 Page-based question: Using multimodal model for page {page_number}")
        
        # Get page content and images
        page_info = self.get_page_info(page_number)
        
        if not page_info['text'] or 'No content found' in page_info['text']:
            return {
                'answer': f"No content found for page {page_number}",
                'type': 'page_based',
                'page_number': page_number,
                'images': []
            }
        
        # Process images with multimodal model
        image_analyses = []
        for image_path in page_info['images']:
            print(f"🖼️ Processing image: {Path(image_path).name}")
            
            image_base64 = self.encode_image_to_base64(image_path)
            if not image_base64:
                continue
            
            # Simple prompt for image analysis - just describe what you see
            prompt = "Describe what you see in this image."
            
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
        
        # Generate final answer using multimodal model with context + images
        print("🤖 Generating final answer with context...")
        
        # Simple final prompt
        final_prompt = f"""Context: {page_info['text']}

Question: {question}

Answer the question based on the page content above."""
        
        payload = {
            "model": "gemma3n:e4b",
            "prompt": final_prompt,
            "stream": False,
            "options": {
                "num_predict": 500,
                "temperature": 0.7
            }
        }
        
        try:
            response = requests.post(self.text_model_url, json=payload, timeout=60)
            response.raise_for_status()
            final_answer = response.json().get('response', '')
            
            print(f"✅ Final answer: {len(final_answer)} characters")
            
            return {
                'answer': final_answer,
                'type': 'page_based',
                'page_number': page_number,
                'images': image_analyses,
                'page_info': page_info
            }
            
        except Exception as e:
            return {
                'answer': f"Error generating answer: {e}",
                'type': 'page_based',
                'page_number': page_number,
                'images': image_analyses
            }
    
    def load_image_for_display(self, image_path: str):
        """Load image for Streamlit display"""
        try:
            full_path = Path(image_path)
            if full_path.exists():
                return Image.open(full_path)
            return None
        except Exception as e:
            return None
    
    def process_question(self, question: str) -> Dict:
        """Main method - route to appropriate handler"""
        print(f"\n🎯 Processing: {question}")
        
        # Check question type
        is_page_based, page_number = self.is_page_based_question(question)
        
        if is_page_based and page_number:
            return self.answer_page_based_question(question, page_number)
        else:
            return self.answer_general_question(question)

# Simple test
def test_both_types():
    """Test both question types"""
    qa_system = EducationQASystem("../datasets/education")
    
    # Test general question
    print("="*50)
    print("TESTING GENERAL QUESTION")
    print("="*50)
    result1 = qa_system.process_question("What is irrigation?")
    print(f"Answer: {result1['answer']}")
    
    # Test page-based question
    print("\n" + "="*50)
    print("TESTING PAGE-BASED QUESTION")
    print("="*50)
    result2 = qa_system.process_question("In page 20, explain about irrigation")
    print(f"Answer: {result2['answer']}")
    print(f"Images: {len(result2.get('images', []))}")

if __name__ == "__main__":
    test_both_types()