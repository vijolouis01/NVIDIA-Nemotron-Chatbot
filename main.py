from dotenv import load_dotenv
import os
from openai import OpenAI

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

messages = [
     {
        "role": "system",
        "content": "You are a friendly Python tutor. Explain concepts in simple English and give short examples."
    }
]

while True:

    question = input("\nYou (or type 'exit' to stop): ")

    if not question.strip():
        print("\nPlease enter question")
        continue

    if question.strip().lower() == 'exit':
        print("\nGoodbye!")
        break

    messages.append({
        'role' : 'user',
        'content' : question
    })
        
    try:    
        response = client.chat.completions.create(
            model = 'nvidia/nemotron-3.5-super-vl-120b-a12b',
            messages=messages,
            max_tokens=1000,
        )

        answer = response.choices[0].message.content

        print(f"\nAI: {answer}")

        with open('chat_history.txt', 'a') as file:
            file.write(f"You: {question}\n")
            file.write(f"AI: {answer}\n\n")
            file.write("=======================================================================")


        messages.append(
            {
                'role': 'assistant',
                'content': answer
            }
        )

    except Exception as error:
        print(f"Something went wrong {error}")
        messages.pop()



    def main():
        print("\nHello from llm-learning!")


    if __name__ == "__main__":
        main()
