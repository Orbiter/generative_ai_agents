import os
import json
from pathlib import Path

# get the path of the current directory
script_dir = Path(__file__).resolve().parent
config_dir = script_dir.parent / "00_config"

# load the config.json file
with open(f"{config_dir}/config.json", "r") as json_data:
    config = json.load(json_data)

# iterate over the objects in the list of the models in the config file
groups = []
for model in config['models']:
    # skip the model if it is not Ollama
    if model['provider'] != 'ollama': continue

    # skip the model if the group was already processed
    group = model['group']
    if group in groups: continue
    groups.append(group)
    
    # extract host and port from apiBase to be able to set OLLAMA_HOST
    # to be able to also pull models on remote ollama servers
    apiBase = model['apiBase']
    parts = apiBase.split('://')
    protocol, remainder = parts[0], parts[1] if len(parts) > 1 else ''
    host_and_port, path = ('/' in remainder and remainder.rsplit('/', 1)) or (remainder, '')
    host, port = host_and_port.split(':')[-2:]
    if not ':' in host_and_port:
        port = protocol == 'http' and '80' or '443'
    
    # call ollama pull to download the model
    modelname = model['model']
    os.environ['OLLAMA_HOST'] = host + ':' + port
    os.system('ollama pull '+ modelname)

# write the list of llms from ollama
os.system('ollama list')
