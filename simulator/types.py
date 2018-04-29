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


class Flags(IntEnum):
    C = "carry"
    P = "parity"
    Z = "zero"
    N = "negative"
