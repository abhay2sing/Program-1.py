import math

def generate_odd_series(a):
    """
    Generates a series of consecutive odd numbers starting from 1.
    The number of odd numbers in the series is determined by ceil(a/2).

    Args:
        a: An integer input.

    Returns:
        A comma-separated string of odd numbers.
    """
    if a <= 0:
        return ""  # Handle non-positive input gracefully, or raise an error

    num_odd_numbers = math.ceil(a / 2)
    series = []
    for i in range(int(num_odd_numbers)):
        series.append(str(2 * i + 1))
    return ", ".join(series)







