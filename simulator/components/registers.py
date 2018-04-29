from ..types import BitInt, Flags


class StatusFlags:

    def __init__(self):
        self.flags = [False, False, False, False]

    @property
    def carry(self):
        return self.flags[Flags.C]

    @property
    def parity(self):
        return self.flags[Flags.P]

    @property
    def zero(self):
        return self.flags[Flags.Z]

    @property
    def negative(self):
        return self.flags[Flags.N]


class Registers:
    def __init__(self):
        self.accumulator = BitInt()
        self.register_b = BitInt()
        self.register_c = BitInt()
        self.register_d = BitInt()
        self.register_e = BitInt()
        self.register_h = BitInt()
        self.register_l = BitInt()

        self.program_counter = BitInt(width=14)
        self.address_stack = [BitInt(width=14) for _ in range(7)]

        self.status_flags = StatusFlags()

    def push_address(self, address: BitInt):
        """Push down the address call stack and update the program counter."""
        self.address_stack.insert(0, self.program_counter)
        self.address_stack.pop()

        self.program_counter = address
