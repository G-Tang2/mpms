
class Question:
    def __init__(self, question: str, answer: str) -> None:
        self.question = question
        self.answer = answer

    def get_question(self):
        return self.question

    def get_answer(self):
        return self.answer

    def set_answer(self, answer):
        self.answer = answer

    @staticmethod
    def create_from_json(json_info):
        question = json_info["question"]
        answer = json_info["answer"]
        return Question(question, answer)
