class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if not len(s):
            return 0

        count = {}
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        # initialize the count hashmap
        for letter in letters:
            count[letter] = 0

        # pointers + return var
        i = 0
        j = 0
        max_len = 0

        def returnFreqCount():
            freq_count = 0
            for letter in letters:
                freq_count = max(freq_count, count.get(letter))
            return freq_count

        # algorithm loop
        while j < len(s):
            letter_j = s[j]
            count[letter_j]+=1

            j+=1
            curr_len = j-i
            freq_count = returnFreqCount()
            change_count = curr_len - freq_count

            # make substring smaller if needed
            while change_count > k:
                letter_i = s[i]
                count[letter_i]-=1
                i+=1

                curr_len = j-i
                freq_count = returnFreqCount()
                change_count = curr_len - freq_count
                
                
            max_len = max(max_len, curr_len)

        return max_len