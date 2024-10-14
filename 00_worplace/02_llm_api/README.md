# README

## Overview

This project provides an educational framework to understand how language models (LLMs) work and what is required to produce an LLM agent. Specifically, we have:

- **Implemented a `QAPair` class**: Represents individual interactions between a user and an assistant.
- **Created a `ChatContext` class**: Manages a conversation, including a system prompt and a sequence of Q&A pairs.
- **Developed a `ChatClient` class**: Interfaces with locally hosted language models using REST APIs, based on configurations specified in a `config.json` file.

This framework is designed to help you learn how to structure conversations for language models and interact with them programmatically.

## Classes Overview

### `QAPair` Class

Represents a single question-answer pair in a conversation.

- **Attributes**:
  - `question` (str): The user's question.
  - `answer` (str): The assistant's response.

- **Methods**:
  - `to_messages()`: Converts the QAPair into a list of message dictionaries compatible with OpenAI's API format.

### `ChatContext` Class

Manages the conversation context, including the system prompt and a list of `QAPair` instances.

- **Attributes**:
  - `system_prompt` (str): A message that sets the behavior or context for the assistant.
  - `qa_pairs` (list): A list of `QAPair` instances representing the conversation history.

- **Methods**:
  - `add_qa_pair(qa_pair)`: Adds a `QAPair` to the conversation history.
  - `to_messages()`: Converts the entire chat context into a list of messages.

### `ChatClient` Class

Handles communication with the local LLM server using RESTful APIs.

- **Attributes**:
  - `models` (list): A list of model configurations loaded from `config.json`.

- **Methods**:
  - `load_config(config_file)`: Loads model configurations from a JSON file.
  - `select_model(model_type)`: Selects a model based on the specified type.
  - `chat(model_type, chat_context)`: Sends the conversation to the selected model and retrieves the assistant's reply.

## Configuration File (`config.json`)

The `config.json` file contains configurations for different models hosted locally. Here's an example structure:

```json
{
    \"models\": [
        {
            \"type\": \"FAST\",
            \"title\": \"Qwen2 0.5b\",
            \"model\": \"qwen2:0.5b-instruct-q8_0\",
            \"provider\": \"ollama\",
            \"apiBase\": \"http://localhost:11434\",
            \"apiKey\": \"_\"
        },
        {
            \"type\": \"AUTO\",
            \"title\": \"Deepseek-Coder V2 16b\",
            \"model\": \"deepseek-coder-v2:16b-lite-instruct-q8_0\",
            \"provider\": \"ollama\",
            \"apiBase\": \"http://localhost:11434\",
            \"apiKey\": \"_\"
        }
        // Add other models as needed
    ]
}
```

- **Fields**:
  - `type`: A label to categorize the model (e.g., \"FAST\", \"AUTO\").
  - `title`: A human-readable name for the model.
  - `model`: The model identifier used by the LLM server.
  - `provider`: The software serving the model (e.g., \"ollama\", \"llama.cpp\").
  - `apiBase`: The base URL of the API endpoint.
  - `apiKey`: API key for authentication (if required).

## Usage Guide

### Creating Q&A Pairs

First, import the `QAPair` class and create instances representing user-assistant interactions.

```python
from qa_pair import QAPair

# Create QAPair instances
qa1 = QAPair(question=\"Hello, who are you?\", answer=\"\")
qa2 = QAPair(question=\"Can you tell me a joke?\", answer=\"\")
```

### Building a Chat Context

Next, create a `ChatContext` instance to manage the conversation.

```python
from chat_context import ChatContext

# Initialize ChatContext with a system prompt
chat_context = ChatContext(system_prompt=\"You are a helpful assistant.\")

# Add QAPairs to the context
chat_context.add_qa_pair(qa1)
chat_context.add_qa_pair(qa2)
```

### Interacting with the Chat Client

Use the `ChatClient` class to send the conversation to the LLM and receive responses.

```python
from chat_client import ChatClient

# Initialize the ChatClient
chat_client = ChatClient(config_file=\"config.json\")

# Choose a model type (e.g., \"CHAT\")
model_type = \"CHAT\"

# Send the chat context to the model and get the assistant's reply
try:
    assistant_reply = chat_client.chat(model_type=model_type, chat_context=chat_context)
    print(\"Assistant:\", assistant_reply)
except Exception as e:
    print(\"Error:\", e)
```

**Note**: Replace `\"CHAT\"` with the appropriate model type defined in your `config.json`.

## Testing the Setup

1. **Ensure LLM Server is Running**:

   - Start your local LLM server (Ollama or llama.cpp).
   - Verify that it's accessible at the `apiBase` URL specified in `config.json`.

2. **Run the Script**:

   - Save your test script (e.g., `test_chat.py`).
   - Execute the script:

     ```bash
     python test_chat.py
     ```

3. **Observe the Output**:

   - The assistant's replies should be printed to the console.
   - If there's an error, the exception message will help diagnose the issue.

## Conclusion

By following this guide, you've learned how to:

- Structure conversations for language models using `QAPair` and `ChatContext`.
- Interface with locally hosted LLMs using the `ChatClient` class.
- Configure and select different models via a `config.json` file.

This framework provides a foundation for developing more advanced LLM agents and understanding the mechanics of language model interactions. Feel free to extend the classes and configurations to suit your educational or development needs.

