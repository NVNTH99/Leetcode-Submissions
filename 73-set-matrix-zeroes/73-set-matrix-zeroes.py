class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rows = list()
        columns = list()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.append(i)
                    columns.append(j)
        for i in range(m):
            for j in range(n):
                if i in rows or j in columns:
                    matrix[i][j] = 0
