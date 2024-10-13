# Set-Up of a Local LLM Environment

There are two options available to run the LLM locally:
- llama.cpp, a C++ implementation for quantized models running inference on CPU
- using ollama, a server framework for many llama.cpp instances

While the first option is the lightest option, the second one is much easier to install
and also more flexible solution. We recommend to use the second option unless you want
to run a LLM model which is not available for ollama.

## Set-Up of ollama

Go to https://ollama.com/ and download the latest version of ollama.
Follow the instructions on the website for your system.

As soon as you are finished with the installation, you can test it by running the following command:
```bash
ollama run qwen2:0.5b-instruct-q8_0
```

This will download the smallest model available and run it on your local machine.
The download requires 0.5 GB of disk space and will take only a few minutes (depending on your internet connection).

The chat can be stopped by pressing `Ctrl+D`.

## Set-Up of llama.cpp

This requires several steps:
- clone the repository
- compile the code
- download the model
- run the model

To do so, you need a complete c++ development environment with cmake and git installed.
We recommend to use a Linux system, but it should also work on MacOS and Windows.

### Installation of the C++ Development Environment

#### Linux

```bash
sudo apt-get update
sudo apt-get install build-essential cmake git
```

#### MacOS

```bash
brew install cmake git
```

#### Windows

Download and install the following software:
- Visual Studio 2019 (https://visualstudio.microsoft.com/)
- CMake (https://cmake.org/)
- Git (https://git-scm.com/)
- Python (https://www.python.org/)

### Clone the Repository

```bash
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
```

### Compile the Code

This will take some time.

```bash
make
```

Because the llama.cpp code is updated on a daily basis, it is recommended to update the code regularly.
You can do this with

```bash
git pull
make
```

### Download the Model

This will download the model into the `models` directory.

```bash
wget --no-check-certificate -P models https://huggingface.co/Qwen/Qwen2-0.5B-Instruct-GGUF/resolve/main/qwen2-0_5b-instruct-q8_0.gguf
```

### Run the Model as llama.cpp Server

```bash
./llama-server --model models/qwen2-0_5b-instruct-q8_0.gguf
```

You must keep the window open to keep the server running.

You can also run the server in the background by running it with
    
```bash
nohup ./llama-server --model models/qwen2-0_5b-instruct-q8_0.gguf &
```

If the server is running in the background, you can stop it with `killall llama-server`.

### Use the Model with it's build-in Web Interface

llama.cpp comes with a build-in web interface which can be accessed by opening a browser and navigating to `http://localhost:8080`.
This allows you to interact with the model in a more user-friendly way. You can also set a lot of parameters for the model.

## Download all Models configured in config.json

There are a list of models in the `config.json` file. You can download ollama models with the following command:

```bash
python3 load_ollama_models.py
```

## Find more models for ollama or llama.cpp

New models are frequently added on huggingface.co. Ollama has a curated list of models which should be compatible with llama.cpp
and publishes them on https://ollama.com/models. You are encouraged to check this website for new models and add them to the `config.json` file yourself.

Huggingface as a much larger list of models available. You can find them on https://huggingface.co/models, but those models are not only
chat/instruct models but also other types of models. Furthermode, we need quantized versions of the models to run them with llama.cpp.
The following process to discover them is recommended:
- Select a model of right kind (instruct), size (for your hardware) and target (math, coding, role-play etc.) from the open-llm leaderboard: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard
- Click on the model to get to the model page. This will provide you with the model binaries at "Files and Versions" tab, however these
  are not quantized. You must copy the model name and then search in the model search field for the model name and the string "gguf".
- If you found a gguf-version of the model, go to the "Files and Versions" tab and select the quantization level you want to use.
  The most usable quantization levels are q8_0 (best quality if you have enough memory) and q4_K_M (best option if you want to save as much memory as possible).

If you find the model you want to use, select it either in ollama and download it with the `ollama run` command or for llama.cpp download it with the `wget` command as shown above.

## Automatically download all ollama models defined in configuration file

You can run the following script to automatically download all Ollama models listed in your configuration file:

```bash
./load_ollama_models.sh
```