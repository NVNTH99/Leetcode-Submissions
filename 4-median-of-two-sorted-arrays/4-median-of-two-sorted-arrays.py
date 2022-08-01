class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        numlength=len(nums1)+len(nums2)
        j=0
        k=0
        nums=[]
        for i in range (0,numlength):
            if j>=len(nums1):
                nums.append(nums2[k])
                k=k+1
            elif k>=len(nums2):
                nums.append(nums1[j])
                j=j+1
            elif nums1[j]<=nums2[k]:
                nums.append(nums1[j])
                j=j+1
            elif nums1[j]>nums2[k]:
                nums.append(nums2[k])
                k=k+1
            
        if numlength%2==0:
            return (float(nums[numlength/2]+nums[(numlength/2)-1]))/2
        else:
            return nums[numlength/2]
            