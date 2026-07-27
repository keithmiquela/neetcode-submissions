class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def perm(stack, nums):
            if not nums:
                temp = stack.copy()
                result.append(temp)
                return
            for i in range(len(nums)):
                num = nums[i]
                temp1 = stack.copy()
                temp1.append(num)
                temp2 = nums.copy()
                temp2.pop(i)
                perm(temp1, temp2)
            
        perm([], nums)
        return result
                