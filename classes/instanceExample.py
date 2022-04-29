class Student:
    def __init__(self, n='', m=0):
        self.name = n
        self.marks = m

    def display(self):
        print('Hi', self.name)
        print('Your Marks ', self.marks)

    def calculate_grade(self):
        if self.marks > 600:
            print('You got first grade')
        elif self.marks >= 500:
            print('You god B grade')
        elif self.marks >= 400:
            print('You got third grade')
        else:
            print('You got failed')


if __name__ == '__main__':
    n = int(input('Enter Name'))
    i = 0

    while i < n:
        name = input('Enter the name')
        marks = int(input('Enter the marks'))

        s = Student(name, marks)
        s.display()
        s.calculate_grade()
        i += 1
        print("_________________________")
