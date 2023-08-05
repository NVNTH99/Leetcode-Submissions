#User function Template for python3
import heapq
class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        l = []
        heapq.heapify(l)
        for i in range(n):
            heapq.heappush(l,(end[i],start[i]))
        prevend = -1
        count = 0
        while l:
            val = heapq.heappop(l)
            if val[1]>prevend:
                prevend = val[0]
                count += 1
        return count
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends