class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        store = {}
        max_length = 0

        while i < len(s):
            curr = s[i]
            if store.get(curr) == 1:
                while s[j]!=curr:
                    temp = s[j]
                    store[temp] -= 1
                    j+=1
                temp = s[j]
                store[temp] -= 1
                j+=1
            store[curr] = store.get(curr) + 1 if store.get(curr) else 1
            max_length = max(max_length, i-j+1)
            i+=1
        return max_length