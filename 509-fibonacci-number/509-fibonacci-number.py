class Solution:
    def fib(self, n: int) -> int:
        nums = [0,1]
        if n < 2:
            return nums[n]
        for i in range(2,n+1):
            nums.append(nums[0] + nums[1])
            nums.pop(0)
        return nums[1]