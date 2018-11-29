VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    """Ask for color, lowercase it, check if 'quit' is entered, if so print
       'bye' and break, next check if given color is in VALID_COLORS, if not,
       continue, finally if that check passes, print the color"""
    while True:
        inp = input("Enter color:").lower()
        if inp == 'quit':
            print("bye")
            break

        if inp not in VALID_COLORS:
            print("Not a valid color")
            continue
        else:
            print(inp)
            break


print_colors()