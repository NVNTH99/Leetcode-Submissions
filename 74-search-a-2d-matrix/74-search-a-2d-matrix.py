class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        beg = 0
        end = len(matrix) - 1
        while end > beg:
            mid = math.ceil((beg + end) / 2)
            if target >= matrix[mid][0]:
                beg = mid
            else:
                end = mid - 1
        temp = beg
        end = len(matrix[beg]) - 1
        beg = 0
        while end >= beg:
            mid = (beg + end) // 2
            if target == matrix[temp][mid]:
                return True
            elif target > matrix[temp][mid]:
                beg = mid + 1
            else:
                end = mid - 1
        return False
        