class One:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.b

    def __lt__(self, object2):
        return self.a < object2.b

    def __gt__(self, object2):
        return self.a > object2.b

    def __le__(self, object2):
        return self.a <= object2.b

    def __ge__(self, object2):
        return self.a >= object2.b

    def __eq__(self, object2):
        return self.a == object2.b

    def __ne__(self, object2):
        return self.a != object2.b


class Two:
    def __init__(self, b):
        self.b = b

    def __add__(self, other):
        return self.b + other.a


ob1 = One(10)
ob2 = Two(20)

obj = ob1 + ob2
print(obj)
print(ob2 > ob1)


class A:
    def __init__(self, item):
        self.item = item

    def __getitem__(self, item):
        return self.item[item]

    def __setitem__(self, index, item1):
        self.item[index] = item1

    def __str__(self):
        return str(self.item)

    def __repr__(self):
        return str(self.__class__)

    def __len__(self):
        return len(self.item)

    def __contains__(self, item):
        return item in self.item

    def __call__(self, b):
        return self.item * b


obj = A([1, 2, 3])

print(f'{obj[0]}')
print(obj[1])  # get function will be invoked here
print(obj[2])

obj[2] = 4  # set item function will be invoked here
print(obj)
print(obj)
print(len(obj))  # len function will be invoked
print(5 in obj)  # contains function will be invoked
print(obj(4))  # invoke call methed object become callable here
# print(repr(dict))


class PrimeNumber:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        for value in range(self.start, self.stop+1):
            if value < 1:
                continue
            if value == 2:
                yield 2

            for i in range(2, value):
                if value % i == 0:
                    break
                if i == value-1:
                    yield value


prime_number = iter(PrimeNumber(0, 42))

for j in prime_number:
    print(j)


class FibonacciGenerator:
    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        a = b = 1
        for index in range(self.stop):
            yield a
            a, b = b, a+b


fibonacci = FibonacciGenerator(10)
for fib in fibonacci:
    print(fib)

fib_list = []
a = b = 1
for i in range(10):
    print(a)
    a, b = b, a+b

zip




