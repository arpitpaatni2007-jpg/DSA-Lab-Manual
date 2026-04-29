class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueSLL:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Underflow! Queue is empty.")
            return None

        val = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return val

    def peek(self):
        if self.front is None:
            return None
        return self.front.data

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" <- ")
            temp = temp.next
        print("None")


q = QueueSLL()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Queue:")
q.display()

print("Dequeue:", q.dequeue())
print("Front:", q.peek())

q.display()

q.dequeue()
q.dequeue()
q.dequeue()