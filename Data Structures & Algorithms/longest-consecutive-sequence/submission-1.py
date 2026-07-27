class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = {}
        for num in nums:
            lookup[num] = 1
        count = 0
        max_count = 0
        for num in nums:
            if lookup.get(num-1):
                continue
            
            temp = num
            while lookup.get(temp):
                count+=1
                temp+=1
            max_count = max(count, max_count)
            count = 0

        return max_count