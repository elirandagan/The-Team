import json
from question_database import ques


def save_ques_db_file(questions: dict):
    with open("user_db_file.txt", 'w') as file:
        json.dump(questions, file, indent=2)


def load_ques_db_file(questions: dict):
    with open("user_db_file.txt", 'r') as file:
        questions = json.load(file)
