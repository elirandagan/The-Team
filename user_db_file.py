import json
from user_database import user_list


def save_user_db_file():
    with open("user_db_file.txt", 'w') as file:
        json.dump(user_list, file, indent=2)


def load_user_db_file():
    with open("user_db_file.txt", 'r') as file:
        user_list = json.load(file)
