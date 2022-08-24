class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def comb(total, count):
            numerator = 1
            for i in range(total, total - count, -1):
                numerator *= i
                total - 1
            denominator = 1
            for i in range(count, 0, -1):
                denominator *= i
            return numerator // denominator
        
        total = m + n - 2
        count = min(m - 1, n - 1)
        return comb(total, count)