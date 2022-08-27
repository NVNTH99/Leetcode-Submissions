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
            rows.append(0)
        for i in range(n):
            columns.append(0)
        i = 0
        j = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = 1
                    columns[j] = 1
        for i in range(m):
            for j in range(n):
                if rows[i] == 1 or columns[j] == 1:
                    matrix[i][j] = 0
                
