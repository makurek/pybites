"""
Complete flatten that takes a list of lists (which can have lists ad infinitum) and flatten them into a one dimensional
list.

So this input:

[1, [2, 3], [4, 5, [6, 7, [8, 9, 10]]]]
... should generate this output:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
(Making this a generator is fine too, the test will convert that into a list).

Make sure you support both lists and tuples. You probably want to use recursion here ... have fun!
"""

def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])


print(flatten([1, [2, 3], [4, 5, [6, 7, [8, 9, 10]]]]))



