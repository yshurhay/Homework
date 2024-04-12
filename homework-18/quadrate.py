class Quadrate:
    def __init__(self, side: float, color: str):
        self.side = side
        self.color = color

    def count_square(self):
        square = self.side * self.side
        return f'Square: {square}'

    def count_perimeter(self):
        perimeter = self.side * 4
        return f'Perimeter: {perimeter}'

    def __str__(self):
        return (f'Side length: {self.side}\n'
                f'Color: {self.color}')
