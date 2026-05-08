"""Tests for credit score checker."""

from src.credit import check_credit_score


def test_good_credit():
    """Test good credit condition."""
    result = check_credit_score(100000, 10000, 0)

    assert result == "Good Credit"


def test_average_credit():
    """Test average credit condition."""
    result = check_credit_score(50000, 30000, 1)

    assert result == "Average Credit"


def test_poor_credit():
    """Test poor credit condition."""
    result = check_credit_score(25000, 80000, 5)

    assert result == "Poor Credit"
