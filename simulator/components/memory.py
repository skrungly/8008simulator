from ..types import BitInt, Address


class Memory:
    def __init__(self):
        # 16kB of cache on the 8008
        self._memory = [[BitInt() for col in range(256)] for row in range(64)]

    def allocate(self, address: Address, item: BitInt):
        row, col = address.position
        self._memory[row][col] = item

    def deallocate(self, address: Address):
        row, col = address.position
        self._memory[row][col] = BitInt()

    def get(self, address: Address) -> BitInt:
        row, col = address.position
        return self._memory[row][col]
