class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for char in nums:
            if counter.get(char):
                return True
            counter[char]=1
        return False