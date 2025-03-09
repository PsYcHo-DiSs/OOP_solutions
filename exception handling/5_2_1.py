def to_number(value):
    if value.isdigit():
        return int(value)
    try:
        return float(value)
    except ValueError:
        return value


try:
    a, b = input().split()
    a, b = to_number(a), to_number(b)
except ValueError:
    pass
finally:
    print(a + b if isinstance(a, (int, float)) and isinstance(b, (int, float)) else str(a) + str(b))
