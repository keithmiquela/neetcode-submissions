class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[],[nums[0]]]
        mid = (int)(len(nums)/2)
        left = self.subsets(nums[0:mid])
        right = self.subsets(nums[mid:len(nums)])
        result = []
        for set_i in left:
            for set_j in right:
                result.append(set_i+set_j)
        return result