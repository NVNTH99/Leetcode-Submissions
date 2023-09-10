#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        sum = 0
        maxlen = 0
        d = dict()
        for i in range(n):
            sum += arr[i]
            # print(i,sum)
            if sum == 0:
                maxlen = i + 1
            elif sum in d:
                maxlen = max(maxlen,i-d[sum])
            else:
                d[sum] = i
        return maxlen


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends