"""Credit score checking module."""


def check_credit_score(income, debt, missed_payments):
    """Return customer credit category."""

    if income >= 80000 and debt < 20000 and missed_payments == 0:
        return "Good Credit"

    if income >= 40000 and debt < 50000 and missed_payments <= 2:
        return "Average Credit"

    return "Poor Credit"
