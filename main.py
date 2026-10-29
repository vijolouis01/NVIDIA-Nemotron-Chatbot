from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

api_key = os.getenv('NVIDIA_API_KEY')

if api_key:
    print("NVIDIA API key loaded successfully")
else:
    print("API key not found. Check your .env file")

client = OpenAI(
    base_url= 'https://integrate.api.nvidia.com/v1',
    api_key = api_key
)

question = input('Enter your Question: ')

if not question.strip():
    print("Please enter question")
    exit()

response = client.chat.completions.create(
    model = 'nvidia/nemotron-3.5-super-vl-120b-a12b',
    messages=[
        {
            'role': 'user',
            'content': question
        }
    ],
    max_tokens=500
)

print(response.choices[0].message.content)



def main():
    print("Hello from llm-learning!")


if __name__ == "__main__":
    main()
