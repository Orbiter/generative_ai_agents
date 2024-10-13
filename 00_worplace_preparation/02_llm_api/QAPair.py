class QAPair:
    """
    Represents a single Query-Answer pair in a conversation.
    """
    def __init__(self, question: str, answer: str, group: str):
        """
        Initializes a QAPair with a question and an answer.

        :param question: The user's query.
        :param answer: The assistant's response.
        :param group: The category or tag for this QAPair.
        """
        self.question = question
        self.answer = answer
        self.group = group or ""

    def to_messages(self):
        """
        Converts the QAPair into a list of message dictionaries.

        :return: A list containing the user and assistant messages.
        """
        return [
            {"role": "user", "content": self.question},
            {"role": "assistant", "content": self.answer}
        ]
