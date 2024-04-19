from house import House


class Human:
    def __init__(self, full_name: str, age: int, money: int, house: str):
        self.full_name = full_name
        self.age = age
        self.money = money
        self.house = house

    def earn_money(self, money: int):
        self.money += money
        return f'Add {money} to your wallet'

    def buy_house(self, house: House):
        if self.money < house.price:
            return 'Not enough money'

        self.money -= house.price

        if self.house == 'No':
            self.house = 'Yes'
            return 'You bought a house'
        return 'You bought another house'

    def __str__(self):
        return (f'Full name: {self.full_name}\n'
                f'Age: {self.age}\n'
                f'Money: {self.money}$\n'
                f'House: {self.house}')

    def __repr__(self):
        return (f'Full name: {self.full_name}\n'
                f'Age: {self.age}\n'
                f'Money: {self.money}$\n'
                f'House: {self.house}')
