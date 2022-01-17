from collections import namedtuple
"""
Sometimes you need to restructure a nested data structure.
For example you can convert a dict in a list of
 (key, value) tuples via dict.items().

In this Bite a real world scenario where we
wanted to plot some data from a Counter dict.

For plots you typically need 2 lists: X + Y axis or
 labels + values. So we needed an easy way to transpose
 data structures.

Complete the transpose function to do just that.
It has to work for both dicts and lists of (named)tuples.
 Examples given in the docstring. See also the TESTS tab.
 Have fun!
"""


def transpose(data):
    """Transpose a data structure
      1. dict
      data = {'2017-8': 19, '2017-9': 13}
      In:  transpose(data)
      Out: [('2017-8', '2017-9'), (19, 13)]

      2. list of (named)tuples
      data = [Member(name='Bob', since_days=60, karma_points=60,
                     bitecoin_earned=56),
              Member(name='Julian', since_days=221,
              karma_points=34,
                     bitecoin_earned=78)]
      In: transpose(data)
      Out: [('Bob', 'Julian'), (60, 221), (60, 34), (56, 78)]
      """
    Member = namedtuple('Member', 'name since_days karma_points bitecoin_earned')

    data = [Member(name='Bob', since_days=60, karma_points=60,
                   bitecoin_earned=56),
            Member(name='Julian', since_days=221,
                   karma_points=34,
                   bitecoin_earned=78)]

    #if data is list
    #keys = data.keys()
    #values = data.values()
    #t = [tuple(keys), tuple(values)]
    #print(t)
    """
    t = [tuple(e[0] for e in data), tuple(e[1] for e in data), tuple(e[2] for e in data), tuple(e[3] for e in data)]
    print(t)
    """
    print(*data)



transpose({'2017-8': 18, '2017-9': 13})