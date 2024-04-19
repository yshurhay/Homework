from funcs import check_rank, check_level, check_exp


class Warrior:
    def __init__(self):
        self.level = 1
        self.exp = 100
        self.rank = 'Pushover'
        self.achievements = []

    def battle(self, enemy_lvl):
        difference = self.level - enemy_lvl
        if difference == 0:
            self.exp += 10
            self.check_stats()
            return 'A good fight'
        elif difference == 1:
            self.exp += 5
            self.check_stats()
            return 'A good fight'
        elif difference >= 2:
            return 'Easy fight'
        elif -5 < difference <= -1:
            self.exp += 20 * difference * difference
            self.check_stats()
            return 'An intense fight'
        else:
            return "You've been defeated"

    def training(self, train: tuple):
        name, exp, lvl = train
        if lvl > self.level:
            return 'Not strong enough'
        self.exp += exp
        self.check_stats()
        self.achievements.append(name)
        return name

    def check_stats(self):
        self.exp = check_exp(self.exp)
        self.level = check_level(self.exp)
        self.rank = check_rank(self.level)

    def __str__(self):
        return (f'Level: {self.level}\n'
                f'Exp: {self.exp}\n'
                f'Rank: {self.rank}\n'
                f'Achievements: {self.achievements}')

    def __repr__(self):
        return (f'Level: {self.level}\n'
                f'Exp: {self.exp}\n'
                f'Rank: {self.rank}\n'
                f'Achievements: {self.achievements}')
