import json
from question_database import ques


def save_ques_db_file(ques):
    with open("ques_db_file.txt", 'w') as file:
        json.dump(ques, file, indent=2)


def load_ques_db_file():
    with open("ques_db_file.txt", 'r') as file:
        ques = json.load(file)


