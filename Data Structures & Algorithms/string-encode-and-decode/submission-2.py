
class Solution:
    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "#"
        result=""
        for string in strs:
            result += str(len(string))+"#"+string
        return result

    def decode(self, s: str) -> List[str]:
        if s == "#":
            return []
        temp_array=[]
        i=0
        j=0
        while i<len(s):
            while s[j]!="#":
                j+=1
            temp=int(s[i:j])
            temp_array.append(s[j+1:j+1+temp])
            i=j+1+temp
            j=i
        return temp_array
            
