import pytest

from reverse_string import reverse_string

def test_empty():
    assert reverse_string('') == ''

def test_one_char():
    assert reverse_string('a') == 'a'

def test_two_chars():
    assert reverse_string('ab') == 'ba'

def test_many_chars():
    assert reverse_string('computer') == 'retupmoc'