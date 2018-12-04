def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and filters out numbers that
       are both positive and even (divisible by 2), try to use a
       list comprehension"""
    out = [ item for item in numbers if (item % 2 == 0) and item > 0]
    return out