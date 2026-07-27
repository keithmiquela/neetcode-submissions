class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}
        for char in s:
            if s_count.get(char):
                s_count[char]+=1
            else:
                s_count[char]=1

        for char in t:
            if t_count.get(char):
                t_count[char]+=1
            else:
                t_count[char]=1
        
        for key in s_count.keys():
            if s_count.get(key) != t_count.get(key):
                return False
        
        return True
