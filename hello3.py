def count_multiples(numbers, divisors):
    """
    Counts the occurrences of numbers in a list that are multiples of given divisors.

    Args:
        numbers (list): The list of numbers to check.
        divisors (list): The list of numbers to check for as divisors.

    Returns:
        dict: A dictionary where keys are the divisors and values are the counts
              of numbers in 'numbers' that are multiples of that divisor.
    """
    result = {}
    for divisor in divisors:
        count = 0
        for num in numbers:
            if num % divisor == 0:
                count += 1
        result[divisor] = count
    return result





