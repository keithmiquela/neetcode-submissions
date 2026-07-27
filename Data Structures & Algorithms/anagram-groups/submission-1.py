class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for string in strs:
            key = "".join(sorted(list(string)))
            if not dictionary.get(key):
                dictionary[key] = []
            dictionary.get(key).append(string)

        return list(dictionary.values())