from countries import countries


class Car:
    obj_count = 0

    def __init__(self, mileage: int, name: str, year: int, price: float):
        self._mileage = mileage
        self.name = name
        self.year = year
        self.price = price
        Car.obj_count += 1

    def __eq__(self, other):
        return self.year == other.year and self.name == other.name

    def __str__(self):
        return (f'Mileage: {self.mileage}\n'
                f'Name: {self.name}\n'
                f'Year: {self.year}\n'
                f'Price: {self.price} BYN')

    def __repr__(self):
        return (f'Mileage: {self.mileage}\n'
                f'Name: {self.name}\n'
                f'Year: {self.year}\n'
                f'Price: {self.price} BYN')

    def get_price(self, value: str):
        if value.lower() == 'rub':
            return f'{self.price * 28.5} RUB'
        elif value.lower() == 'usd':
            return f'{self.price * 0.32} USD'
        else:
            return 'Not correct value'

    @classmethod
    def get_obj_count(cls):
        return cls.obj_count

    @staticmethod
    def get_country(brand: str):
        if brand in countries:
            return countries[brand]
        return f'No info about {brand}'

    def get_mileage(self):
        return self._mileage

    def set_mileage(self, value: int):
        self._mileage = value

    def delete_mileage(self):
        self._mileage = 0

    mileage = property(fget=get_mileage, fset=set_mileage, fdel=delete_mileage)


class Audi(Car):
    @staticmethod
    def get_country(brand='Audi'):
        return countries[brand]
