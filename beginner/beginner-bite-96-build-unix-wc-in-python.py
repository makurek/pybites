'''
In this Bite you will convert Unix' wc command into Python. Your function takes a file (absolute path),
reads it in and calculates the lines/words/chars. It returns a string of these numbers and the filename,
like as a typical wc output, for example:

$ wc wc.py
      13      56     514 wc.py
Don't worry about the amount of white space between the columns, you can use tabs or spaces.

Unix files add an extra newline to the end, you don't have to make that assumption here, so 'Hello\nworld' == 11 chars
not 12 as Unix' wc would return. Let's keep it simple. Do note that newline (\n) counts as a char.

See the tests for more info. Thanks Brian for introducing us to pytest's tmp_path fixture!

Have fun and keep coding in Python!

'''

def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    pass

