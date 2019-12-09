from time import sleep
from user_database import user_list
from question_database import ques, add_question
from user_db_file import save_user_db_file, load_user_db_file
from questions_db_file import save_ques_db_file, load_ques_db_file
from classes import Question

user_menu = {'1': "LOGIN", '2': "EXIT"}
student_menu = {'1': "EXIT", '2': "CHOOSE A QUESTION", '3': "SHOW A QUESTIONS", '4': "FILTER A QUESTION",
                '5': "SEARCH A QUESTION"}
lecturer_menu = dict()
lecturer_menu.update({'6': "CREATE A TEST"})
lecturer_menu.update(student_menu.copy())

coordinator_menu = dict()
coordinator_menu.update({'7': "ADD TEACHER", '8': "REMOVE A TEACHER", '9': "UPDATE A TEACHER",
                         '10': "ADD A QUESTION", '11': "ADD AN ANSWER",
                         '12': "DELETE A QUESTION", '13': "UPDATE A QUESTION", '14': "DEFINE QUESTION INFO", })
coordinator_menu.update(lecturer_menu.copy())


def clear():
    print('\n' * 10)


def to_exit():
    save_ques_db_file(ques)
    save_user_db_file(user_list)
    print("\t***  BYE BYE !  ***")
    exit(0)


def load_dbs():
    load_ques_db_file()
    load_user_db_file()


def get_key(state: dict):
    while True:
        _key = input()
        if _key not in state.keys():
            print("\t***  Sorry... can't help you with that key:(\n\tPlease try again ***")
        else:
            return _key


def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    clear()

    print("\t**********************************************")
    print("\t***  WELCOME TO QUESTION'S DATA BASE  ***")
    print("\t**********************************************\n")


def display_user_title_bar(user: tuple):
    # Clears the terminal screen, and displays a title bar.
    clear()
    _name, _, user_type = user
    print("\t**********************************************")
    print("\t***  HELLO {0} - {1}   ***".format(_name, user_type))
    print("\t**********************************************\n")


def first_menu_display_title_bar():
    print("\t***  PRESS 1 FOR LOG-IN  ***")
    print("\t***  PRESS 2 FOR EXIT  ***")


def first_menu(_key):
    if _key == '1':
        return
    elif _key == '2':
        to_exit()
    else:
        print('UNWANTED VALUE REACHED IN MAIN MENU  - KEY =  {}'.format(_key))
        _key = get_key(user_menu)
        first_menu(_key)


def is_access_granted(user_pass: str):
    print("\t***  Enter user passwords :   ***")
    _pass = input()
    if user_pass == _pass:
        return True
    return False


def login():
    def is_login_name():
        nonlocal user
        print("\t***  Enter user name  or enter return :  ***")
        user_name = input()
        if user_name.lower() == "return":
            main()
        for student in user_list["Student"]:
            _name, _pass = student
            if _name == user_name:
                user = user_name, _pass, "Student"
                return True

        for lecturer in user_list["Lecturer"]:
            _name, _, _, _pass = lecturer
            if _name == user_name:
                user = user_name, _pass, "Lecturer"
                return True

        for coor in user_list["Coordinator"]:
            _name, _, _pass = coor
            if _name == user_name:
                user = user_name, _pass, "Coordinator"
                return True

        return False

    while True:
        clear()
        user = tuple()
        print("\t***  LOGIN ***")
        if is_login_name():
            if is_access_granted(user[1]):
                return user
            print("\t***  Invalid password, try again   ***")
            sleep(1)
            continue
        print("\t***    sorry... user not found     ***")
        sleep(1)


def display_student_menu():
    for pair in student_menu.items():
        dict_key, option = pair
        print("\t***  TO {0}  - PRESS {1} ".format(option, dict_key))
    key = get_key(student_menu)
    if key == '1':
        to_exit()
    elif key == '2':

        print("\t   you chose a question    *** ")
        sleep(2)
        clear()
    elif key == '3':
        print("\t  question has shown    *** ")
        sleep(2)
        clear()
    elif key == '4':
        print("\t   question has filtered    *** ")
        sleep(2)
        clear()
    elif key == '5':
        print("\t   you searched a question    *** ")
        sleep(2)
        clear()
    else:
        print("INVALID KEY POPPED")
        exit(-1)
    display_student_menu()


def display_lecturer_menu():
    for pair in lecturer_menu.items():
        dict_key, option = pair
        print("\t***  TO {0}  - PRESS {1} ".format(option, dict_key))
    key = get_key(lecturer_menu)
    print(key)
    if key == '1':
        to_exit()
    elif key == '2':
        print("\t   you chose a question    *** ")
        sleep(2)
        clear()
    elif key == '3':
        print("\t  question has shown    *** ")
        sleep(2)
        clear()
    elif key == '4':
        print("\t   question has filtered    *** ")
        sleep(2)
        clear()
    elif key == '5':
        print("\t   you searched a question    *** ")
        sleep(2)
        clear()
    elif key == '6':
        print("\t   a test has created    *** ")
        sleep(2)
        clear()
    else:
        print("INVALID KEY POPPED")
        exit(-1)
    display_lecturer_menu()


def display_coordinator_menu():
    for pair in coordinator_menu.items():
        dict_key, option = pair
        print("\t***  TO {0}  - PRESS {1} ".format(option, dict_key))
    key = get_key(coordinator_menu)
    print(key)

    if key == '1':
        to_exit()
    elif key == '2':
        print("\t   you chose a question    *** ")
        sleep(2)
        clear()
    elif key == '3':
        print("\t  question has shown    *** ")
        sleep(2)
        clear()
    elif key == '4':
        print("\t   question has filtered    *** ")
        sleep(2)
        clear()
    elif key == '5':
        print("\t   you searched a question    *** ")
        sleep(2)
        clear()
    elif key == '6':
        print("\t   a test has created    *** ")
        sleep(2)
        clear()
    elif key == '7':
        print("\t   a teacher was added    *** ")
        sleep(2)
        clear()
    elif key == '8':
        print("\t   a teacher was removed    *** ")
        sleep(2)
        clear()
    elif key == '9':
        print("\t   a teacher was updated    *** ")
        sleep(2)
        clear()
    elif key == '10':
        creat_question()
        print("\t   a question was added    *** ")
        sleep(2)
        clear()
    elif key == '11':
        print("\t   an answer was added    *** ")
        sleep(2)
        clear()
    elif key == '12':
        print("\t   you deleted a question    *** ")
        sleep(2)
        clear()
    elif key == '13':
        print("\t   you updated a question    *** ")
        sleep(2)
        clear()
    elif key == '14':
        print("\t   question's info was updated    *** ")
        sleep(2)
        clear()
    else:
        print("INVALID KEY POPPED")
        exit(-1)
    display_coordinator_menu()


def creat_question():

    q = Question()
    print("please enter the serial number of the question")
    q.set_question_serial_number(input())
    print("please enter the main subject of the question")
    q.set_main_subject(input())
    print("please enter the sub subject of the question")
    q.set_sub_subject(input())
    print("please enter the difficulty level of the question")
    q.set_difficulty_lvl(input())
    print("please enter the solution of the question")
    q.set_solution(input())
    print("please enter the year of the question")
    q.set_year(input())
    print("please enter the semester of the question")
    q.set_semester(input())
    print("please enter the exam date of the question")
    q.set_exam_date(input())
    print("please enter the question format of the question")
    q.set_question_format(input())

    add_question(q)

def main():
    load_dbs()
    display_title_bar()
    first_menu_display_title_bar()
    key = get_key(user_menu)
    first_menu(key)
    user = login()
    display_user_title_bar(user)
    if user[2] == "Student":
        display_student_menu()

    if user[2] == "Lecturer":
        display_lecturer_menu()

    if user[2] == "Coordinator":
        display_coordinator_menu()


if __name__ == '__main__':
    main()
