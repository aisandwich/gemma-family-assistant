# rao_vision_qa.py - Vision Assistant with Gemma 3 Multimodal

import requests
import base64
from PIL import Image
import io
import pyttsx3
import tempfile
import os

class RaoVisionQASystem:
    def __init__(self):
        self.model_url = "http://localhost:11434/api/generate"
        self.model = "gemma3:latest"  # Single Gemma 3 multimodal model
        
        # Initialize text-to-speech
        try:
            self.tts = pyttsx3.init()
            self.tts.setProperty('rate', 150)  # Speaking rate
            self.tts_available = True
        except:
            self.tts_available = False
    
    def encode_image_to_base64(self, image_data) -> str:
        """Convert uploaded image to base64"""
        try:
            # Read image bytes
            image_bytes = image_data.read()
            image = Image.open(io.BytesIO(image_bytes))
            
            # Convert to RGB if needed
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Convert back to bytes
            buffer = io.BytesIO()
            image.save(buffer, format='JPEG')
            image_bytes = buffer.getvalue()
            
            # Encode to base64
            return base64.b64encode(image_bytes).decode('utf-8')
        except Exception as e:
            print(f"Error encoding image: {e}")
            return ""
    
    def save_audio_temp(self, audio_data) -> str:
        """Save audio data to temporary file"""
        try:
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
            temp_file.write(audio_data)
            temp_file.close()
            return temp_file.name
        except Exception as e:
            print(f"Error saving audio: {e}")
            return ""
    
    def process_with_audio_and_image(self, image_data, audio_data) -> str:
        """Process both audio question and image with Gemma 3"""
        
        # Encode image
        image_base64 = self.encode_image_to_base64(image_data)
        if not image_base64:
            return "I couldn't process the image."
        
        # Save audio temporarily
        audio_file = self.save_audio_temp(audio_data)
        
        try:
            # Read audio file as base64 (for Gemma 3 multimodal)
            with open(audio_file, 'rb') as f:
                audio_base64 = base64.b64encode(f.read()).decode('utf-8')
            
            # Simple prompt for multimodal processing
            prompt = "Listen to the audio question and look at the image. Answer what the person is asking about the image."
            
            payload = {
                "model": self.model,
                "prompt": prompt,
                "images": [image_base64],
                "audio": [audio_base64],  # If Gemma 3 supports this format
                "stream": False,
                "options": {
                    "num_predict": 400,
                    "temperature": 0.7
                }
            }
            
            response = requests.post(self.model_url, json=payload, timeout=60)
            response.raise_for_status()
            return response.json().get('response', 'I cannot process this request.').strip()
            
        except Exception as e:
            return f"Error processing audio and image: {e}"
        finally:
            # Clean up temp file
            try:
                os.unlink(audio_file)
            except:
                pass
    
    def simple_image_description(self, image_data) -> str:
        """Simple image description only"""
        image_base64 = self.encode_image_to_base64(image_data)
        if not image_base64:
            return "I couldn't process the image."
        
        prompt = "Describe everything you can see in this image in detail. Be descriptive and helpful for someone who cannot see."
        
        payload = {
            "model": self.model,
            "prompt": prompt,
            "images": [image_base64],
            "stream": False,
            "options": {
                "num_predict": 400,
                "temperature": 0.7
            }
        }
        
        try:
            response = requests.post(self.model_url, json=payload, timeout=60)
            response.raise_for_status()
            return response.json().get('response', 'I cannot describe this image.').strip()
        except Exception as e:
            return f"I'm having trouble seeing the image. Error: {e}"
    
    def speak_text(self, text: str):
        """Convert text to speech for Rao"""
        if self.tts_available:
            try:
                self.tts.say(text)
                self.tts.runAndWait()
                return True
            except Exception as e:
                print(f"TTS Error: {e}")
                return False
        return False