import time
from datetime import datetime


def to_upper(func):
    def wrap(*args):
        result = func(*args)
        return result.upper()

    return wrap


def catch(func):
    def wrap(*args):
        try:
            func(*args)
        except ValueError:
            return 'ValueError'
        except TypeError:
            return 'TypeError'
        except ZeroDivisionError:
            return 'ZeroDivisionError'
    return wrap


def delay(func):
    def wrap(*args):
        time.sleep(3)
        return func(*args)
    return wrap


def count_time(func):
    def wrap(*args):
        start = datetime.now()
        func(*args)
        end = datetime.now()
        return f'Time: {end - start} Name: {func.__name__}'
    return wrap


@to_upper
@count_time
def function_1(string, num):
    return string * num


@delay
@catch
def function_2(a, b):
    return a / b

