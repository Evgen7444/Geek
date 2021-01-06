class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def fullname(self):
        return self.name + ' ' + self.surname

    def total(self):
        return self._income.get('wage') + self._income.get('bonus')


a = Position('Евген', 'Петров', 'Киллер', 200000, 75000)
print(a.fullname())
print(a.position)
print(a.total())
