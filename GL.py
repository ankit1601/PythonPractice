a = [[1, 2, 3, [4, 5, 6]], [2, 3, 4]]
out = [1, 2, 3, 2, 3, 4]


def flatten(b):
    for i in b:
        if type(i) == list:
            flatten(i)
        else:
            flatten_list.append(i)


flatten_list = []

flatten(a)
print(flatten_list)
#
# test = [1, 0, 1, 1, 1, 0, 0, 0, 1, 0]
# res = []


# Research Project


def check_type(type_):
    def wrapper(func):
        def inner(a_):
            res_ = func(a_)
            if type(res_) == type_:
                return res_
            else:
                raise TypeError("Incorrect Type")

        return inner

    return wrapper


@check_type(list)
def add(a):
    return a


try:
    print(add([1, 2, 3]))
except (TypeError, ArithmeticError) as err:
    print(err)
finally:
    print("End Function")


# Employee
# Salary

# obj1 = a
# obj2 = b

class Employee:
    def __init__(self, s):
        self.salary = s

    def __add__(self, other):
        return self.salary + other.salary


obj1 = Employee(10)
obj2 = Employee(20)

print(obj1+obj2)


# multiple #

# A
# B(A)
# C(B)


a = [1, 2, 3, 4, 5, 6]
sum_ = 0
for i in a:
    sum_ += i

print(sum_)

# a = 0
# print(id(a))
# b = 0
# print(id(b))
#
# a = 10
# print(id(a))
#
# c = [1, 2, 3]
# print(id(c))
# d = c
# print(id(d))

