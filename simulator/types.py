class Int8:
    def __init__(self, bits, signed=False):
        if len(bits) > 8:
            raise ValueError(f"Construction of int8 attempted with more than 8 bits, received {len(bits)} bits")

        self.bits = bits
        self.signed = signed

    @staticmethod
    def from_int(x: int):
        binary_representation = '{0:08b}'.format(x)

        bits = []
        signed = False

        if binary_representation[0] == "-":
            signed = True
            bits.append(True)
            binary_representation = binary_representation[1:]

        bits.extend([y == "1" for y in binary_representation])

        return Int8(bits, signed=signed)

    def __int__(self):
        out = 0

        bit_copy = self.bits

        if self.signed:
            signing_bit = bit_copy.pop(0)

        for bit in bit_copy:
            out = (out << 1) | bit

        if self.signed:
            if signing_bit:
                out *= -1

        return out