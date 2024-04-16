from house import House
from human import Human


def get_recommendations(human: Human, houses: list[House], discount):
    if discount == 'on':
        rec_houses = list(filter(lambda house: house.price <= human.money and house.discount == 'Yes', houses))
    elif discount == 'off':
        rec_houses = list(filter(lambda house: house.price <= human.money and house.discount == 'No', houses))
    else:
        rec_houses = list(filter(lambda house: house.price <= human.money, houses))

    rec_houses = sorted(rec_houses, key=lambda house: house.price / house.square)
    return rec_houses
