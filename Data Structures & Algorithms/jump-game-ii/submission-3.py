class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        i = 0
        j = nums[0]
        maxJump = nums[0]
        jumps = 0
        while i < len(nums):
            while i <= j:
                if i >= len(nums):
                    break
                maxJump = max(maxJump, nums[i]+i)
                i+=1
            jumps+=1
            j = maxJump
        return jumps