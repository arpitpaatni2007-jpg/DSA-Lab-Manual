class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print('Underflow! Stack is empty.')
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            print('Stack is empty.')
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        print('Stack (top -> bottom):', self.items[::-1])


s = Stack()

word = 'HELLO'
for ch in word:
    s.push(ch)

reversed_word = ''
while not s.is_empty():
    reversed_word += s.pop()

print('Original:', word)
print('Reversed:', reversed_word)


s2 = Stack()

s2.push(10)
s2.push(20)
s2.push(30)

s2.display()

print('Peek:', s2.peek())
print('Pop:', s2.pop())

s2.display()

s2.pop()
s2.pop()
s2.pop()