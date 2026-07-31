class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = 0
        if nums[len(nums)-1] < nums[0]:
            i = 0
            j = len(nums) - 1
            while i <= j:
                mid = (i+j)//2
                
                if nums[mid] > nums[mid+1]:
                    pivot = mid + 1
                    break
                elif nums[mid] < nums[j]:
                    j = mid
                else:
                    i = mid + 1
        
        # pivot = number of rotations

        i = 0
        j = len(nums)-1

        while i <= j:
            mid = (i+j)//2

            rot_mid = (mid+pivot)%len(nums)
            rot_i = (i+pivot)%len(nums)
            rot_j = (j+pivot)%len(nums)
            
            if nums[rot_mid] == target:
                return rot_mid
            elif nums[rot_mid] > target:
                j = mid - 1
            else:
                i = mid + 1

        return -1