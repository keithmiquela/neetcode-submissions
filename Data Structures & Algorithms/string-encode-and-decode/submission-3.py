class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ''
        for string in strs:
            code += "$"
            code += str(len(string))
            code += "$"
            code += string
        return code

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i+2
            while s[j] != "$":
                j+=1
                if j == len(s):
                    return [s]
            length = int(s[i+1:j])
            j+=1
            result.append(s[j:j+length])
            i = j+length
        
        return result