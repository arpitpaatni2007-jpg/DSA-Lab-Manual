class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackSLL:

    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        val = self.top.data
        self.top = self.top.next
        return val

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None


def is_balanced(expr):
    stack = StackSLL()
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in expr:
        if ch in '([{':
            stack.push(ch)
        elif ch in ')]}':
            if stack.is_empty() or stack.pop() != pairs[ch]:
                return False

    return stack.is_empty()


tests = ["()", "()[]{}", "(]", "([)]", "{[()]}"]

for t in tests:
    print(f"{t} -> {is_balanced(t)}")