from openai import OpenAI
import os
from getpass import getpass
import dotenv
from utils.config_utils import CONFIG
from utils.file_utils import load_json

dotenv.load_dotenv()

def main():
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        openai_api_key = getpass(prompt="Please enter your OpenAI API key: ")

    client = OpenAI(api_key=openai_api_key)

    json_file_path = os.path.join(CONFIG['scenarios_dir'], 'scenario_1', 'scenario_1_gpt4o.json')
    json_prompt = load_json(json_file_path)

    model = json_prompt.get("model", "")
    messages = json_prompt.get("messages", [])

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=CONFIG['max_tokens']
    )

    print(response.choices[0])

if __name__ == "__main__":
    main()