"""
In this Bite you write a small class to keep track of the max score in a game.
When called as a function it receives a new score and returns the max score.
Note it should work with negative numbers as well.

This is how it should work:

  >>> from record import RecordScore

  >>> record = RecordScore()
  >>> print(record(10))
  10
  >>> print(record(9))
  10
  >>> print(record(11))  # new max
  11

  >>> record = RecordScore()
  >>> print(record(-5))
  -5
  >>> print(record(-10))
  -5
  >>> print(record(-2))  # new max
  -2
Use the __call__ dunder ("special") method to make the RecordScore class callable.

Good luck and keep calm and code in Python!
"""


class RecordScore():
    """Class to track a game's maximum score"""

    test = "dupek"

    def __init__(self):
        self._current_max = None

    def __call__(self, v):
        if self._current_max is None:
            self._current_max = v
        elif v > self._current_max:
            self._current_max = v
        return self._current_max

a = RecordScore()
b = RecordScore()

print(a.test)
print(b.test)

a.test = "srupek"

print(a.test)
print(b.test)
print(RecordScore.test)


