import json
from question_database import ques


def save_ques_db_file(ques):
    with open("ques_db_file.txt", 'w') as file:
        json.dump(ques, file, indent=2)


def load_ques_db_file():
    with open("ques_db_file.txt", 'r') as file:
        ques = json.load(file)


<<<<<<< HEAD
save_ques_db_file()
=======
>>>>>>> 25d4b561d60831f77c458a97a5db029999000191
