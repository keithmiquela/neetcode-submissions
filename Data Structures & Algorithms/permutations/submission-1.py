class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [[nums[0]]]
        results = []
        for i in range(len(nums)):
            num = nums[i]
            temp = nums[0:i]+nums[i+1:len(nums)]
            result = self.permute(temp)
            for tempArray in result:
                results.append([num]+tempArray)
        return results