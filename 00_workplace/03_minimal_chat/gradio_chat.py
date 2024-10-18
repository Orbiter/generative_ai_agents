import os
import sys
import queue
import threading
import gradio as gr
from gradio import ChatMessage

# get the config path
script_dir = os.path.dirname(os.path.abspath(__file__))

# import the chat client from a previous lecture (don't do this in the same style)
llm_api_dir = os.path.abspath(os.path.join(script_dir, "../02_llm_api"))
sys.path.append(llm_api_dir)

from chat_client import ChatClient, default_config_file
from chat_context import ChatContext, default_system_prompt

# initialize a chat client
chat_client = ChatClient(config_file=default_config_file)
chat_context = ChatContext(system_prompt=default_system_prompt)

def chatstream(message, history):
    r = ""
    history = history or []
    # Ensure all messages are dictionaries
    history.append({"role": "user", "content": message})

    token_queue = queue.Queue()
    stop_event = threading.Event()

    def streamresponder(token):
        token_queue.put(token)

    def run_chatstream():
        chat_client.chatstream(
            group="CHAT",
            chat_context=chat_context,
            prompt=message,
            callback=streamresponder
        )
        stop_event.set()

    threading.Thread(target=run_chatstream).start()

    while not stop_event.is_set() or not token_queue.empty():
        try:
            token = token_queue.get(timeout=0.1)
            r += token
            partial_history = history + [{"role": "assistant", "content": r}]
            yield {"role": "assistant", "content": r}
            #yield partial_history
        except queue.Empty:
            continue

    # Append the final response
    history.append({"role": "assistant", "content": r})
    yield history

# Launch Gradio with the updated chat function
gr.ChatInterface(chatstream, type="messages").launch()