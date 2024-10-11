# Configuration

Here we store all the configuration for the LLM engine and the models we will use. We will roll out a method to name specific classes of LLMs which apply to certain tasks. These tasks are:

- `FAST` Fast classification and simple question answering
- `AUTO` In-place replacements for autocompletion in IDEs
- `CODE` Coding questions and generation of code snippets
- `CHAT` Knowledge and general question answering
- `VAST` Most capable models that serve as teacher models and run in batch mode

By using the configuration we can easily switch between different LLMs. We will also use a custom model for each task.

