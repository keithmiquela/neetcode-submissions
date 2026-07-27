class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currMax = nums[0]
        currSum = nums[0]

        for i in range(1,len(nums)):
            if currSum < 0:
                currSum = nums[i]
            else:
                currSum += nums[i]
            currMax = max(currMax, currSum)
        return currMax