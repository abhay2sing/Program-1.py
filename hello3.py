def count_multiples(numbers, divisors):
    
    result = {}
    for divisor in divisors:
        count = 0
        for num in numbers:
            if num % divisor == 0:
                count += 1
        result[divisor] = count
    return result





