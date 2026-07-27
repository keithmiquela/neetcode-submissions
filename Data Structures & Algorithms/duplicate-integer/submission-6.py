class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            if count.get(num):
                return True
            else:
                count[num]=1

        return False