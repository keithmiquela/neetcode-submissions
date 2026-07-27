class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case, can't contain s1
        if len(s2) < len(s1):
            return False
        
        # init count hashmaps
        count1 = {}
        count2 = {}
        pop_letters = "abcdefghijklmnopqrstuvwxyz"
        for letter in pop_letters:
            count1[letter] = 0
            count2[letter] = 0
        
        def compareCounts():
            return count1 == count2

        # init count1 with real values
        for letter in s1:
            count1[letter] += 1

        # pointers
        i = 0
        j = len(s1) - 1

        # add values to count2
        for letter in s2[i:j]:
            count2[letter] += 1
        
        # algorithm loop
        while j < len(s2):

            letter_j = s2[j]
            count2[letter_j]+=1

            if compareCounts():
                return True
            
            letter_i = s2[i]
            count2[letter_i]-=1
            i+=1

            j+=1
        return False

        