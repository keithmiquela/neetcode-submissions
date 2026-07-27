class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp=sorted(nums)
        i=0
        j=len(temp)-1
        while temp[i]+temp[j]!=target:
            if temp[i]+temp[j]<target:
                i+=1
            else:
                j-=1
        return [min(nums.index(temp[i]),nums.index(temp[j]) if nums.index(temp[i])!=nums.index(temp[j]) else nums.index(temp[j],nums.index(temp[i])+1)),max(nums.index(temp[i]),nums.index(temp[j]) if nums.index(temp[i])!=nums.index(temp[j]) else nums.index(temp[j],nums.index(temp[i])+1))]