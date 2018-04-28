from ..types import BitInt


class Memory:
    def __init__(self):
        # 16kB of cache on the 8008
        self._memory = [BitInt() for _ in range(16384)]

    def allocate(self, index: int, item: BitInt):
        self._memory[index] = item

    def deallocate(self, index: int):
        self._memory[index] = BitInt()

    def get(self, index: int) -> BitInt:
        return self._memory[index]
