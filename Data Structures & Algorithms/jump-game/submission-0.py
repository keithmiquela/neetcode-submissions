class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lim = nums[0]
        for i in range(1, len(nums)):
            if i > lim:
                return False
            lim = max(lim, nums[i]+i)
        return True