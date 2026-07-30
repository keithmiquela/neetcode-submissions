class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        i = 0
        j = (rows * cols) - 1

        while i <= j:
            mid = (i + j)//2

            mid_row = mid // cols
            mid_col = mid % cols

            mid_num = matrix[mid_row][mid_col]

            if mid_num == target:
                return True
            elif mid_num < target:
                i = mid + 1
            else:
                j = mid - 1
        return False