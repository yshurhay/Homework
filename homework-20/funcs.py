from ranks import ranks


def check_exp(exp: int):
    if exp > 10000:
        return 10000
    return exp


def check_level(exp: int):
    return int(exp // 100)


def check_rank(lvl: int):
    return ranks[lvl // 10]
