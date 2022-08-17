class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def check2(result,nums,per=[]):
            if not len(nums):
                if per not in result:
                    result.append(per)
                return
            l = len(nums)
            for i in range(l):
                temp = nums.copy()
                r = temp.pop(i)
                check2(result,temp,per + [r])
                
        result = list()
        check2(result,nums)
        return result