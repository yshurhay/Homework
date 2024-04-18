class Bank:
    def __init__(self):
        self.account = None

    def open_account(self):
        self.account = 0
        return 'Account is open'

    def close_account(self):
        self.account = None
        return 'Account is close'

    def put_money(self, money):
        if self.account is None:
            return 'You have to open account'
        self.account += money
        return f'You put {money} to account'

    def take_money(self, money):
        if self.account is None:
            return 'You have to open account'
        if money > self.account:
            return 'Not enough money'
        self.account -= money
        return f'You take {money} from account'
