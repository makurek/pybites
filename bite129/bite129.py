"""
In this Bite we will answer some questions about stocks, using some JSON data obtained from the awesome Mockeroo fake
data generator service.

Here is a snippet of the output you will parse (full output here):

  [{"id":1,"name":"Anworth Mortgage Asset  Corporation",
    "symbol":"ANH","industry":"Real Estate Investment Trusts",
    "sector":"Consumer Services","market":"NYSE","cap":"$600.57M"},
   {"id":2,"name":"DarioHealth Corp.",
   "symbol":"DRIO","industry":"Medical/Dental Instruments",
   "sector":"Health Care","market":"NASDAQ","cap":"$21.78M"},
   ... 998 more stocks ...
  ]
Complete the 4 functions below following the instructions in the docstrings. Good luck and keep calm and parse your
Data in Python.
"""

import requests
from itertools import groupby


STOCK_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off, multiply by 1,000 and return
         value as float"""
    if cap == 'n/a':
        return 0
    if cap[-1:] == 'M':
        return float(cap[1:-1])
    if cap[-1:] == 'B':
        return float(cap[1:-1])*1000


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    sum = 0
    for stock in data:
        if stock['industry'] == industry:
            sum += _cap_str_to_mln_float(stock['cap'])
    return float("{:.2f}".format(sum))


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    result = sorted(data, key=lambda x: _cap_str_to_mln_float(x['cap']), reverse=True)
    return result[0]['symbol']


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""

    filtered = list()
    result = []
    for elem in data:
        if elem['sector'] != 'n/a':
            filtered.append(elem)
    def key_func(k):
        return k['sector']
    SOR = sorted(filtered, key=key_func)
    for key, value in groupby(SOR, key_func):
        result.append((key,len(list(value))))
    s = sorted(result, key=lambda x:x[1])
    return((s[len(s)-1][0], s[0][0]))





print(get_sectors_with_max_and_min_stocks())