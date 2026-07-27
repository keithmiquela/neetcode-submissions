class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def split(low,high):
            if high == low:
                return nums[high]
            mid = math.ceil((high-low)/2 + low)

            if nums[mid] > nums[high]:
                return split(mid+1, high)
            else:
                if nums[high] > nums[low]:
                    return nums[low]
                else:
                    return split(low+1, mid)
            
        return split(0, len(nums)-1)

