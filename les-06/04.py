class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction):
        return f'{self.name} повернула {direction}'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name} составляет {self.speed}'


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f'Скорость автомобиля {self.name} выше, чем это позволено для городского автомобиля'
        else:
            return f'Скорость автомобиля {self.name} нормальная для городского автомобиля'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочего автомобиля {self.name} составляет {self.speed}')

        if self.speed > 40:
            return f'Скорость автомобиля {self.name} выше, чем это позволено для рабочего автомобиля'
        else:
            return f'Скорость автомобиля {self.name} нормальная для рабочего автомобиля'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def sport(self):
        if self.is_police:
            return f'Автомобиль {self.name} является спортивным'
        else:
            return f'Автомобиль {self.name} не является спортивным'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'Автомобиль {self.name} является полицейским'
        else:
            return f'Автомобиль {self.name} не является полицейским'


HONDA = TownCar(80, 'Черная', 'Хонда', False)
JEEP = WorkCar(70, 'Серая', 'Джип', False)
AUDI = SportCar(100, 'Красная', 'Ауди', False)
NISSAN = PoliceCar(110, 'Бело-синяя',  'Ниссан', True)

print(JEEP.turn("Направо"))
print(f'Когда {HONDA.turn("Налево")}, то {AUDI.stop()}')
print(f'{JEEP.go()} со скоростью {JEEP.show_speed()}')
print(f'{JEEP.name} цвета {JEEP.color}')

print(f'{AUDI.name} полицейская машина? {AUDI.is_police}')
print(f'{JEEP.name} полицейская машина? {JEEP.is_police}')

print(AUDI.show_speed())
print(HONDA.show_speed())
print(NISSAN.police())
print(NISSAN.show_speed())