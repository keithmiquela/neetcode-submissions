class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = "([{"
        close_brackets = ")]}"
        close_to_open = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        stack = []
        
        for char in s:
            if char not in open_brackets and char not in close_brackets:
                return False
            elif char in open_brackets:
                stack.append(char)
            else:
                if not stack or close_to_open.get(char) != stack[-1]:
                    return False
                stack.pop()
            
        return len(stack) == 0


