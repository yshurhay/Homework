class Book:
    def __init__(self, book_name: str, author: str, pages_count: int, year: int):
        self.book_name = book_name
        self.author = author
        self.pages_count = pages_count
        self.year = year

    def __str__(self):
        return (f'Book name: {self.book_name}\n'
                f'Author: {self.author}\n'
                f'Pages count: {self.pages_count}\n'
                f'Year: {self.year}')
