class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def split(low, high):
            if high<low:
                return -1
            mid = math.floor((high-low)/2 + low)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if target > nums[high] and nums[mid] < nums[low]:
                    return split(low, mid-1)
                else:
                    return split(mid+1, high)
            else:
                if nums[mid] > nums[high] and target < nums[low]:
                    return split(mid+1, high)
                else:
                    return split(low, mid-1)
                
        
        return split(0, len(nums)-1)
                        
                        