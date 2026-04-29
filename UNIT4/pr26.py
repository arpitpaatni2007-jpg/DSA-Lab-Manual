class HashTable:

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self._hash(key)

        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return

        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)

        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]

        return None

    def delete(self, key):
        index = self._hash(key)

        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                return True

        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"{i}: {bucket}")


ht = HashTable()

ht.insert(10, "A")
ht.insert(20, "B")
ht.insert(15, "C")  # collision example
ht.insert(25, "D")

print("Hash Table:")
ht.display()

print("\nGet 15:", ht.get(15))

ht.delete(20)
print("\nAfter deleting 20:")
ht.display()