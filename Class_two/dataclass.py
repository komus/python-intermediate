# simple class
from dataclasses import dataclass

class Book:
    def __init__(self, name:str, author:str, year:int):
        self.name = name
        self.author = author
        self.year = year

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def is_new_book(self, current_year):
        diff = int(current_year) - int(self.year)
        if(diff > 2):
            return False
        return True


@dataclass
class BookDS:
    name:str
    author:str
    year:int

    def is_new_book(self, current_year:int):

        diff = int(current_year) - int(self.year)
        if(diff > 2):
            return false
        return true

book1 = BookDS("Things fall apart", "chinwe Aechiebe", "1979")
print(book1.name)
print(book1)
book1.name = "New name"
print(book1.name)
