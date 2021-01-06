class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} стартовал'

    def stop(self):
        return f'{self.name} остановился'

    def turn_right(self):
        return f'{self.name} повернул направо'

    def turn_left(self):
        return f'{self.name} повернул налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} составляет {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):

        print(f'Текущая скорость городского автомобиля {self.name} составляет {self.speed} км/ч')

        if self.speed > 60:
            return f'Скорость {self.name} превышает разрешенную для городского авто'
        else:
            return f'Скорость {self.name} в пределах нормы для городского авто'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочего автомобиля {self.name} составляет {self.speed} км/ч')

        if self.speed > 40:
            return f'Скорость {self.name} превышает разрешенную для рабочего авто'
        else:
            return f'Скорость {self.name} в пределах нормы для рабочего авто'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из полицейского гаража'
        else:
            return f'{self.name} отношения к полиции не имеет'


Zonda = SportCar(320, 'красная', 'Зонда', False)
Kia = TownCar(160, 'зеленая', 'Киа', False)
Porter = WorkCar(38, 'белый с кузовом', 'Портер', False)
Skoda = PoliceCar(320, 'серебристый', 'Шкода', True)
print(Kia.turn_left())
print(f'Когда {Zonda.turn_right()}, {Porter.stop()}')
print(f'{Skoda.name} имеет {Skoda.color} цвет')
print(f'{Porter.name} относится к полиции? {Porter.is_police}')
print(f'{Skoda.name} относится к полиции? {Skoda.is_police}')
print(f'{Zonda.name} относится к полиции? {Zonda.is_police}')
print(Zonda.show_speed())
print(Kia.show_speed())
print(Skoda.police())
print(Porter.show_speed())
