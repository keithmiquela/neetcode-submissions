class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        i = 0
        j = len(nums) - 1 
        
        while i <= j:
            if nums[i] == nums[j]:
                return nums[i]

            mid = (i+j)//2
            
            if nums[mid]>nums[j]:
                i = mid + 1
            else:
                j = mid