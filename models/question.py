
class Question:
    def __init__(self, question: str, answer: str) -> None:
        self.question = question
        self.answer = answer

    def get_question(self) -> str:
        return self.question

    def get_answer(self) -> str:
        return self.answer

    def set_answer(self, answer) -> bool:
        self.answer = answer
        return True

    @staticmethod
    def create_from_json(json_info):
        '''
        Create a question instance based on json input
        '''
        question = json_info["question"]
        answer = json_info["answer"]
        return Question(question, answer)
