class Node:
    def __init__(self, val = ""):
        self.val = val
        self.next = {}
        self.end = False


class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if curr.next.get(char):
                curr = curr.next[char]
                continue
            
            new_node = Node(char)
            curr.next[char] = new_node
            curr = new_node
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if curr.next.get(char):
                curr = curr.next[char]
                continue
            return False
        
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if curr.next.get(char):
                curr = curr.next[char]
                continue
            return False
        
        return True
        