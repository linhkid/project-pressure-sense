import requests
from .config_utils import CONFIG

def get_ai_response(messages, model):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": messages,
        "temperature": CONFIG['temperature'],
        "top_p": CONFIG['top_p'],
        "max_tokens": CONFIG['max_tokens']
    }
    response = requests.post(CONFIG['localai_url'], headers=headers, json=data)
    return response.json()['choices'][0]['message']['content']