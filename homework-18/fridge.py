class Fridge:
    def __init__(self, fabricator: str, capacity: float, model: str):
        self.fabricator = fabricator
        self.capacity = capacity
        self.model = model

    def open_door(self):
        return f'The door of {self.model} is open'

    def close_door(self):
        return f'The door of {self.model} is close'

    def turn_on(self):
        return f'the fridge {self.model} is on'

    def __str__(self):
        return (f'Fabricator: {self.fabricator}\n'
                f'Capacity: {self.capacity}\n'
                f'model: {self.model}')
