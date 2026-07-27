class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def findCycle(i,j):
            i=nums[i]
            j=nums[nums[j]]
            while i!=j:
                i=nums[i]
                j=nums[nums[j]]
            return j

        def floydAlgo(i, j):
            while i!=j:
                i=nums[i]
                j=nums[j]
            return j
        i=0
        j=findCycle(0, 0)
        return floydAlgo(i,j)