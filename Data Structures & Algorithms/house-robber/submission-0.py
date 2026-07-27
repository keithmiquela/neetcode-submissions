class Solution:
    def rob(self, nums: List[int]) -> int:
        house_count = len(nums)
        M = [0]*(house_count+1)
        M[1] = nums[0]
        if house_count == 1:
            return M[1]

        for i in range(2, house_count + 1):
            index = i-1
            M[i] = max(M[i-1], M[i-2]+ nums[index])
        return M[house_count]