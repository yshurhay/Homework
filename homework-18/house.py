class House:
    def __init__(self, floors_count: int, rooms_count: int):
        self.floors = floors_count
        self.rooms = rooms_count

    def count_price(self):
        price = self.rooms * self.floors * 100
        return f'Price {price}$'

    def __str__(self):
        return (f'Floors count: {self.floors}\n'
                f'Rooms count: {self.rooms}')

