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

    def search(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

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

print("Inorder traversal (sorted):")
bst.inorder(root)

print("\nSearch 60:", "Found" if bst.search(root, 60) else "Not Found")
print("Search 25:", "Found" if bst.search(root, 25) else "Not Found")