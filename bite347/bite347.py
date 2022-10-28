from enum import Enum

class Hand(str, Enum):
    RIGHT = "right"
    LEFT = "left"
    BOTH = "both"

# 27.10.2022

LEFT_HAND_CHARS = set("QWERTASDFGZXCVB")
RIGHT_HAND_CHARS = set("YUIOPHJKLNM")


def get_hand_for_word(word: str) -> Hand:
    """
    Use the LEFT_HAND_CHARS and RIGHT_HAND_CHARS sets to determine
    if the passed in word can be written with only the left or right
    hand, or if both hands are needed.
    """
    LEFT = True
    RIGHT = True
    for letter in word:
        if letter.upper() not in LEFT_HAND_CHARS:
            LEFT = False
            break
    for letter in word:
        if letter.upper() not in RIGHT_HAND_CHARS:
            RIGHT = False
            break
    if LEFT == True:
        return Hand.LEFT
    elif RIGHT == True:
        return Hand.RIGHT
    else:
        return Hand.BOTH


print(get_hand_for_word("terret"))