class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                curr_sum = nums[i] + nums[j]
                target = -curr_sum
                if target in nums[j+1:len(nums)]:
                    triplet = [nums[i], nums[j], target]
                    if sorted(triplet) in result:
                        continue
                    result.append(sorted(triplet))

        return result