import openai
from openai import OpenAI

import os
from getpass import getpass
import json
import dotenv
dotenv.load_dotenv()
def main():
    # Fetch the OpenAI API key from an environment variable or prompt the user for it
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        openai_api_key = getpass(prompt="Please enter your OpenAI API key: ")

    # Set the API key for the OpenAI library
    openai.api_key = openai_api_key

    # Read the JSON prompt from the file
    json_file_path = 'prompts/pressure_sense_emotion/scenario_2_with_reasoning.json'

    # Make a request to the OpenAI API
    client = OpenAI()
    # Read the JSON prompt from the file
    with open(json_file_path, 'r') as file:
        json_prompt = json.load(file)

    # Construct messages for the chat completion
    model = json_prompt.get("model", "")
    messages = json_prompt.get("messages", [])
    #max_tokens = json_prompt.get("max_tokens", 512)

    response = client.chat.completions.create(
        #gpt-4o-2024-08-06
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=2048
    )

    print(response.choices[0])

if __name__ == "__main__":
    main()
