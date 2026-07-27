class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        house_count = len(nums) - 1
        left = [0] * (house_count + 1)
        right = [0] * (house_count + 1)
        
        left[1] = nums[0]
        right[1] = nums[1]

        for i in range(2, house_count+1):
            left[i] = max(left[i-1], left[i-2] + nums[i-1])
            right[i] = max(right[i-1], right[i-2]+nums[i])

        return max(left[house_count], right[house_count]) 