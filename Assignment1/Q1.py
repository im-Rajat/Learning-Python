"""
1. Write a Python program that has a member function Sum inside class. This function will have array_numbers and target_sum as input to them. This function should find index of the consecutive two numbers from input array_numbers , addition of which should match the input target_sum. This function will return index of that two consecutive numbers.

For e.g.
Input: array_numbers= [10,20,10,40,50,60,70], target_sum=50 Output: 3, 4
"""


class ConsecutiveNumber:

    def __init__(self):
        pass

    def sum(self, numbers, target_sum):
        for i in range(len(numbers) - 1):
            if (numbers[i] + numbers[i + 1]) == target_sum:
                return i + 1, i + 2
        return "Not", "Found"


array_numbers = [10, 20, 10, 40, 50, 60, 70]
target_sum = 50

obj1 = ConsecutiveNumber()
x, y = obj1.sum(array_numbers, target_sum)
print(x, y)
