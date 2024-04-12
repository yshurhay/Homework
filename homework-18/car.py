class Car:
    def __init__(self, brand: str, model: str, year: int, color: str):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def turn_on_engine(self):
        return f'Engine of {self.brand} is on'

    def __str__(self):
        return (f'Brand: {self.brand}\n'
                f'Model: {self.model}\n'
                f'Year: {self.year}\n'
                f'Color: {self.color}')
