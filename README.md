# Ollama Chat Python

A Python command-line interface for interacting with Ollama LLMs locally.

## Features

- Chat with Ollama models from terminal
- Multiple model support
- Streamed responses
- Conversation history
- System prompts
- Easy model switching
- Python API for integration

## Installation

```bash
pip install ollama-chat-python
```

Or clone and install:

```bash
git clone https://github.com/mizoz/ollama-chat-python.git
cd ollama-chat-python
pip install -e .
```

## Usage

### Command Line

```bash
# Start chat session
ollama-chat

# Chat with specific model
ollama-chat --model llama2

# With system prompt
ollama-chat --system "You are a helpful coding assistant"
```

### Python API

```python
from ollama_chat import OllamaChat

chat = OllamaChat(model='llama2')
response = chat.chat("Hello, how are you?")
print(response)

# With system prompt
chat = OllamaChat(
    model='llama2',
    system="You are a Python expert"
)
response = chat.chat("How do I use list comprehensions?")
```

## Options

- `-m, --model` - Specify the model to use
- `-s, --system` - Set system prompt
- `-h, --history` - Enable conversation history

## Requirements

- Python 3.8+
- Ollama installed and running locally

## License

MIT License

## Author

mizoz
