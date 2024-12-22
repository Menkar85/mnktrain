def mean_three_round_three(x, y, z):
    """Calculates average of 3 digits and rounds
    it to 3 decimals.
    >>> mean_three_round_three(20, 30, 70)
    40.0
    >>> mean_three_round_three(1, 5, 8)
    4.667
    """
    return round((x + y + z) / 3, 3)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
