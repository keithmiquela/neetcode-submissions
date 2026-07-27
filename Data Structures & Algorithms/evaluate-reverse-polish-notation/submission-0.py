class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+","-","*","/"]
        for token in tokens:
            if token in operations:
                y=stack.pop()
                x=stack.pop()
                if token == "+":
                    stack.append(x+y)
                elif token == "-":
                    stack.append(x-y)
                elif token == "*":
                    stack.append(x*y)
                else:
                    stack.append(int(x/y))
            else:
                stack.append(int(token))
        return stack.pop()