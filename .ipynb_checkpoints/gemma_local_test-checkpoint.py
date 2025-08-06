import requests

response = requests.post(
    'http://localhost:11434/api/generate',
    json={
        'model': 'gemma3n:e4b',
        'prompt': 'Explain photosynthesis in simple terms',
        'stream': False
    }
)

print(response.json()['response'])