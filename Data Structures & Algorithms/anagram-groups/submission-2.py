class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        letters = list("abcdefghijklmnopqrstuvwxyz")
        for string in strs:
            key = str([[letter,string.count(letter)] for letter in letters])
            if not dictionary.get(key):
                dictionary[key] = []
            dictionary.get(key).append(string)

        return list(dictionary.values())