class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted([[nums[i],i] for i in range(len(nums))])
        i = 0
        j = len(nums)-1
        while i<j:
            a = nums[i]
            b = nums[j]
            if a[0] + b[0] < target:
                i+=1
            elif a[0] + b[0] > target:
                j-=1
            else:
                return [min(a[1],b[1]), max(a[1],b[1])]
        return -1