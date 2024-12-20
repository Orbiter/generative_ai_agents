import os
import sys
import json
from pathlib import Path

# get the config path
script_dir = os.path.dirname(os.path.abspath(__file__))
archetypes_dir = os.path.abspath(os.path.join(script_dir, "../10_archetypes"))

# import the chat client from a previous lecture (don't do this in the same style)
llm_api_dir = os.path.abspath(os.path.join(script_dir, "../../00_workplace/02_llm_api"))
sys.path.append(llm_api_dir)
from chat_client import ChatClient, default_config_file
from chat_context import ChatContext, default_system_prompt

# load the config.json file
with open(f"{archetypes_dir}/archetypes.json", "r") as json_data:
    archetypes = json.load(json_data)

# create a chat client
chat_client = ChatClient(config_file=default_config_file)
chat_context = ChatContext(system_prompt=default_system_prompt)
group = "FAST"

lists_template = archetypes["lists"]["template"]
lists_prompt = archetypes["lists"]["prompt"].replace("<template>", lists_template)
question = "Name 10 cities in France"

try:
    assistant_reply = chat_client.chat(group = group, chat_context = chat_context, prompt=question + "\n" + lists_prompt)
    
    print(assistant_reply)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)


knowledge_template = archetypes["knowledge"]["template"]
knowledge_prompt = archetypes["knowledge"]["prompt"].replace("<template>", knowledge_template)
question = "Write an travelers description of France and it's capital, Paris."

# Get the assistant's reply
try:
    assistant_reply = chat_client.chat(group = group, chat_context = chat_context, prompt=question + "\n" + knowledge_prompt)
    
    print(assistant_reply)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
