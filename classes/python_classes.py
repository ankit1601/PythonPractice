from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def method(self):
        raise NotImplementedError


class B(A):
    def __init__(self):
        pass

    # def method(self):
    #     print("implemented")


if __name__ == '__main__':
    b = B()
    b.method()