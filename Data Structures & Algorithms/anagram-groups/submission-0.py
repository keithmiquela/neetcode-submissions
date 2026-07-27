class Solution:
    def is_anagram(self, string1: str, string2: str):
        if len(string1)!=len(string2):
            return False
        for char in string1:
            if string1.count(char)!= string2.count(char):
                return False
        return True
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        checked=[False]*len(strs)
        result=[]
        for i in range(0,len(strs)):
            temp=[]
            for j in range(i,len(strs)):
                if not checked[j] and len(strs[i])==len(strs[j]) and self.is_anagram(strs[i],strs[j]):
                    temp.append(strs[j])
                    checked[j]=True
            if temp:
                result.append(temp)
        return result