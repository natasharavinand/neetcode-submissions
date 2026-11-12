class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        targetRowIdx = -1

        # Do binary search on the matrix's columns to find target row
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                top = mid + 1
            else:
                bottom = mid - 1
        
        targetRowIdx = bottom

        # Do binary search on the target row
        left = 0
        right = len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[targetRowIdx][mid] == target:
                return True
            elif matrix[targetRowIdx][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
        
        
        
        