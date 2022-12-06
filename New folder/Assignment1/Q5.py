"""
5. Write a program which accepts input from console which is numbers separated by comma as shown below and generate a list & a tuple of all that numbers.

Input:
34,67,55,33,12,98

Output:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""


numbers_list = list(map(int, input("Enter comma seperated Numbers : ").split(', ')))
numbers_tuple = tuple(numbers_list)

print("Generated List :", numbers_list)
print("Generated Tuple :", numbers_tuple)
