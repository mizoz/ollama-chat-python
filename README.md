# Ollama Chat Python

[![PyPI Version](https://img.shields.io/pypi/v/ollama-chat-python?style=flat-square)](https://pypi.org/project/ollama-chat-python/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/ollama-chat-python?style=flat-square)](https://pypi.org/project/ollama-chat-python/)
[![License](https://img.shields.io/pypi/l/ollama-chat-python?style=flat-square)](LICENSE)
[![Python Version](https://img.shields.io/pypi/pyversions/ollama-chat-python?style=flat-square)](https://pypi.org/project/ollama-chat-python/)
[![GitHub Stars](https://img.shields.io/github/stars/mizoz/ollama-chat-python?style=flat-square)](https://github.com/mizoz/ollama-chat-python)

> A Python command-line interface for interacting with Ollama LLMs locally from your terminal.

## Features

- Chat with Ollama models from terminal
- Multiple model support
- Streamed responses for real-time output
- Conversation history
- System prompts
- Easy model switching
- Python API for integration

## Installation

### From PyPI

```bash
pip install ollama-chat-python
```

### From Source

```bash
git clone https://github.com/mizoz/ollama-chat-python.git
cd ollama-chat-python
pip install -e .
```

## Usage

### Prerequisites

- Python 3.8+
- Ollama installed and running locally

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

chat = OllamaChat(model="llama2")
response = chat.chat("Hello, how are you?")
print(response)

# With system prompt
chat = OllamaChat(
    model="llama2",
    system="You are a Python expert"
)
response = chat.chat("How do I use list comprehensions?")
```

## CLI Options

| Option | Description |
|--------|-------------|
| `-m, --model` | Specify the model to use |
| `-s, --system` | Set system prompt |
| `-h, --history` | Enable conversation history |

## Requirements

- Python 3.8+
- Ollama installed and running locally

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Author

**mizoz**
- GitHub: [@mizoz](https://github.com/mizoz)

---

⭐ If you find this project useful, please consider giving it a star on GitHub!
