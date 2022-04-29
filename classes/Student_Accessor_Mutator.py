class Student:

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMarks(self, marks):
        self.marks = marks

    def getMarks(self):
        return self.marks

    @classmethod
    def set_gender(cls, gender):
        cls.gender = gender

    def getGender(self):
        return self.gender


n = int(input('How many students? '))

i = 0

while i < n:
    s = Student()
    name = input('Enter name')
    s.setName(name)
    marks = int(input('Enter marks'))
    s.setMarks(marks)
    s.set_gender('Male')
    s2 = Student()
    print("s2", s2.getGender())
    print(s2.set_gender("Female"))

    print('Hi', s.getName())
    print('Your Marks', s.getMarks())
    print('Your Gender', s.getGender())

    i += 1
    print('----------------------------')
