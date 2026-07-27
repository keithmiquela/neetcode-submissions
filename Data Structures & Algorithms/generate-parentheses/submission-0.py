class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def dfs(openN, closedN):
            
            if openN == closedN == n:
                result.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                dfs(openN+1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                dfs(openN, closedN + 1)
                stack.pop()
        dfs(0,0)
        return result
            
                
            


        