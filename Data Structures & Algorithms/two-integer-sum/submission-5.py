class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums = sorted([[num, i] for i,num in enumerate(nums)])

        i = 0
        j = len(nums)-1
        while j>i:
            if nums[j][0]+nums[i][0]<target:
                i+=1
                continue
            if nums[j][0]+nums[i][0]>target:
                j-=1
                continue
            
            break

        return [min(nums[i][1],nums[j][1]),max(nums[i][1],nums[j][1])]