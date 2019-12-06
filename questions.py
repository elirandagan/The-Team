class Questions:
    def __init__(self, question_serial_number, main_subject, sub_subject, difficulty_lvl, solution, year, semester,
                 exam_date, format_q):
        self.question_serial_number = question_serial_number
        self.main_subject = main_subject
        self.sub_subject = sub_subject
        self.difficulty_lvl = difficulty_lvl
        self.solution = solution
        self.year = year
        self.semester = semester
        self.exam_date = exam_date
        self.format_q = format_q

    def get_question_serial_number(self):
        return self.question_serial_number

    def set_question_serial_number(self, number):
        self.question_serial_number = number

    def get_main_subject(self):
        return self.main_subject

    def set_main_subject(self, subject):
        self.main_subject = subject

    def get_difficulty_lvl(self):
        return self.difficulty_lvl

    def set_difficulty_lvl(self, difficulty):
        self.difficulty_lvl = difficulty

    def get_solution(self):
        return self.solution

    def set_solution(self, solution):
        self.solution = solution

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_semester(self):
        return self.semester

    def set_semester(self, semester):
        self.semester = semester

    def set_exam_date(self, date):
        self.self.exam_date = date

    def get_format_q(self):
        return self.format_q

    def set_format_q(self, format):
        self.format_q = format


q = Questions("question_serial_number", 'main_subject','sub_subject', '5', 'solution', 'year', 'semester', 'exam_date',
              'format_q')

print(q.format_q)
