
"""
TASK DESCRIPTION:

Write a function that can sum up numbers:

It should receive a list of n numbers.
If no argument is provided, return sum of numbers 1..100.
Look closely to the type of the function's default argument ...
"""
input = []

############################### KEY TAKEAWAYS #################################
###
###
###
###
###
################################################################################


### ----------- My solution ---------------------------

def my_sum_numbers(numbers=None):
    result = 0
    # Dlaczego samo "if numbers:" nie dziala? Tzn. wtedy jak podamy pusta liste to nie spelnia warunku?
    # albo inaczej, przy przekazywaniu argumentu "if arg" dla pelnej tablicy dziala, dla pustej nie
    # "false" values include False, None, 0 and [] (an empty list).
    if numbers != None:
        for item in numbers:
            result += item
        return result
    for i in range(101):
        result += i
    return result


def test_sum(num=None):
    return sum(num)


### ---------- PyBites original solution ---------------

def pyb_sum_numbers(numbers=None):
    if numbers is None:
        numbers = range(1, 101)
    return sum(numbers)

### Tutaj nie wiem, co chcialem osiagnac. Chyba chcialem sprawdzic alternatywny sposob, jak moznaby
### cos takiego napisac. Zamiast sprawdzac, co zostalo przekazane jako argument, mozna
### probowac obsluzyc wyjatek 'NoneType' object is not iterable

def sum_numbers_1(numbers=None):
    try:
        return sum(numbers)
    except TypeError:
        return sum(range(1,101))


print(pyb_sum_numbers(input))

print(test_sum())