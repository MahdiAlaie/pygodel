import pytest
from pygodel.syntax import FormalValidator

def test_balanced_parentheses_valid():
    validator = FormalValidator()
    assert validator.check_balanced_parentheses(["(", "x1", "∧", "x2", ")"]) is True
    assert validator.check_balanced_parentheses(["(", "(", "x1", ")", ")"]) is True
    assert validator.check_balanced_parentheses(["x1"]) is True


def test_balanced_parentheses_invalid():
    validator = FormalValidator()
    assert validator.check_balanced_parentheses([")", "("]) is False
    assert validator.check_balanced_parentheses(["(", "x1", "∧", "x2"]) is False
    assert validator.check_balanced_parentheses(["(", "x1", ")", ")"]) is False

def test_valid_token_sequence():
    validator = FormalValidator()

    assert validator.is_valid_token_squence(["(", "∧", ")"]) is True
    assert validator.is_valid_token_squence(["x1", "@", "x2"]) is False
    assert validator.is_valid_token_squence([]) is False

