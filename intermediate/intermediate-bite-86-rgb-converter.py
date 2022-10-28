"""
Designer Mary wants to convert her CSS from statements like background-color: rgb(128, 128, 0);
to: background-color: #808000;.

Don't worry, you don't have to rewrite CSS, just complete the rgb_to_hex helper for her that takes a tuple
of RGB (3 ints) and converts it to the corresponding hex value.

For example for Maroon you would call it like rgb_to_hex((128, 0, 0)) and it would return the hex #800000.

Make sure you check that each r, g and b int is within the valid range of 0 and 255 (both included),
if not raise a ValueError, Explicit is better than implicit (Zen).

Check the TESTS tab for more examples, there we check your code for 16 colors and 3 excepions. Have fun!
"""

def _is_valid_color(rgb):
    if (rgb >= 0) and (rgb <= 255):
        return True
    else:
        return False


def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    if not all([_is_valid_color(t) for t in rgb]):
        raise ValueError
    else:
        output = "#{:02X}{:02X}{:02X}".format(rgb[0], rgb[1], rgb[2])
    print(rgb[2])
    return output

print(rgb_to_hex((0,0,255)))
