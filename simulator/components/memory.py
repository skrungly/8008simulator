from ..types import BitInt

class Memory:
	def __init__(self):
		self.memory = []

		for i in range(16384): #  16kB of cache on the 8008
			self.memory.append(BitInt(size=8))

	def insert(index: int, item: BitInt):
		self.memory[index] = item

	def deallocate(index: int):
		self.memory[index] = BitInt()

	def get(index: int) -> BitInt:
		return self.memory[index]