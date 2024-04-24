class User:
    def __init__(self, name: str, surname: str, age: int, country: str, gender: str, profession: str = None):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country
        self.gender = gender
        self.profession = profession

    @property
    def email(self):
        return f'{self.name}.{self.surname}@gmail.com'

    @property
    def birth_year(self):
        return 2024 - self.age

    def be_doctor(self):
        return User(self.name, self.surname, self.age, self.country, self.gender, 'doctor')

    def be_policeman(self):
        return User(self.name, self.surname, self.age, self.country, self.gender, 'policeman')

    def be_teacher(self):
        return User(self.name, self.surname, self.age, self.country, self.gender, 'teacher')

    def __str__(self):
        return (f'Full name: {self.name} {self.surname}\n'
                f'Age: {self.age}\n'
                f'Country: {self.country}\n'
                f'Gender: {self.gender}\n'
                f'Profession: {self.profession}')

    def __repr__(self):
        return (f'Full name: {self.name} {self.surname}\n'
                f'Age: {self.age}\n'
                f'Country: {self.country}\n'
                f'Gender: {self.gender}\n'
                f'Profession: {self.profession}')
