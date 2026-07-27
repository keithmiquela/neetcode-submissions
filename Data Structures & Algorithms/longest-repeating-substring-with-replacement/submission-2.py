class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dictionary = { s[0]: 1 }

        max_length = 1
        i = 0 
        j = 1

        while j < len(s):
            if i == j:
                dictionary[s[i]] = 1
                j+=1
                continue
                
            curr = s[j]
            begin = s[i]
            total_count = j-i
            max_count = max(dictionary.values()) 
            if dictionary.get(curr) == max_count:
                dictionary[curr] +=1
                j+=1
                max_length = max(max_length, j-i)
                continue
            
            if total_count - max_count >= k:
                dictionary[begin] -= 1
                i+=1
            else:
                dictionary[curr] = dictionary[curr] + 1 if dictionary.get(curr) else 1
                j+=1
                max_length = max(max_length, j-i)

        max_length = max(max_length, j-i)

        return max_length
            