# Chatbot

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
- uv for dependency and environment management

## Prerequisites
- Python 3.12+
- uv installed on your machine

Install uv if you do not already have it:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

For Windows PowerShell, you can use:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Setup

1. Clone the repository and change into the project directory:

   ```bash
   git clone https://github.com/vijolouis01/NVIDIA-Nemotron-Chatbot.git
   cd NVIDIA-Nemotron-Chatbot
   ```

2. Create the project environment and install dependencies with uv:

   ```bash
   uv sync
   ```

   This creates a local virtual environment and installs the packages from `pyproject.toml`.

3. Create a `.env` file in the project root and add your NVIDIA API key:

   ```env
   NVIDIA_API_KEY=your_api_key_here
   ```

4. Run the chatbot:

   ```bash
   uv run python main.py
   ```

## Commands
- `help` — Show available commands.
- `clear` — Clear conversation memory.
- `exit` — Stop the chatbot.

## Security
Never share your API key or upload your `.env` file to GitHub.

## Useful uv commands
- `uv sync` — install dependencies from `pyproject.toml`
- `uv run python main.py` — run the app in the managed environment
- `uv add <package>` — add a dependency to the project
- `uv remove <package>` — remove a dependency from the project
