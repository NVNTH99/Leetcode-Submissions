class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:           
        l = len(arr)
        visit = list()
        for i in range(l):
            visit.append(0)
        nums = list()
        nums.append(start)
        while arr[nums[0]] != 0:
            i = nums[0] + arr[nums[0]]
            j = nums[0] - arr[nums[0]]
            visit[nums[0]] = 1
            if i < l and visit[i] == 1 and j > -1 and visit[j] == 1:
                return False
            if i < l and visit[i] == 0:
                nums.append(i)
            if j > -1 and visit[j] == 0:
                nums.append(j)
            nums.pop(0)
            if not nums:
                return False
        return True
            