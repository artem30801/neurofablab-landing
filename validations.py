def valid_size(x, maxsize: int) -> bool:
    return len(x) < maxsize


def valid_phonelike(x: str) -> bool:
    first = x[:2] == '+7'
    second = x[1:].isdigit()

    return first and second and len(x) == 12
