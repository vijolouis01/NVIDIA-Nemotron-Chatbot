from dotenv import load_dotenv
import os
from openai import OpenAI
from ai_helper import ask_ai
from input_helper import is_valid_question 
from datetime import datetime

load_dotenv()

api_key = os.getenv('NVIDIA_API_KEY')

if api_key:
    print("\nNVIDIA API key loaded successfully")
else:
    print("\nAPI key not found. Check your .env file")


client = OpenAI(
    base_url= 'https://integrate.api.nvidia.com/v1',
    api_key = api_key
)

SYSTEM_MESSAGE = (
    "You are a friendly Python tutor. "
    "Explain concepts in simple English and give short examples."
)

messages = [
     {
        "role": "system",
        "content": SYSTEM_MESSAGE
    }
]

def main():
    global messages
    print("\nWelcome to your NVIDIA Nemotron chatbot!")
    print("\nType 'help' for commands or 'exit' to stop.")

    while True:
        question = input("\nYou: ")
        if question.strip().lower() == 'exit':
            print("\nGoodbye!")
            break

        if question.lower() == "help":
            print("\nAvailable commands:")
            print("help  - Show available commands")
            print("clear - Clear conversation memory")
            print("exit  - Stop the chatbot")
            continue
        
        if not is_valid_question(question):
            print("\nPlease enter a question between 1 and 500 characters.")
            continue

        if question.strip() == 'clear':
            messages = [
                {
                    'role': 'system',
                    'content' : SYSTEM_MESSAGE
                }
            ]

            print("\nConversation cleared successfully!")
            continue

        messages.append({
            'role' : 'user',
            'content' : question
        })
        
        try:

            print("\nAI is thinking...........")
            
            answer = ask_ai(client, messages)

            if answer is None:
                messages.pop()
                continue

            print(f"\nAI: {answer}")

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:

                with open('chat_history.txt', 'a') as file:
                    file.write(f"[{timestamp}] You: {question}\n")
                    file.write(f"[{timestamp}] AI: {answer}\n\n")
                    file.write("=" * 60 + "\n")
            except OSError as error:
                print("Could not save chat history:", error)

            messages.append(
                {
                    'role': 'assistant',
                    'content': answer
                }
            )

        except Exception as error:
            print(f"Something went wrong {error}")
            if messages and messages[-1]["role"] == "user":
                messages.pop()


if __name__ == "__main__":
     main()
