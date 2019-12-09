import json
from user_database import user_list


def save_user_db_file(users: dict):
    with open("user_db_file.txt", 'w') as file:
        json.dump(users, file, indent=2)


def load_user_db_file(users: dict):
    with open("user_db_file.txt", 'r') as file:
        users = json.load(file)
