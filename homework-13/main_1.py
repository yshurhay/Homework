def create_multiplications(n):
    return [lambda x, a=i: a * x for i in range(n)]


class Dinglemouse(object):

    def __init__(self):
        self.name = None
        self.sex = None
        self.age = None
        self.string = 'Hello.'

    def setAge(self, age):
        if not self.age:
            self.string += ' I am {age}.'
        self.age = age
        return self

    def setSex(self, sex):
        if not self.sex:
            self.string += ' I am {sex}.'   
        self.sex = 'male' if sex == 'M' else 'female'
        return self

    def setName(self, name):
        if not self.name:
            self.string += ' My name is {name}.'
        self.name = name
        return self

    def hello(self):
        return self.string.format(age=self.age, name=self.name, sex=self.sex)
