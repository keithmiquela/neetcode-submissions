class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        checked=[]
        result=[]
        i=0
        j=1
        while i <len(nums)-1:
            if nums[i] not in checked:
                j_checked=[]
                while j<len(nums):
                    if nums[j] not in j_checked:
                        if -nums[i]-nums[j] in nums[j+1:len(nums)]:
                            result.append([nums[i],nums[j],-nums[i]-nums[j]])
                        j_checked.append(nums[j])
                    j+=1
                checked.append(nums[i])
            i+=1
            j=i+1
        return result

        