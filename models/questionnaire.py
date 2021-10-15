
from typing import List
from models.question import Question
import csv


class Questionnaire:
    def __init__(self, questions: List[Question]) -> None:
        self.questions = questions

    def get_question_list(self) -> List[Question]:
        return self.questions

    @staticmethod
    def create_from_csv():
        '''
        Create a GP instance based on csv file
        '''
        question_list = []

        with open("./app_data/question.csv", "r", encoding='utf-8-sig') as f:
            f_reader = csv.DictReader(f)
            for question_info in f_reader:
                question_list.append(Question.create_from_json(question_info))

        return Questionnaire(question_list)

    @staticmethod
    def create_from_json(json_info):
        '''
        Create a GP instance based on json input
        '''
        questionnaire = []
        for question_json in json_info["questions"]:
            questionnaire.append(Question.create_from_json(question_json))
        return Questionnaire(questionnaire)