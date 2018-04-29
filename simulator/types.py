from enum import IntEnum


class BitInt:
    def __init__(self, value: int = 0, width: int = 8):
        # Truncate the value and un-sign it.
        value &= (1 << width) - 1

        self._value = value
        self._width = width

    def __repr__(self):
        width = self.width
        unsigned = self.unsigned
        signed = self.signed
        # This is the binary representation of the value.
        binary = f"{unsigned:0{width}b}"

        return f"<BitInt width={width} unsigned={unsigned} signed={signed} binary={binary}>"

    def __and__(self, other):
        width = max(self.width, other.width)
        result = self.unsigned & other.unsigned

        return BitInt(result, width)

    def __or__(self, other):
        width = max(self.width, other.width)
        result = self.unsigned | other.unsigned

        return BitInt(result, width)

    def __xor__(self, other):
        width = max(self.width, other.width)
        result = self.unsigned ^ other.unsigned

        return BitInt(result, width)

    # TODO: make sure the 8008 does actually use unsigned comparisons
    def __gt__(self, other):
        return self.unsigned > other.unsigned

    def __lt__(self, other):
        return self.unsigned < other.unsigned

    def __eq__(self, other):
        return self.unsigned == other.unsigned

    def __ge__(self, other):
        return self.unsigned >= other.unsigned

    def __le__(self, other):
        return self.unsigned <= other.unsigned

    def __ne__(self, other):
        return self.unsigned != other.unsigned

    def __lshift__(self, shift):
        res = self.unsigned << shift
        return BitInt(res, width=self.width)

    def __rshift__(self, shift):
        res = self.unsigned >> shift
        return BitInt(res, width=self.width)

    @property
    def unsigned(self) -> int:
        return self._value

    @property
    def signed(self) -> int:
        # The maximum integer this width can store.
        max_value = (1 << self._width) - 1

        # If our number is 'negative' (a.k.a. first binary digit is 1):
        if self._value > max_value >> 1:
            # Return the two's complement equivalent.
            return ~(max_value - self._value)

        # Otherwise, just return the value.
        return self._value

    @property
    def width(self) -> int:
        return self._width

    def rotate(self, amount):
        # Allow it to wrap, and work for negative (left) rotations
        amount %= self.width

        # Perform the actual rotation
        return self >> amount | self << self.width - amount


class Address:
    def __init__(self, high: BitInt, low: BitInt):
        self.high = high
        self.low = low

    @property
    def position(self):
        return self.high.unsigned, self.low.unsigned


class Flags(IntEnum):
    C = 0
    P = 1
    Z = 2
    N = 3
