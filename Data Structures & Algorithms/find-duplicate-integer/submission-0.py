class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(1, 10001):
            if nums.count(i)>1:
                return i