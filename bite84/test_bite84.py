import pytest
from bite84 import bite84

@pytest.mark.parametrize("input_arg, expected", [([4,[2,1]], [4,2,1]), ([1,2,[3,[5,6]]], [1,2,3,5,6])])
def test_flatten(input_arg, expected):
    assert bite84.flatten(input_arg) == expected