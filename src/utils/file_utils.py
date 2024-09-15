import os
import json
from .config_utils import CONFIG

def load_system_message(scenario, reasoning):
    file_name = os.path.join(CONFIG['system_instruction_dir'],
                             f"peer_support_{'no_' if not reasoning else ''}reasoning.txt")
    try:
        with open(file_name, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Warning: System instruction file '{file_name}' not found. Using default instruction.")
        return "You are a helpful AI assistant."

def save_conversation(messages, scenario, model, reasoning):
    output_dir = os.path.join(CONFIG['scenarios_dir'], scenario)
    fname = f"{scenario}_{model}{'_with_reasoning' if reasoning else ''}.json"
    full_path = os.path.join(output_dir, fname)

    try:
        os.makedirs(output_dir, exist_ok=True)
    except Exception as e:
        print(f"Error creating directory {output_dir}: {e}")
        return

    conversation = {
        "model": model,
        "messages": messages,
        "temperature": CONFIG['temperature'],
        "top_p": CONFIG['top_p'],
        "max_tokens": CONFIG['max_tokens']
    }

    try:
        with open(full_path, "w") as f:
            json.dump(conversation, f, indent=2)
        #print(f"Conversation saved to {full_path}")
    except Exception as e:
        print(f"Error saving conversation to {full_path}: {e}")

def load_json(path):
    with open(path, "r") as reader:
        return json.load(reader)