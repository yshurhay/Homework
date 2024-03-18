def create_phone_number(array):
    return '({}{}{}) {}{}{}-{}{}-{}{}'.format(*array)


def buying_products(money: float, products: list[dict]) -> dict:
    products_price = 0
    for product in products:
        products_price += product['count'] * product['price']
    if money < products_price:
        return {"status": "fail", "comment": f"Not enough money. Deposit {products_price - money:.2f} money"}
    else:
        return {"status": "success", "comment": f"Products are paid"}


list_dicts = [
    {'product name': 'milk', 'count': 2, 'price': 12.5},
    {'product name': 'meat', 'count': 1, 'price': 20},
    {'product name': 'bread', 'count': 3, 'price': 7.3}
]
