class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def check2(result,nums,per=[]):
            if not len(nums):
                result.append(per)
                return
            for i in nums:
                temp = nums.copy()
                temp.remove(i)
                check2(result,temp,per + [i])
                
        result = list()
        check2(result,nums)
        return result