import argparse
from utils.config_utils import CONFIG
from utils.file_utils import load_system_message, save_conversation
from utils.api_utils import get_ai_response

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
    parser.add_argument("--model", default=CONFIG['default_model'],
                        help=f"Model type (default: {CONFIG['default_model']})")
    parser.add_argument("--reasoning", action="store_true", help="Include reasoning in the output")

    args = parser.parse_args()

    main(f"scenario_{args.scenario}", args.model, args.reasoning)