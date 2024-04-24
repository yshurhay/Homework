class Animal:
    def __init__(self, species: str, age: int, weight: float):
        self.species = species
        self.age = age
        self.weight = weight

    def __eq__(self, other):
        result = self.species == other.species and self.age == other.age and self.weight == other.weight
        return result

    def __gt__(self, other):
        return self.weight > other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __ge__(self, other):
        return self.weight >= other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __repr__(self):
        return (f'Species: {self.species}\n'
                f'Age: {self.age}\n'
                f'Weight: {self.weight} kg')

    def __str__(self):
        return (f'Species: {self.species}\n'
                f'Age: {self.age}\n'
                f'Weight: {self.weight} kg')
