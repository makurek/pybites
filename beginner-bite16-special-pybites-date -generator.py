'''
Write a generator that returns special dates for PyBites:

Every year mark counting from PYBITES_BORN date
Every 100 days mark counting from PYBITES_BORN
See the tests for more details how your code will be tested: as this is a beginner's
challenge we only calculate a few years ahead, leaving the next leap year (2020) out of this challenge.

We will revisit this in an intermediate challenge. Have fun! '''

'''
TEST CODE:

import datetime
from itertools import islice

from gendates import gen_special_pybites_dates


def test_gen_special_pybites_dates():
    gen = gen_special_pybites_dates()
    dates = list(islice(gen, 100))

    expected = [datetime.datetime(2017, 3, 29, 0, 0),    1
                datetime.datetime(2017, 7, 7, 0, 0),     2
                datetime.datetime(2017, 10, 15, 0, 0),   3
                datetime.datetime(2017, 12, 19, 0, 0),   0
                datetime.datetime(2018, 1, 23, 0, 0),    1
                datetime.datetime(2018, 5, 3, 0, 0),     2
                datetime.datetime(2018, 8, 11, 0, 0),    3
                datetime.datetime(2018, 11, 19, 0, 0),   0 ----
                datetime.datetime(2018, 12, 19, 0, 0),   1
                datetime.datetime(2019, 2, 27, 0, 0)]    2

    assert dates[:10] == expected
'''

from datetime import datetime
from datetime import timedelta
from itertools import islice


def gen_special_pybites_dates():
    PYBITES_BORN = datetime(year=2016, month=12, day=19)
    limit = datetime(year=2020, month=1, day=1)
    current = PYBITES_BORN
    delta_100d = timedelta(days=100)
    delta_1y = timedelta(days=365)
    exec_cnt = 1
    while(current.year <= 2020):
        if exec_cnt % 4:
            current = current + delta_100d
            yield current
        else:
            PYBITES_BORN = PYBITES_BORN + delta_1y
            yield PYBITES_BORN
        exec_cnt = exec_cnt + 1



gen = gen_special_pybites_dates()
dates = list(islice(gen,20))
print(dates)

