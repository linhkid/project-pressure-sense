import anthropic
import os
import json
import dotenv
from utils.config_utils import CONFIG
from utils.file_utils import load_json, get_project_root, load_system_judge

dotenv.load_dotenv()

def main():
    try:
        client = anthropic.Anthropic(
            api_key=os.environ.get("ANTHROPIC_API_KEY")
        )

        json_file_path = os.path.join(CONFIG['scenarios_dir'], 'scenario_1', 'scenario_1_gpt4o.json')
        json_prompt = load_json(json_file_path)

        system_prompt = load_system_judge()

        messages = "Evaluate below conversation (in json format):\n"
        messages += json.dumps(json_prompt, indent=2)
        print("Sending the following to Claude for evaluation:")
        print(messages)

        message = client.messages.create(
            model=CONFIG.get('claude_model', 'claude-3-5-sonnet-20240620'),
            max_tokens=CONFIG['max_tokens'],
            temperature=CONFIG['temperature'],
            system=system_prompt,
            messages=[
                {
                    "role": "user",
                    "content": messages
                }
            ]
        )
        print("Claude's evaluation:")
        print(message.content)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()