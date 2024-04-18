def check_exp(exp: int):
    if exp > 10000:
        return 10000
    return exp


def check_level(exp: int):
    return int(exp // 100)


def check_rank(lvl: int):
    if 1 < lvl < 10:
        return 'Pushover'
    elif 10 <= lvl < 20:
        return 'Novice'
    elif 20 <= lvl < 30:
        return 'Fighter'
    elif 30 <= lvl < 40:
        return 'Warrior'
    elif 40 <= lvl < 50:
        return 'Veteran'
    elif 50 <= lvl < 60:
        return 'Sage'
    elif 60 <= lvl < 70:
        return 'Elite'
    elif 70 <= lvl < 80:
        return 'Conqueror'
    elif 80 <= lvl < 90:
        return 'Champion'
    elif 90 <= lvl < 100:
        return 'Master'
    elif lvl == 100:
        return 'Greatest'

