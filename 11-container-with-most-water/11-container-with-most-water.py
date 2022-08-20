class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maximum = 0
        while i < j:
            volume = min(height[i], height[j]) * (j - i)
            if volume > maximum:
                maximum = volume
            if height[i]<height[j]:
                i += 1
            else:
                j -= 1
        return maximum