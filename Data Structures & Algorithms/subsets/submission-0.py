class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        limit = len(nums)
        # input: stack
        # add answer to result
        def dfs(stack, index):
            copy = stack.copy()
            if index >= limit:
                result.append(stack)
                return
            copy.append(nums[index])

            dfs(stack,index+1)
            dfs(copy,index+1)
        dfs([],0)
            
        return result