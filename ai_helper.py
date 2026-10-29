import os
from dotenv import load_dotenv

load_dotenv()

max_tokens = int(os.getenv('MAX_TOKENS'))

if max_tokens:
    print("\nMAX_TOKENS key loaded successfully")
else:
    print("\nMAX_TOKENS not found. Check your .env file")

model_name = os.getenv('MODEL_NAME')

if model_name:
    print("\nMODEL_NAME key loaded successfully")
else:
    print("\nnMODEL_NAME not found. Check your .env file")

def ask_ai(client, messages):
    response = client.chat.completions.create(
        model = model_name,
        messages=messages,
        max_tokens=max_tokens,
    )
    
    return response.choices[0].message.content