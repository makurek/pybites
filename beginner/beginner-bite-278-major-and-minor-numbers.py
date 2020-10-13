from collections import OrderedDict
"""
You are given a list of integers. Write code to find the majority and minorty numbers in that list.
Definition: a majority number is the one appearing most frequently, a minority number appears least frequently.
Here is a simple example how it should work:

>>> numbers = [1, 2, 2, 3, 2, 3]
>>> major_n_minor(numbers)
(2, 1)
Note - you can assume that there will be only one of each.
Hint: any built-in library that supports convenient and rapid tallies?
"""

def major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """
    ###https: // stackoverflow.com / questions / 55125342 / usage - of - dict - value - and -dict - key - in -python3
    # https://stackoverflow.com/questions/52135345/is-some-dict-items-an-iterator-in-python
    # https://stackoverflow.com/questions/21062781/shortest-way-to-get-first-item-of-ordereddict-in-python-3
    test = {'oranges': 5,
            'apples': 3,
            'peach': 1}
    print(type((test.items())))
    print(type(test.values()))
    print(type(test.keys()))
    d = OrderedDict()
    for num in numbers:
        try:
            d[num] += 1
        except:
            d[num] = 1
    # difference between for i in d:
    # for i in d.items(): ?
    return (next((iter(reversed(d.items()))))[1], next(iter(d.items()))[1] )

print(major_n_minor([0,0,0,1,2,2]))