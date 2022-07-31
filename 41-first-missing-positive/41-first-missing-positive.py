class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        nums = list(dict.fromkeys(nums))
        l = len(nums)
        k=1;
        for i in range(l):
            if nums[i]<=0:
                continue;
            if nums[i]!=k:
                break;
            k += 1
        return k