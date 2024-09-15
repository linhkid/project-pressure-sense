import yaml
import json


class ChatUtils:
    def __init__(self, config_file='config.yaml'):
        self.config = self.load_config(config_file)

    def load_config(self, config_file):
        with open(config_file, 'r') as file:
            return yaml.safe_load(file)

    def format_conversation(self, messages):
        return {
            "model": self.config.get('model', 'meta-llama-3.1-8b-instruct'),
            "messages": messages,
            "temperature": self.config.get('temperature', 0.9),
            "top_p": self.config.get('top_p', 0.95),
            "max_tokens": self.config.get('max_tokens', 1024)
        }

    def process_data(self, data):
        # This is a placeholder function. Replace with actual data processing logic.
        processed_data = {
            "processed_" + key: value.upper() if isinstance(value, str) else value
            for key, value in data.items()
        }
        return processed_data

    def save_conversation(self, messages, data, filename='conversation.json'):
        conversation = self.format_conversation(messages)
        conversation["data"] = self.process_data(data)

        with open(filename, "w") as f:
            json.dump(conversation, f, indent=2)

    def load_conversation(self, filename='conversation.json'):
        try:
            with open(filename, "r") as f:
                conversation = json.load(f)
            return conversation["messages"], conversation.get("data", {})
        except FileNotFoundError:
            return [], {}


# Usage example
if __name__ == "__main__":
    utils = ChatUtils()
    messages = [{"role": "user", "content": "Hello"}]
    data = {"emotion": "happy", "risk_level": "low"}

    utils.save_conversation(messages, data)
    loaded_messages, loaded_data = utils.load_conversation()

    print("Loaded messages:", loaded_messages)
    print("Loaded data:", loaded_data)