import os
import json
import urllib3
import requests
from typing import Optional

class_dir = os.path.dirname(os.path.abspath(__file__))
default_config_file = os.path.abspath(os.path.join(class_dir, "../00_config/config.json"))

class ChatClient:
    """
    Implements a chat client that communicates with locally hosted LLMs
    using configurations specified in 'config.json'.
    """
    def __init__(self, config_file: str = default_config_file):
        """
        Initializes the ChatClient by loading the configuration file.

        :param config_file: Path to the JSON configuration file.
        """
        self.models = self.load_config(config_file)

    def load_config(self, config_file: str):
        """
        Loads the configuration from the given JSON file.

        :param config_file: Path to the JSON configuration file.
        :return: A list of model configurations.
        """
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
            return config.get('models', [])
        except FileNotFoundError:
            raise Exception(f"Configuration file '{config_file}' not found.")
        except json.JSONDecodeError:
            raise Exception(f"Error decoding JSON from '{config_file}'.")

    def select_model(self, group: str) -> Optional[dict]:
        """
        Selects a model from the configuration based on the given group.

        :param group: The group of model to select (e.g., 'FAST', 'AUTO').
        :return: The selected model configuration or None if not found.
        """
        for model in self.models:
            if model.get('group') == group:
                return model
        return None

    def chat(self, group: str, chat_context, prompt: str) -> str:
        """
        Sends the chat context to the selected model's API endpoint
        and returns the assistant's reply.

        :param group: The group of model to use for the chat.
        :param chat_context: An instance of ChatContext containing the conversation.
        :param prompt: The prompt for the assistant.
        :return: The assistant's reply as a string.
        """
        # Select the model based on the given group
        model_config = self.select_model(group)
        if not model_config:
            raise Exception(f"No model found for group '{group}'.")
        
        # Prepare the request payload
        context = chat_context.to_messages()
        context = context + [{"role": "user", "content": prompt}]
        payload = {
            "model": model_config.get('model'),
            "temperature": 0.0,
            "max_tokens": 300,
            "messages": context,
            "stream": False
        }

        # Prepare headers (if needed, e.g., for API key authentication)
        headers = {
            "Content-Type": "application/json",
        }
        api_key = model_config.get('apiKey')
        if api_key and api_key != "_":
            headers["Authorization"] = f"Bearer {api_key}"

        # Prepare the API endpoint URL
        api_base = model_config.get('apiBase')
        endpoint = f"{api_base}/v1/chat/completions"

        # Disable SSL warnings
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        # Send the request to the API endpoint with SSL verification disabled
        try:
            response = requests.post(endpoint, headers=headers, json=payload, verify=False)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            # get the error message from the response
            if response:
                try:
                    data = response.json()
                    message = data.get('message', {})
                    content = message.get('content', '')
                    raise Exception(f"API request failed: {content}")
                except json.JSONDecodeError:
                    raise Exception(f"API request failed: {e}")

        # Parse the response
        try:
            data = response.json()
            choices = data.get('choices', [])
            if len(choices) == 0: raise Exception("No response from the API.")
            message = choices[0].get('message', [])
            content = message.get('content', '')
            return content
        except json.JSONDecodeError:
            raise Exception("Failed to parse JSON response from the API.")

        return ""

