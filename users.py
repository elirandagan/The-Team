class Student:
    def __init__(self, name='', password=''):
        self.password = password
        self.name = name

    def setPassword(self, password):
        self.password = password

    def getPassword(self):
        return self.password

    def getName(self):
        return self.name

    def setName(self, studentName):
        self.name = studentName


class Lecturer:
    def __init__(self, name='', phoneNumber='', profession='', password=''):
        self.name = name
        self.phoneNumber = phoneNumber
        self.profession = profession
        self.password = password

    def getName(self):
        return self.name

    def setName(self, lecturerName):
        self.name = lecturerName

    def getPhoneNumber(self):
        return self.phoneNumber

    def setPhoneNumber(self, phone):
        self.phoneNumber = phone

    def getProfession(self):
        return self.profession

    def setProfession(self, profession):
        self.profession = profession

    def setPassword(self, password):
        self.password = password


class Coordinator:
    def __init__(self, name='', phoneNumber='', password=''):
        self.name = name
        self.phoneNumber = phoneNumber
        self.password = password

    def getName(self):
        return self.name

    def setName(self, coordinatorName):
        self.name = coordinatorName

    def getPhoneNumber(self):
        return self.phoneNumber

    def setPhoneNumber(self, phone):
        self.phoneNumber = phone

    def setPassword(self, password):
        self.password = password



