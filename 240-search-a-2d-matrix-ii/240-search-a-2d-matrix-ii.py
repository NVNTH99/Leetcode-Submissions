class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = len(matrix[0])
        for i in matrix:
            end = l - 1
            beg = 0
            while end >= beg:
                mid = (beg + end) // 2
                if target == i[mid]:
                    return True
                elif target > i[mid]:
                    beg = mid + 1
                else:
                    end = mid - 1
        return False