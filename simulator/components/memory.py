from ..types import BitInt


class Memory:
    def __init__(self):
        # 16kB of cache on the 8008
        self._memory = [[BitInt() for y in range(256)] for x in range(64)]

    def allocate(self, row: int, col: int, item: BitInt):
        self._memory[row][col] = item

    def deallocate(self, row: int, col: int):
        self._memory[row][col] = BitInt()

    def get(self, row: int, col: int) -> BitInt:
        return self._memory[row][col]
