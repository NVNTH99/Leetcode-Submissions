#User function Template for python3
import heapq
class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        l = []
        heapq.heapify(l)
        for i in Jobs:
            heapq.heappush(l,(i.deadline,-1*i.profit))
        time = 0
        profit = []
        count = 0
        while l:
            val = heapq.heappop(l)
            if time>=val[0]:
                if profit and -1*val[1] > profit[0]:
                    heapq.heappop(profit)
                    heapq.heappush(profit,-1*val[1])
            else:
                heapq.heappush(profit,-1*val[1])
                count += 1
                time += 1
        total = 0
        while profit:
            total += heapq.heappop(profit)
        return [count,total]
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends