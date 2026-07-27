class Node:
    def __init__(self, val = 0, branches = None, end=False):
        self.val = val
        self.branches = branches if branches else {}
        self.end = end

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            branches = curr.branches
            if char in branches:
                curr = branches.get(char)
                continue
            branches[char] = Node(char)
            curr = branches.get(char)
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(node, string):
            if not string and node.end:
                return True
            if not string:
                return False
            char = string[0]
            branches = node.branches
            if char == '.':
                for node in branches.values():
                    if dfs(node, string[1:]):
                        return True

                return False
            if char in branches:
                return dfs(branches.get(char),string[1:])
            return False
        return dfs(self.root, word)
