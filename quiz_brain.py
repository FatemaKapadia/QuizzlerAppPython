from question_model import Question


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        self.current_answer = "False"

    def next_question(self):
        try:
            self.current_question = self.question_list[self.question_number][0]
            self.current_answer = self.question_list[self.question_number][1]
            self.question_number += 1
            return f"Q{self.question_number}. {self.current_question}"

        except IndexError:
            return None

    def check_answer(self, user_answer):
        if user_answer.lower() == self.current_answer.lower():
            self.score += 1
            return True
        else:
            return False
