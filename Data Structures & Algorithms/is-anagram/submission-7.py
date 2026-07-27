import string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = list(string.ascii_lowercase)

        for char in letters:
            if s.count(char)!=t.count(char):
                return False
        return True