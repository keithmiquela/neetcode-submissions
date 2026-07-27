class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for char in s:
            if char in dictionary.values():
                stack.append(char)
            else:
                if len(stack) == 0 or stack[len(stack)-1]!=dictionary[char]:
                    return False
                else:
                    stack.pop(len(stack)-1)
        return False if stack else True