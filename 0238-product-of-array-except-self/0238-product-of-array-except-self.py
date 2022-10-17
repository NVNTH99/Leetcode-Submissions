class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        products = [1 for i in range(l)]
        pro = 1
        for i in range(l):
            products[i] *= pro
            pro *= nums[i]
        pro = 1
        for i in range(l-1,-1,-1):
            products[i] *= pro
            pro *= nums[i]
        return products