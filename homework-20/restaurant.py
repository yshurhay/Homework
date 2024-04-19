class Restaurant:
    def __init__(self, menu: list):
        self.menu = menu
        self.order = []

    def add_dish(self, dish: str):
        if dish not in self.menu:
            return f'No {dish} in menu'

        self.order.append(dish)
        return f'Add {dish} to order'

    def remove_dish(self, dish: str):
        if dish not in self.order:
            return f'No {dish} in order'

        self.order.remove(dish)
        return f'Remove {dish} from order'

    def make_order(self):
        if not self.order:
            return 'Your order is empty'
        order = '\n'.join(dish for dish in self.order)
        self.order = []
        return order
