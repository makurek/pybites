
"""
Write a function that can sum up numbers:

It should receive a list of n numbers.
If no argument is provided, return sum of numbers 1..100.
Look closely to the type of the function's default argument ...
"""
input = []

def my_sum_numbers(numbers=None):
    result = 0
    # Dlaczego samo "if numbers:" nie dziala? Tzn. wtedy jak podamy pusta liste to nie spelnia warunku?
    if numbers != None:
        for item in numbers:
            result += item
        return result
    for i in range(101):
        result += i
    return result

def sum_numbers(numbers=None):
    if numbers is None:
        numbers = range(1, 101)
    return sum(numbers)

print(sum_numbers(input))