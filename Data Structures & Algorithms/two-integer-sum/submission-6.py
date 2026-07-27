class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dictionary = {}
        for i in range(0,len(nums)):
            num = nums[i]
            if dictionary.get(target-num) != None:
                j = dictionary.get(target-num)
                return [j,i]
            
            dictionary[num] = i

        return None