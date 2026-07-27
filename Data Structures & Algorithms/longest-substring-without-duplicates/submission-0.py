class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        i = 0
        j = 1
        max_length = 1
        while j < len(s):
            substring = s[i:j]
            if s[j] in substring:
                i+=1
            else:
                j+=1
                max_length = max(max_length, j-i)
        max_length = max(max_length, j-i)
        return max_length