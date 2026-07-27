class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for string in strs:
            char_count = [0]*26
            for char in string:
                char_count[ord(char)-ord('a')]+=1
            key = tuple(char_count)

            if not dictionary.get(key):
                dictionary[key]= []
            dictionary[key].append(string)

        return list(dictionary.values())