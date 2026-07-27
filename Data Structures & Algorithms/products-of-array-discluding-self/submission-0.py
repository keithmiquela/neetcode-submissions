class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes=[1]*len(nums)
        suffixes=[1]*len(nums)
        for i in range(0,len(nums)-1):
            prefixes[i+1]=nums[i]*prefixes[i]
        for i in range(len(nums)-1,0,-1):
            suffixes[i-1]=nums[i]*suffixes[i]
        products=[1]*len(nums)
        for i in range(0,len(nums)):
            products[i]=prefixes[i]*suffixes[i]
        return products