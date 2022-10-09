class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0 for i in range(n+2)]
        arr[0] = 0
        arr[1] = 1
        for i in range(2,n+2):
            arr[i] = arr[i-1] + arr[i-2]
        return arr[n+1]