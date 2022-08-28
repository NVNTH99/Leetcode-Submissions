class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        maximum = 0
        for i in range(l):
            if i <= maximum and i+nums[i]>maximum:
                maximum = i + nums[i]
        if maximum >= l - 1:
            return True
        return False