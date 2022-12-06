"""
4. Write a Python program to calculate a cat's age in cat's years. Note: For the first two years, a cat year is equal to 11.5 human years. After that, each cat year equals 3 human years.
Expected Output:
Input a cat's age in human years: 15

The cat's age in cat's years is 62
"""


def cats_age(years):
    if years <= 2:
        return years * 11.5

    return 23 + (years - 2) * 3


age = int(input("Enter Cat's Age in Human Years : "))

print("The Cat's Age in Cat's Years is :", cats_age(age))
