class Question:
    def __init__(self, question_serial_number='', main_subject='', sub_subject='', difficulty_lvl='', solution='',
                 year=''
                 , semester='', exam_date='', question_format=''):
        self.question_serial_number = question_serial_number
        self.difficulty_lvl = difficulty_lvl
        self.solution = solution
        self.year = year
        self.question_format = question_format
        self.main_subject = main_subject
        self.sub_subject = sub_subject
        self.semester = semester
        self.exam_date = exam_date


    def set_main_subject(self,main_subject):
        self.main_subject = main_subject

    def get_main_subject():
        return self.main_subject

    def set_question_serial_number(self,serialNumber):
        self.question_serial_number = serialNumber

    def get_question_serial_number():
        return self.question_serial_number

    def get_difficulty_lvl(self):
        return self.difficulty_lvl

    def set_difficulty_lvl(self, diff):
        self.difficulty_lvl = diff

    def get_solution(self):
        return self.solution

    def set_solution(self, solution_type):
        self.solution = solution_type

    def get_semester(self):
        return self.semester

    def set_semester(self, question_semester):
        self.semester = question_semester

    def get_year(self):
        return self.year

    def set_year(self, question_year):
        self.year = question_year

    def get_exam_date(self):
        return self.exam_date

    def set_exam_date(self, question_exam_date):
        self.exam_date = question_exam_date

    def get_question_format(self):
        return self.question_format

    def set_question_format(self, question__format):
        self.question_format = question__format

    def get_sub_subject(self):
        return self.sub_subject

    def set_sub_subject(self, question_subtopic):
        self.sub_subject = question_subtopic


class Clause:
    def __init__(self, clause_number='', clause_subject='', clause_difficulty=''):
        self.clause_number = clause_number
        self.clause_subject = clause_subject
        self.clause_difficulty = clause_difficulty

    def set_clause_number(self, number):
        self.clause_number = number

    def get_clause_number(self):
        return self.clause_number

    def set_clause_subject(self, sub):
        self.clause_subject = sub

    def get_clause_subject(self):
        return self.clause_subject

    def set_clause_difficulty(self, dif):
        self.clause_difficulty = dif

    def get_clause_difficulty(self):
        return self.clause_difficulty


class Lecturer:
    def __init__(self, name='', phone_number='', topic='', password=''):
        self.name = name
        self.phone_number = phone_number
        self.topic = topic
        self.password = password

    def get_name(self):
        return self.name

    def set_name(self, professor_name):
        self.name = professor_name

    def get_phone(self):
        return self.phone_number

    def set_phone(self, professor_phone):
        self.phone_number = professor_phone

    def get_topic(self):
        return self.topic

    def set_topic(self, professor_topic):
        self.topic = professor_topic

    def get_password(self):
        return self.password

    def set_password(self, professor_password):
        self.password = professor_password


class Student:
    def __init__(self, name='', password=''):
        self.name = name
        self.password = password

    def get_name(self):
        return self.name

    def set_name(self, student_name):
        self.name = student_name

    def get_password(self):
        return self.password

    def set_password(self, student_password):
        self.password = student_password


class Coordinator:
    def __init__(self, coordinator_name='', phone_number='', password=''):
        self.coordinator_name = coordinator_name
        self.phone_number = phone_number
        self.password = password

    def get_coordinator_name(self):
        return self.coordinator_name

    def set_coordinator_name(self, name):
        self.coordinator_name = name

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, coordinator_phone_number):
        self.phone_number = coordinator_phone_number

    def get_password(self):
        return self.password

    def set_password(self, coordinator_password):
        self.password = coordinator_password
