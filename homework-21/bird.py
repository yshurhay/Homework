from animal import Animal


class Bird(Animal):
    def __init__(self, species: str, age: int, weight: float, wingspan: float, flight_speed: float):
        Animal.__init__(self, species, age, weight)
        self.wingspan = wingspan
        self.flight_speed = flight_speed

    def __eq__(self, other):
        result = Animal.__eq__(self, other) and self.wingspan == other.wingspan and self.flight_speed == other.flight_speed
        return result

    def __gt__(self, other):
        return Animal.__gt__(self, other) and self.wingspan > other.wingspan and self.flight_speed > other.flight_speed

    def __lt__(self, other):
        return Animal.__lt__(self, other) and self.wingspan < other.wingspan and self.flight_speed < other.flight_speed

    def __ge__(self, other):
        return Animal.__ge__(self, other) and self.wingspan >= other.wingspan and self.flight_speed >= other.flight_speed

    def __le__(self, other):
        return Animal.__le__(self, other) and self.wingspan <= other.wingspan and self.flight_speed <= other.flight_speed

    def __repr__(self):
        return (f'{Animal.__repr__(self)}\n'
                f'Wingspan: {self.wingspan} sm\n'
                f'Flight speed: {self.flight_speed} km/s')

    def __str__(self):
        return (f'{Animal.__str__(self)}\n'
                f'Wingspan: {self.wingspan}\n'
                f'Flight speed: {self.flight_speed} km/s')
