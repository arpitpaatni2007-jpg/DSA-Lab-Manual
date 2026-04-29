class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.end = True

    def search(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return node.end

    def startsWith(self, prefix):
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return True


trie = Trie()

words = ["apple", "app", "bat", "ball"]

for w in words:
    trie.insert(w)

print("Search 'app':", trie.search("app"))
print("Search 'bat':", trie.search("bat"))
print("Search 'bad':", trie.search("bad"))

print("Prefix 'ap':", trie.startsWith("ap"))
print("Prefix 'ba':", trie.startsWith("ba"))
print("Prefix 'ca':", trie.startsWith("ca"))