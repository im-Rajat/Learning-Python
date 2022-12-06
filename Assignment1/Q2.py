"""
2. If you have a list b = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Using only a single line of Python code that takes this list b as input and generates a new list that should have only even elements of this list b in it.
"""


list_a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list_b = [i for i in list_a if i % 2 == 0]

print(list_b)