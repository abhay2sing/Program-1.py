def generate_odd_series(a):
    
    if a <= 0:
        return ""

    series = []
    current_odd = 1
    for _ in range(a):
        series.append(str(current_odd))
        current_odd += 2
    return ", ".join(series)





