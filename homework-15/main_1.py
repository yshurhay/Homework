def annotations(func):
    def wrap(**kwargs):
        func(**kwargs)
        for key, value in kwargs.items():
            if not isinstance(value, func.__annotations__[key]):
                return False
        return True
    return wrap


@annotations
def task_1(a: int, b: str):
    return a * b


def access(func):
    def wrap(user_type):
        if user_type.lower() == 'admin':
            print('access')
            print(func(user_type))
        elif user_type.lower() in ('user', 'auth_user'):
            print('denied')
        else:
            print('not correct input')
    return wrap


@access
def task_2(user_type):
    return f'Hello {user_type}'


def memo(fn):
    cache = {}
    miss = object()

    def wrapper(*args):
        result = cache.get(args, miss)
        if result is miss:
            result = fn(*args)
            cache[args] = result
        return result

    return wrapper


@memo
def task_3(a, b):
    return a + b


print(task_3(1, 2))
print(task_3(3, 4))
print(task_3(5, 6))



def memo(func):
    cache = []
    arr = []

    def wrapper(*args):
        if not arr:
            result = func(*args)
            cache.append(result)
            arr.append(1)
            return cache
        elif len(arr) == 3:
            arr.clear()
            return cache
        else:
            arr.append(1)
            return cache

    return wrapper


@memo
def function(a, b):
    return a + b


print(function(1, 2))
print(function(1, 3))
print(function(1, 4))
print(function(1, 5))
print(function(1, 6))