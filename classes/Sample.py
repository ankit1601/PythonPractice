class Sample:
    def __init__(self):
        self.x = 10

    def modify(self):
        self.x += 1


if __name__ == '__main__':
    s1 = Sample()
    s2 = Sample()
    print(f'x for s1 {s1.x}')
    s1.modify()
    s1.x += 5
    print(f'x for s1 {s1.x}')
    print(f'x for s1 {s2.x}')
    s2.x += 1
    print(f'x for s1 {s2.x}')