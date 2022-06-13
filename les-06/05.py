class Stationery:
    def __init__(self, title):
        self.title = title

    @staticmethod
    def draw():
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Отрисовка {self.title}. Класс Pen')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Отрисовка {self.title}. Класс Pencil')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Отрисовка {self.title}. Класс Handle')


P_OBJ = Pen("ручкой")
PC_OBJ = Pencil("карандашом")
H_OBJ = Handle("маркером")

P_OBJ.draw()
PC_OBJ.draw()
H_OBJ.draw()