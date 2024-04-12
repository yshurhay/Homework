class Pupil:
    def __init__(self, name: str, surname: str, age: int, marks: tuple):
        self.name = name
        self.surname = surname
        self.age = age
        self.marks = marks

    def count_gpa(self):
        gpa = sum(self.marks) / len(self.marks)
        return f'GPA: {gpa}'

    def get_achievements(self):
        gpa = sum(self.marks) / len(self.marks)
        if gpa > 9:
            return f'{self.name} {self.surname} is an excellent student'
        elif gpa > 7.5:
            return f'{self.name} {self.surname} is a good student'
        elif gpa > 6:
            return f'{self.name} {self.surname} is an average student'
        else:
            return f'{self.name} {self.surname} is a bad student'

    def __str__(self):
        return (f'Name: {self.name}\n'
                f'Surname: {self.surname}\n'
                f'Age: {self.age}\n'
                f'Marks: {self.marks}')
    