class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)[::-1]
        
        result = []
        def dfs(stack, total_sum, nums):
            if not nums:
                return
            for i in range(len(nums)):
                num = nums[i]
                temp = stack.copy()
                if total_sum + num < target:
                    temp.append(num)
                    dfs(temp, total_sum + num, nums[i:])
                if total_sum + num == target:
                    temp.append(num)
                    result.append(temp)
        dfs([], 0, nums)
        return result