class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:

    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return root

    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:
            # Case 1: No child
            if root.left is None and root.right is None:
                return None

            # Case 2: One child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3: Two children
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)


bst = BST()
root = None

keys = [50, 30, 70, 20, 40, 60, 80]

for key in keys:
    root = bst.insert(root, key)

print("Original tree (inorder):")
bst.inorder(root)

# Delete leaf
root = bst.delete(root, 20)
print("\nAfter deleting 20:")
bst.inorder(root)

# Delete node with one child
root = bst.delete(root, 30)
print("\nAfter deleting 30:")
bst.inorder(root)

# Delete node with two children
root = bst.delete(root, 50)
print("\nAfter deleting 50:")
bst.inorder(root)