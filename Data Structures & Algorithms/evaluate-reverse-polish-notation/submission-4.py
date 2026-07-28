class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = "+-*/"
        for token in tokens:
            if token in operands:
                b = stack.pop()
                if token == "+":
                    stack[-1]+=b
                elif token == "-":
                    stack[-1]-=b
                elif token == "*":
                    stack[-1]*=b
                else:
                    stack[-1] = int(stack[-1]/b)
            else:
                stack.append(int(token))
        return stack[-1]