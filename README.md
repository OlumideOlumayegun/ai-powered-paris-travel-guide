# AI-Powered Paris Travel Guide

![eiffel-tower](images/eiffel-tower.png)

A small Python project that uses the OpenAI API to answer predefined tourist questions about Paris for **Tour Company**.

## Project goal

This chatbot answers three required questions:

1. How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?
2. Where is the Arc de Triomphe?
3. What are the must-see artworks at the Louvre Museum?

The implementation follows the hands-on project requirements:

- uses the OpenAI Python SDK
- starts with a `system` message
- stores the chat in a list of dictionaries named `conversation`
- uses `role` and `content` fields
- loops through the questions
- appends each assistant reply back into the conversation history
- uses `temperature=0.0`
- limits output to `100` tokens per answer

## Repository structure

```text
paris-travel-guide-repo/
├── app.py
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/OlumideOlumayegun/ai-powered-paris-travel-guide.git
cd ai-powered-paris-travel-guide
```

### 2. Create and activate a virtual environment

**Windows**

```bash
python -m venv .venv
.venv\\Scripts\\activate
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API key

Create a `.env` file or export your API key in your shell.

Example environment variable:

```bash
OPENAI_API_KEY=your_api_key_here
```

## Run the project

```bash
python app.py
```

## How the code works

### OpenAI client

The project creates an `OpenAI()` client so Python can communicate with the API.

### Conversation structure

The chatbot keeps all messages in a list called `conversation`.
Each message is a dictionary with:

- `role`
- `content`

Example:

```python
{"role": "user", "content": "Where is the Arc de Triomphe?"}
```

### System message

The first message tells the assistant how to behave:

```python
{
    "role": "system",
    "content": "You are a helpful Paris travel guide..."
}
```

### Question loop

The app loops through the required Paris questions, sends the accumulated chat history to the model, receives a response, and appends that response back into `conversation`.

### Model settings

The request uses:

- `temperature=0.0` for more consistent answers
- `max_tokens=100` to keep responses short

## Example final conversation structure

```python
[
    {"role": "system", "content": "You are a helpful Paris travel guide..."},
    {"role": "user", "content": "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?"},
    {"role": "assistant", "content": "..."},
    {"role": "user", "content": "Where is the Arc de Triomphe?"},
    {"role": "assistant", "content": "..."},
    {"role": "user", "content": "What are the must-see artworks at the Louvre Museum?"},
    {"role": "assistant", "content": "..."}
]
```

## Notes

- Make sure your OpenAI API key is available as `OPENAI_API_KEY`.
- If your account uses a different available model, you can replace `gpt-4o-mini` in `app.py`.
- Exact wording may vary slightly across runs, but `temperature=0.0` reduces variation.

