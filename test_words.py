"""Verify that the prefix and suffix functions work correctly."""

from words import prefix, suffix
import pytest


def test_prefix():
    """Verify that the prefix function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the prefix function and verify that it returns a string.
    pre = prefix("upbeat", "upgrade")
    assert isinstance(pre, str), "prefix function must return a string"

    # Call the prefix function nine times and use an assert
    # statement to verify that the string returned by the
    # prefix function is correct each time.
    
    assert prefix("", "") == ""
    assert prefix("", "correct") == ""
    assert prefix("clear", "") == ""
    assert prefix("happy", "funny") == ""
    assert prefix("cat", "catalog") == "cat"
    assert prefix("dogmatic", "dog") == "dog"
    assert prefix("jump", "joyous") == "j"
    assert prefix("upbeat", "upgrade") == "up"
    assert prefix("Disable", "dIstasteful") == "dis"



def test_suffix():
    """Verify that the suffix function works correctly."
    Parameters: none
    Return: nothing
    """
    # Call the suffix function and verify that it returns a string.
    suf = suffix("upbeat", "upgrade")
    assert isinstance(suf, str), "suffix function must return a string"

    # Call the suffix function nine times and use an assert
    # statement to verify that the string returned by the
    # suffix function is correct each time.
    
   


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.

