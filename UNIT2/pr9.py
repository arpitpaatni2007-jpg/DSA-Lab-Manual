class DynamicArray:

    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.arr = [None] * self.capacity

    def append(self, value):
        if self.size == self.capacity:
            self._resize()

        self.arr[self.size] = value
        self.size += 1
        self._print_state("append")

    def pop(self):
        if self.size == 0:
            print("Underflow!")
            return None

        value = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        self._print_state("pop")
        return value

    def _resize(self):
        self.capacity *= 2
        new_arr = [None] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def _print_state(self, op):
        print(f"{op.upper()} → size: {self.size}, capacity: {self.capacity}, array: {self.arr[:self.size]}")


da = DynamicArray()

da.append(10)
da.append(20)
da.append(30)
da.append(40)

da.pop()
da.pop()