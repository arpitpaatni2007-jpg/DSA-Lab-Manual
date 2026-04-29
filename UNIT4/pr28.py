class BloomFilter:

    def __init__(self, size):
        self.size = size
        self.bit_array = [0] * size

    def _hash1(self, item):
        return hash(item) % self.size

    def _hash2(self, item):
        return (hash(item) * 7) % self.size

    def add(self, item):
        index1 = self._hash1(item)
        index2 = self._hash2(item)

        self.bit_array[index1] = 1
        self.bit_array[index2] = 1

    def check(self, item):
        index1 = self._hash1(item)
        index2 = self._hash2(item)

        if self.bit_array[index1] == 1 and self.bit_array[index2] == 1:
            return "Possibly Present"
        else:
            return "Definitely Not Present"


bf = BloomFilter(10)

items = ["apple", "banana", "grape"]

for item in items:
    bf.add(item)

print("Checking items:")

test_items = ["apple", "banana", "cherry", "mango"]

for item in test_items:
    print(item, "->", bf.check(item))