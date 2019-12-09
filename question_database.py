from classes import Question

ques = {"question_serial_number": ["main_subject", "sub_subject", "difficulty_level", "solution", "year",
                                   "semester", "exam_date", "format"]}

""" Need to be checked in the sending if its a Question class"""


def add_question(q: Question):
    ques.update({q.question_serial_number: [q.main_subject, q.sub_subject, q.difficulty_lvl, q.solution, q.year
        , q.semester, q.exam_date, q.question_format]})


def del_question(string: str):
    for key in ques:
        if string == key:
            ques.pop(key)
            break
        else:
            return -1


def update_question():  # todo implement
    pass


q = Question('1', 'math', 'none', '7', 'none', '2019', 'a', 'a', 'pdf')

add_question(q)
