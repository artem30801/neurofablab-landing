def valid_size(x: str, maxsize: int) -> bool:
    return 0 < len(x) < maxsize


def valid_phonelike(x: str) -> bool:
    first = x[:2] == '+7'
    second = x[1:].isdigit()

    return first and second and len(x) == 12

#print(valid_size("", 10))