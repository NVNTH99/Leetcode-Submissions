class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        done = set()
        l = len(nums)
        list1 = list()
        for i in range(l):
            if nums[i] > 0:
                break
            if nums[i] in done:
                continue
            j = i + 1
            k = l - 1
            done.add(nums[i])
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j = j + 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k = k - 1
                else:
                    if [nums[i], nums[j], nums[k]] not in list1:
                        list1.append([nums[i], nums[j], nums[k]])
                    j = j + 1
        return list1