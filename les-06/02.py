class Road:
    weight = 25
    thickness = 0.1

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc(self):
        res = (self.length * self.width * Road.weight * Road.thickness) / 1000
        print(f'Потребуется {res} тонн')


r_obj = Road(200, 5000)
r_obj.calc()
