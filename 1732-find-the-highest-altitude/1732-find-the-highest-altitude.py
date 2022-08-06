class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum = 0
        m = 0
        for i in gain:
            sum += i
            if sum>m:
                m = sum
        return m