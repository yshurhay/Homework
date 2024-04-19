class House:
    def __init__(self, square: int, price: int, discount: str):
        self.square = square
        self.price = price
        self.discount = discount

    def apply_discount(self):
        if self.discount == 'Yes':
            return 'Discount already applied'

        self.discount = 'Yes'
        self.price *= 0.75
        return 'Discount applied successfully'

    def __str__(self):
        return (f'Square: {self.square} m2\n'
                f'Price: {self.price}$\n'
                f'Discount: {self.discount}')

    def __repr__(self):
        return (f'Square: {self.square} m2\n'
                f'Price: {self.price}$\n'
                f'Discount: {self.discount}')
