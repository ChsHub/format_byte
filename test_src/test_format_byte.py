from format_byte import format_byte, format_bit
from hypothesis import given
from hypothesis._strategies import floats, integers


@given(floats(allow_nan=False, allow_infinity=False))
def test_format_bit(nr):
    assert format_bit(nr)


@given(floats(allow_nan=False, allow_infinity=False), integers())
def test_format_byte(nr, precision):
    assert format_byte(nr, precision)

@given(integers(), integers())
def test_format_byte2(nr, precision):
    assert format_byte(nr, precision)

if __name__ == "__main__":
    test_format_bit()
    test_format_byte()
    test_format_byte2()