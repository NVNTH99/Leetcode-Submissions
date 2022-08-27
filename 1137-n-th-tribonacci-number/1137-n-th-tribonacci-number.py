class Solution:
    def tribonacci(self, n: int) -> int:
        nums = [0,1,1]
        if n < 3:
            return nums[n]
        for i in range(3,n+1):
            nums.append(nums[0] + nums[1] + nums[2])
            nums.pop(0)
        return nums[2]