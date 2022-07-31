class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
        for i in range(n):
            for j in range((n-1)//2+1):
                temp = matrix[i][j]
                matrix[i][j]=matrix[i][n-j-1]
                matrix[i][n-j-1]=temp
            