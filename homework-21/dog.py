from mammal import Mammal


class Dog(Mammal):
    def __init__(self, species: str, age: int, weight: float, fur_type: str, diet: str, breed: str, temperament: str):
        Mammal.__init__(self, species, age, weight, fur_type, diet)
        self.breed = breed
        self.temperament = temperament

    def __eq__(self, other):
        result = Mammal.__eq__(self, other) and self.breed == other.breed and self.temperament == other.temperament
        return result

    def __repr__(self):
        return (f'{Mammal.__repr__(self)}\n'
                f'Breed: {self.breed}\n'
                f'Temperament: {self.temperament}')

    def __str__(self):
        return (f'{Mammal.__str__(self)}\n'
                f'Breed: {self.breed}\n'
                f'Temperament: {self.temperament}')
