import pytest
from game_of_life import *

def test_advance_should_return_a_set():
    assert isinstance(advance(set()), set)
