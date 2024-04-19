from random import choice, randint
from house import House


def generate_houses():
    return [House(
        square=randint(15, 35) * 5,
        price=randint(10, 100) * 1000,
        discount=choice(('Yes', 'No'))
    ) for _ in range(10)]
