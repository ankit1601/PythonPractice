class Person:
    def __init__(self, name, dob):
        self.name = name
        self.db = self.Dob(dob)

    def display(self):
        print(" Name= ", self.name)

    class Dob:
        def __init__(self, dob):
            self.dob = dob

        def display(self):
            print("DOB", self.dob)


if __name__ == '__main__':
    p = Person('Ankit', "16-01-1993")
    p.display()
    p.db.display()