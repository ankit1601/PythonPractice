from abc import  ABC, abstractmethod


class A(ABC):
    def method(self):
        raise NotImplementedError


class B(A):
    def method(self):
        pass


class C(B):
    def method2(self):
        pass


if __name__ == '__main__':
    b = A()
    print(b)
