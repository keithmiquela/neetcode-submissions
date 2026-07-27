from collections import deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case: len_t > len_s
        if len(t) > len(s):
            return ""

        # sliding window
        # grows if doesn't contain t
        # shrinks if it does
        # uses hashmap to keep count
        # if all t in s, record count
        # if not, grow

        # initialize hashmaps
        count_t = {}
        count_s = {}

        # populate count_t
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for letter in letters:
            count_t[letter] = 0
            count_s[letter] = 0

        for letter in t:
            count_t[letter] += 1

        # declare return val
        min_len = -1
        queue_substring = deque()
        min_substring = ""

        # initialize pointers
        i = 0
        j = 0

        # helper: isContained() -- check if t is contained is substring
        def isContained():
            for letter in letters:
                if count_t[letter] > count_s[letter]:
                    return False
            return True
            
        # algorithm loop
        while j < len(s):
            # add j
            letter_j = s[j]
            queue_substring.append(letter_j)
            count_s[letter_j] += 1
            j+=1

            # if letters are contained
            # for each letter in T, count_t <= count_s
            # if possible, shrink and recalculate
            while isContained():
                if min_len == -1 or j - i <= min_len:
                    min_len = j-i
                    min_substring = "".join(queue_substring)
        
                # i moves forward
                letter_i = s[i]
                queue_substring.popleft()
                count_s[letter_i]-=1
                i += 1

        # return min val
        return min_substring

