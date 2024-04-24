from animal import Animal


class Mammal(Animal):
    def __init__(self, species: str, age: int, weight: float, fur_type: str, diet: str):
        Animal.__init__(self, species, age, weight)
        self.fur_type = fur_type
        self.diet = diet

    def __eq__(self, other):
        result = Animal.__eq__(self, other) and self.fur_type == other.fur_type and self.diet == other.diet
        return result

    def __repr__(self):
        return (f'{Animal.__repr__(self)}\n'
                f'Fur type: {self.fur_type}\n'
                f'Diet: {self.diet}')

    def __str__(self):
        return (f'{Animal.__str__(self)}\n'
                f'Fur type: {self.fur_type}\n'
                f'Diet: {self.diet}')
