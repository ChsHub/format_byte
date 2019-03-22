from math import log


def format_bit(nr):
    return format_byte(nr / 8)


_unit = ["B", "kiB", "MiB", "GiB", "TiB", "EiB", "ZiB", "YiB"]
def format_byte(nr, precision: int = 2):
    exponent = int(log(nr, 1024))
    exponent = min(exponent, len(_unit) - 1)
    return str(round(nr / pow(1024, exponent), precision)) + _unit[exponent]
