from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import UI


question_bank = [(i["question"], i["correct_answer"]) for i in question_data]
quiz = QuizBrain(question_bank)
quiz_window = UI(quiz)
