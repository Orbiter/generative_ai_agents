from qa_pair import QAPair
import json

default_system_prompt = "You are a helpful assistant."

class ChatContext:
    '''
    Manages a chat dialog consisting of a system prompt and a sequence of QAPairs.
    '''
    def __init__(self, system_prompt: str):
        '''
        Initializes the ChatContext with a system prompt.

        :param system_prompt: The initial system message guiding the assistant's behavior.
        '''
        self.system_prompt = system_prompt or default_system_prompt
        self.qa_pairs = []

    def add_qa_pair(self, qa_pair: QAPair):
        '''
        Adds a QAPair to the conversation history.

        :param qa_pair: An instance of QAPair.
        '''
        self.qa_pairs.append(qa_pair)

    def save(self, filename: str):
        '''
        Saves the chat context to a JSON file.

        :param filename: The path to the output JSON file.
        '''
        list_of_questions = []
        list_of_answers = []
        list_of_groups = []
        for qa_pair in self.qa_pairs:
            list_of_questions.append(qa_pair.question)
            list_of_answers.append(qa_pair.answer)
            list_of_groups.append(qa_pair.group)
        data = {
            's_t': self.system_prompt,
            'q_txt': list_of_questions,
            'a_txt': list_of_answers,
            'g_sxt': list_of_groups
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def load(filename: str, system_prompt = default_system_prompt):
        '''
        Loads the chat context from a JSON file.

        :param filename: The path to the input JSON file.
        :return: A new instance of ChatContext loaded from the file.
        '''
        with open(filename, 'r') as f:
            data = json.load(f)
            current_system_prompt = data.get('system_t', system_prompt)
            if not current_system_prompt or len(current_system_prompt) == 0: current_system_prompt = system_prompt
            new_context = ChatContext(system_prompt=current_system_prompt)
            for question, answer, group in zip(data.get('q_txt', []), data.get('a_txt', []), data.get('g_sxt', [])):
                new_context.qa_pairs.append(QAPair(question=question, answer=answer, group=group))
        return new_context

    def to_messages(self):
        '''
        Converts the entire chat context into a list of message dictionaries compatible with the OpenAI API.

        :return: A list of messages representing the conversation history.
        '''
        messages = [{"role": "system", "content": self.system_prompt}]
        for qa_pair in self.qa_pairs:
            messages.extend(qa_pair.to_messages())
        return messages
