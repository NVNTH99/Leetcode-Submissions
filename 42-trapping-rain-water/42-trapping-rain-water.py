class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = 0
        rightmax = 0
        left = 0
        water= 0
        right = len(height) - 1
        while left <= right:
            if rightmax < leftmax:
                
                if height[right] < rightmax:
                    water += rightmax - height[right]
                else:
                    rightmax = height[right]
                right -= 1
            else:
                if height[left] > leftmax:
                    leftmax = height[left]
                else:
                    water += leftmax - height[left]
                left += 1
        return water