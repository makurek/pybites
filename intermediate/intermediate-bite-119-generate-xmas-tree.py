"""
In this Bite you complete generate_xmas_tree that takes a rows arg (= height of the tree).
For each row you print row_number*2-1 stars and center them, so for default height=10 the tree would look like this:

         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
No printing to the console this time, you return this output from the function (use newlines / \n between the lines).
Good luck and keep calm and code in Python!

"""

def generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""

    MAX = rows*2-1
    RESULT = ""
    padding = " "
    arr = []
    for current_row in range(1, rows+1):
        #LINE = '{message}:>{fill}'.format(message="*"*current_row, fill=((MAX-current_row)/2)-1)
        in_this_row = current_row*2 -1
        s = "*" * in_this_row
        p = int((MAX-in_this_row)/2)
        #print(f'{s:{padding}>{p}}')
        LINE = s.center(MAX, ' ')
        arr.append(LINE)
    RESULT = '\n'.join(arr)
    return RESULT




generate_xmas_tree()