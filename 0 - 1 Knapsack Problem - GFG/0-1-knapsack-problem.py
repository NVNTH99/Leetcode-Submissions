#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        result = [[0 for i in range(W+1)] for i in range(n+1)]
        for i in range(n):
            for j in range(0,W+1):
                taken = 0
                if j>=wt[i]:
                    taken = val[i] + result[i][j-wt[i]]
                result[i+1][j] = max(0+result[i][j],taken)
        # print(result)
        return result[n][W]
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends