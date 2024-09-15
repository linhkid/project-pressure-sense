# import requests
# import json
# import argparse
# import os
#
# LOCALAI_URL = "http://localhost:8080/v1/chat/completions"
# DEFAULT_MODEL = "meta-llama-3.1-8b-instruct"
#
# def load_system_message(scenario, reasoning):
#     file_name = f"prompts/system_instruction/peer_support_{'no_' if not reasoning else 'with_'}reasoning.txt"
#     try:
#         with open(file_name, 'r',encoding='utf-8') as file:
#             return file.read().strip()
#     except FileNotFoundError:
#         print(f"Warning: System instruction file '{file_name}' not found. Using default instruction.")
#         return "You are a helpful AI assistant."
#
#
# def get_ai_response(messages, model):
#     headers = {
#         "Content-Type": "application/json"
#     }
#     data = {
#         "model": model,
#         "messages": messages,
#         "temperature": 0.9,
#         "top_p": 0.95,
#         "max_tokens": 1024
#     }
#     response = requests.post(LOCALAI_URL, headers=headers, json=data)
#     return response.json()['choices'][0]['message']['content']
#
#
# def format_conversation(messages, model):
#     return {
#         "model": model,
#         "messages": messages,
#         "temperature": 0.9,
#         "top_p": 0.95,
#         "max_tokens": 1024
#     }
#
#
# def save_conversation(messages, scenario, model, reasoning):
#     # Get the directory of the current script
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#
#     # Construct the full path for the output file
#     output_dir = os.path.join(script_dir, "prompts", scenario)
#     fname = f"../{scenario}_{model}_{'with' if reasoning else 'without'}_reasoning.json"
#     full_path = os.path.join(output_dir, fname)
#
#     # Ensure the output directory exists
#     try:
#         os.makedirs(output_dir, exist_ok=True)
#     except Exception as e:
#         print(f"Error creating directory {output_dir}: {e}")
#         return
#
#     # Save the conversation
#     conversation = format_conversation(messages, model)
#     try:
#         with open(full_path, "w") as f:
#             json.dump(conversation, f, indent=2)
#         print(f"Conversation saved to {full_path}")
#     except Exception as e:
#         print(f"Error saving conversation to {full_path}: {e}")
# # def save_conversation(messages, scenario, model, reasoning):
# #     fname = f"../prompts/{scenario}/{scenario}_llama813b{'_with_reasoning' if reasoning else ''}.json"
# #     conversation = format_conversation(messages, model)
# #
# #     #os.makedirs(os.path.dirname(fname), exist_ok=True)
# #
# #     with open(fname, "w") as f:
# #         json.dump(conversation, f, indent=2)
# #     print(conversation)
# #     print('Saved file: {}'.format(fname))
# #     f.close()
#
# def main(scenario, model, reasoning):
#     system_message = load_system_message(scenario, reasoning)
#     messages = [
#         {
#             "role": "system",
#             "content": [
#                 {
#                     "type": "text",
#                     "text": system_message
#                 }
#             ]
#         }
#     ]
#     print(f"Starting chat with scenario {scenario}, model {model}, {'with' if reasoning else 'without'} reasoning.")
#     print("Type 'quit' to exit.")
#
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == 'quit':
#             break
#
#         messages.append({"role": "user", "content": user_input})
#         ai_response = get_ai_response(messages, model)
#         messages.append({"role": "assistant", "content": ai_response})
#
#         print(f"AI: {ai_response}")
#
#     save_conversation(messages, scenario, model, reasoning)
#
#
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Chat with an AI model.")
#     parser.add_argument("scenario", choices=['1', '2', '3'], help="Scenario number (1, 2, or 3)")
#     parser.add_argument("--model", default=DEFAULT_MODEL,
#                         help=f"Model type (default: {DEFAULT_MODEL})")
#     parser.add_argument("--reasoning", action="store_true", help="Include reasoning")
#
#     args = parser.parse_args()
#
#     main(f"scenario_{args.scenario}", args.model, args.reasoning)

import requests
import json
import argparse
import os
import sys

LOCALAI_URL = "http://localhost:8080/v1/chat/completions"
DEFAULT_MODEL = "meta-llama-3.1-8b-instruct"


def load_system_message(scenario, reasoning):
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_name = os.path.join(project_root, "prompts", "system_instruction",
                             f"peer_support_{'no_' if not reasoning else ''}reasoning.txt")
    try:
        with open(file_name, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Warning: System instruction file '{file_name}' not found. Using default instruction.")
        return "You are a helpful AI assistant."


def get_ai_response(messages, model):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": messages,
        "temperature": 0.9,
        "top_p": 0.95,
        "max_tokens": 1024
    }
    response = requests.post(LOCALAI_URL, headers=headers, json=data)
    return response.json()['choices'][0]['message']['content']


def format_conversation(messages, model):
    return {
        "model": model,
        "messages": messages,
        "temperature": 0.9,
        "top_p": 0.95,
        "max_tokens": 1024
    }


def save_conversation(messages, scenario, model, reasoning):
    # Get the project root directory (parent of src)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(project_root, "prompts", scenario)
    fname = f"{scenario}_{model}{'_with_reasoning' if reasoning else ''}.json"
    full_path = os.path.join(output_dir, fname)

    try:
        os.makedirs(output_dir, exist_ok=True)
    except Exception as e:
        print(f"Error creating directory {output_dir}: {e}")
        return

    # Save the conversation
    conversation = format_conversation(messages, model)
    try:
        with open(full_path, "w") as f:
            json.dump(conversation, f, indent=2)
        print(f"Conversation saved to {full_path}")
    except Exception as e:
        print(f"Error saving conversation to {full_path}: {e}")


def main(scenario, model, reasoning):
    system_message = load_system_message(scenario, reasoning)
    messages = [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": system_message
                }
            ]
        }
    ]
    print(f"Starting chat with scenario {scenario}, model {model}, {'with' if reasoning else 'without'} reasoning.")
    print("Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break

        messages.append({"role": "user", "content": user_input})
        ai_response = get_ai_response(messages, model)
        messages.append({"role": "assistant", "content": ai_response})

        print(f"AI: {ai_response}")

        save_conversation(messages, scenario, model, reasoning)
    print("Responses saved!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chat with an AI model.")
    parser.add_argument("scenario", choices=['1', '2', '3'], help="Scenario number (1, 2, or 3)")
    parser.add_argument("--model", default=DEFAULT_MODEL,
                        help=f"Model type (default: {DEFAULT_MODEL})")
    parser.add_argument("--reasoning", action="store_true", help="Include reasoning in the output")

    args = parser.parse_args()

    main(f"scenario_{args.scenario}", args.model, args.reasoning)