from chat_client import ChatClient, default_config_file
from chat_context import ChatContext, default_system_prompt
from qa_pair import QAPair
import argparse
import sys
import os

def main():
    parser = argparse.ArgumentParser(description="Chat with a local LLM.")
    parser.add_argument("--group", default="FAST", help="Set the model group.")
    parser.add_argument("--system", default="Be a helpful assistant.", help="Set a system prompt.")
    parser.add_argument("--config", help="File name of the configuration JSON file.")
    parser.add_argument("--context", help="File name of a ChatContext stored in a JSON file.")
    args = parser.parse_args()
    group = args.group or "CHAT"
    config_file = args.config or default_config_file
    context_file = args.context or None
    system_prompt = args.system or default_system_prompt
    chat_client = ChatClient(config_file=config_file)
    if context_file:
        if os.path.exists(context_file):
            chat_context = ChatContext.load(context_file, system_prompt)
        else:
            chat_context = ChatContext(system_prompt=system_prompt)
    else:
        chat_context = ChatContext(system_prompt=system_prompt)

    print(context_file)
    print(system_prompt)

    # Read the user prompt from stdin
    prompt = sys.stdin.read().strip()
    if not prompt:
        print("Error: No input provided.", file=sys.stderr)
        sys.exit(-1)

    # Get the assistant's reply
    try:
        assistant_reply = chat_client.chat(group = group, chat_context = chat_context, prompt=prompt)
        # Output the assistant's reply to stdout
        print(assistant_reply)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


    # Save the updated context if a context file is specified
    if context_file:
        new_qa_pair = QAPair(question=prompt, answer=assistant_reply, group=group)
        chat_context.add_qa_pair(new_qa_pair)
        chat_context.save(context_file)

if __name__ == "__main__":
    main()
