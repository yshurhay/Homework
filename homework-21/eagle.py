from bird import Bird


class Eagle(Bird):
    def __init__(self, species: str, age: int, weight: float, wingspan: float, flight_speed: float, beak_length: float,
                 prey_type: str):
        super(Bird).__init__(species, age, weight, wingspan, flight_speed)
        self.beak_length = beak_length
        self.prey_type = prey_type

    def __eq__(self, other):
        result = Bird.__eq__(self, other) and self.beak_length == other.beak_length and self.prey_type == other.prey_type
        return result

    def __gt__(self, other):
        return Bird.__gt__(self, other) and self.beak_length > other.beak_length

    def __lt__(self, other):
        return Bird.__lt__(self, other) and self.beak_length < other.beak_length

    def __ge__(self, other):
        return Bird.__ge__(self, other) and self.beak_length >= other.beak_length

    def __le__(self, other):
        return Bird.__le__(self, other) and self.beak_length <= other.beak_length

    def __repr__(self):
        return (f'{Bird.__repr__(self)}\n'
                f'Beak length: {self.beak_length} sm\n'
                f'Prey type: {self.prey_type}')

    def __str__(self):
        return (f'{Bird.__str__(self)}\n'
                f'Beak length: {self.beak_length} sm\n'
                f'Prey type: {self.prey_type}')
