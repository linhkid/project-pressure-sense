import os
import json
from .config_utils import CONFIG

def get_project_root():
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def load_system_message(scenario, reasoning):
    file_name = os.path.join(CONFIG['system_instruction_dir'],
                             f"peer_support_{'no_' if not reasoning else 'with_'}reasoning.txt")
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Warning: System instruction file '{file_name}' not found. Using default instruction.")
        return "You are a helpful AI assistant."
def load_system_judge():
    project_root = get_project_root()
   # prompt_path = os.path.join(project_root, CONFIG['system_prompt_file'])
    prompt_path = os.path.join(project_root, CONFIG['system_instruction_dir'], CONFIG['system_prompt_file'])
    try:
        with open(prompt_path, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: System prompt file not found at {prompt_path}")
        raise
    except Exception as e:
        print(f"Error reading system prompt file: {e}")
        raise
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
    project_root = get_project_root()
    full_path = os.path.join(project_root, path)
    try:
        with open(full_path, "r") as reader:
            return json.load(reader)
    except FileNotFoundError:
        print(f"Error: File not found at {full_path}")
        raise