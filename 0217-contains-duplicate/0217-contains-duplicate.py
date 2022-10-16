class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        l = len(nums)
        prev = nums[0]
        for i in range(1,l):
            if prev == nums[i]:
                return True
            prev = nums[i]
        return False