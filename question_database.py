from classes import Question

ques = {"question_serial_number": ["main_subject", "sub_subject", "difficulty_level", "solution", "year",
                                   "semester", "exam_date", "format"]}

""" Need to be checked in the sending if its a Question class"""


def add_question(q: Question):
    ques.update({q.question_serial_number: [q.main_subject, q.sub_subject, q.difficulty, q.solution, q.year,
                                            q.question_format]})


def del_question(string: str):
    for key in ques:
        if string == key:
            ques.pop(key)
            break
        else:
            return -1


def update_question():  # todo implement
    pass
