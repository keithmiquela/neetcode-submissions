class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        for i in range(len(nums)):
            num = nums[i]
            if num == target:
                result.append([num])
            if num < target:
                new_target = target-num
                new_list = self.combinationSum(nums[i:len(nums)], new_target)
                for new_nums in new_list:
                    result.append([num]+new_nums)
        return result
            