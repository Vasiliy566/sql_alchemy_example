def max_number(a: int, b: int, c: int) -> int:
    if a > b and a > c:
        return a
    if b > c:
        return b
    return c
