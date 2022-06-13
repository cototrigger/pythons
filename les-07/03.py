class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Сумма клеток = {str(Cell(self.quantity + other.quantity))}'

    def __str__(self):
        return f'({self.quantity})'

    def __truediv__(self, other):
        return f'Деление клеток = {Cell(round(self.quantity // other.quantity))}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Клетка  равна: {sub}' if sub > 0 else 'Клетка исчезла'

    def __mul__(self, other):
        return f'Умножение клеток = {Cell(int(self.quantity * other.quantity))}'

    def make_order(self, cells_count):
        row = ''
        for _ in range(int(self.quantity / cells_count)):
            row += f'{"*" * cells_count}\\n '
        row += f'{"*" * (self.quantity % cells_count)}'
        return row


cell1 = Cell(43)
cell2 = Cell(23)

cell3 = Cell(14)
cell4 = Cell(2)

print()

print(cell1 + cell2)

print()

print(cell2 - cell1)
print(cell4 - cell3)

print()

print(cell2 * cell1)

print()

print(cell1 / cell2)

print()

print(cell1.make_order(5))
print(cell2.make_order(10))