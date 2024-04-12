class Human:
    def __init__(self, name: str, surname: str, age: int, number: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.number = number

    def stand_up(self):
        return f'{self.name} {self.surname} stands up'

    def sit_down(self):
        return f'{self.name} {self.surname} sits down'

    def __str__(self):
        return (f'Name: {self.name}\n'
                f'Surname: {self.surname}\n'
                f'Age: {self.age}\n'
                f'Number: {self.number}')
