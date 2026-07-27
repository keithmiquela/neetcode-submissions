class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        high_index = len(matrix)*len(matrix[0])-1

        def split(low, high):
            
            if high < low:
                return False
            mid = math.floor((high-low)/2 + low)
            
            row = math.floor(mid/len(matrix[0]))
            col = mid % len(matrix[0])
            mid_num = matrix[row][col]
            if mid_num == target:
                return True
            elif mid_num < target:
                return split(mid+1, high)
            else:
                return split(low, mid-1)
        
        return split(0,high_index)