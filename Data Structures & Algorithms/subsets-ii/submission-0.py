class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        def findSubset(stack, nums):
            if not nums:
                temp = stack.copy()
                if temp not in result:
                    result.append(stack)
                return
            temp1 = stack.copy()
            temp2 = stack.copy()
            temp2.append(nums[0])
            findSubset(temp1, nums[1:])
            findSubset(temp2, nums[1:])
        findSubset([], nums)
        return result
            
