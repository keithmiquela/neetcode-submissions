class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        count_dict = {}

        for letter in letters:
            if letter in s1:
                count_dict[letter] = s1.count(letter)
        
        i = 0
        j = len(s1)

        while j <= len(s2):
            substring = s2[i:j]
            match = True
            for letter in count_dict.keys():
                if not letter in substring:
                    match = False
                    break;
                if substring.count(letter) != count_dict[letter]:
                    match = False
                    break;
            if match:
                return True
            i+=1
            j+=1

        return False
                
                