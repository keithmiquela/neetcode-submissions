class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        strs = [[''.join(sorted(string)),string] for string in strs]
        for string in strs:
            if group.get(string[0]):
                group.get(string[0]).append(string[1])
            else:
                group[string[0]]=[string[1]]
        
        return list(group.values())