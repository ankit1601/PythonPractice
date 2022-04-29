class Vehicle:
    def __init__(self, type_='Car'):
        self.type = type_

    def count_tyre(self):
        print(f'{self.type} have 4 tyres')


class Ford(Vehicle):
    def __init__(self):
        super().__init__() # if this statement is not there then parent class constructor is overridden
        self.type = 'Ford Car'

    def count_tyre(self):
        super().count_tyre() # we are calling parent class method using Ford instance
        print(f'{self.type} have 6 tyre')


if __name__ == '__main__':
    Veh = Vehicle()
    Veh.count_tyre()

    Ford_ = Ford()
    Ford_.count_tyre()

    if isinstance(Ford_, Vehicle):
        print(True)

    if isinstance(Veh, Vehicle):
        print(True)

    if isinstance(Ford_, Ford):
        print(True)

    if isinstance(Veh, Ford):
        print(True)
    else:
        print(False)
