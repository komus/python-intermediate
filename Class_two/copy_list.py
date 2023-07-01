from copy import deepcopy, copy
from dataclass import Book

book1 = Book("try again", "value", 2012)

original_list = ['apple', 'bread', book1]

shallow_copy = list(original_list)
deep_copy = deepcopy(original_list)


original_list[0] = 'Tuna fish'
book1.name = "values"
print(f"original list: {original_list[2].name}")
print(f"Shallow list: {shallow_copy[2].name}")
print(f"Deep list: {deep_copy[2].name}")

