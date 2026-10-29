# NVIDIA Nemotron Chatbot

## About
A simple AI chatbot built using Python and the NVIDIA Nemotron API.

## Features
- Ask questions and receive AI answers.
- Remember previous messages during a conversation.
- Clear conversation memory.
- Save chat history to a file.
- Handle API errors.
- Validate user input.

## Technologies
- Python
- NVIDIA Nemotron API
- OpenAI Python library
- python-dotenv

## Setup

1. Create and activate a virtual environment.
2. Install the required packages:

   `python -m pip install -r requirements.txt`

3. Add your NVIDIA API key to the `.env` file:

   `NVIDIA_API_KEY=your_api_key_here`

4. Run the chatbot:

   `python main.py`

## Commands
- `help` — Show available commands.
- `clear` — Clear conversation memory.
- `exit` — Stop the chatbot.

## Security
Never share your API key or upload your `.env` file to GitHub.