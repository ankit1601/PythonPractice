class A:
    def __init__(self):
        print("class a constructor")

    def method(self):
        print("class a method")


class B:
    def __init__(self):
        print("class b constructor")

    def method(self):
        print("class b method")


class C(A, B):
    def __init__(self):
        print('class C Constructor')


if __name__ == '__main__':
    c = C()
    c.method()
    print(C.mro())

