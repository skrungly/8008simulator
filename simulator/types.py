class BitInt:
    def __init__(self, bits=None, size=8, signed=False):
        if bits is None:
            bits = []

        if len(bits) > size:
            raise ValueError(f"Construction of BitInt attempted with more than {size} bits, received {len(bits)} bits.")

        padding = [False for _ in range(size - len(bits))]
        self.bits = padding + bits
        self.signed = signed

    @staticmethod
    def from_int(value: int):
        binary = '{0:08b}'.format(value)

        bits = []
        signed = False

        if binary[0] == "-":
            signed = True
            bits.append(True)
            binary = binary[1:]

        bits.extend([bit == "1" for bit in binary])

        return BitInt(bits, signed=signed)

    def __int__(self):
        out = 0

        bit_copy = self.bits.copy()

        if self.signed:
            signing_bit = bit_copy.pop(0)

        for bit in bit_copy:
            out = (out << 1) | bit

        if self.signed:
            if signing_bit:
                out *= -1

        return out
