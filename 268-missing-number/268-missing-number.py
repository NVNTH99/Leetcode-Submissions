class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        for i in range(l):
            if i != nums[i]:
                return i
        return l