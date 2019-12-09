from users import Student, Lecturer, Coordinator

user_list = {"Student": [("full name", "password")],
             "Lecturer": [["full name", "phone number", "profession", "password"]],
             "Coordinator": [["full name", "phone number", "password"]]}

"Database of questions using dictionary"


def add_user(obj: Student or Lecturer or Coordinator):
    if type(obj) == Student:
        user_list["Student"].append((obj.getName(), obj.getPassword()))
    elif type(obj) == Lecturer:
        user_list.update({"Lecturer": [obj.name, obj.phoneNumber, obj.profession, obj.password]})
    else:
        user_list.update({"Coordinator": [obj.name, obj.phoneNumber, obj.password]})


def del_user(string: str):
    for lec in user_list["Lecturer"]:
        if lec == user_list["Lecturer"][0]:
            user_list["Lecturer"].pop(0)


stu = Student("eliran", "123")
add_user(stu)
print(user_list["Student"])
del_user("full name")
print(user_list["Lecturer"])
