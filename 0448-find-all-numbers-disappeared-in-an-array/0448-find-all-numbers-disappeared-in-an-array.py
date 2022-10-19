class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            j = abs(i)
            if nums[j-1]>0:
                nums[j-1] *= -1
        l = len(nums)
        for i in range (l-1,-1,-1):
            if nums[i]<0:
                nums.pop(i)
            else:
                nums[i] = i+1
        return nums