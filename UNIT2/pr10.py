class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def delete(self, value):
        temp = self.head

        if temp and temp.data == value:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != value:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        prev.next = temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


sll = SinglyLinkedList()

sll.insert_begin(10)
sll.insert_begin(5)
sll.insert_end(20)
sll.insert_end(30)

print("List:")
sll.traverse()

sll.delete(20)
print("After deleting 20:")
sll.traverse()

sll.delete(5)
print("After deleting 5:")
sll.traverse()