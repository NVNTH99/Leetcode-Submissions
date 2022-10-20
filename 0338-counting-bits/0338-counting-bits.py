class Solution:
    def countBits(self, n: int) -> List[int]:
        result = list()
        num = 2
        nextnum = 4
        for i in range(n + 1):
            if i == 0 or i == 1:
                result.append(i)
                continue
            if nextnum == i*2:
                num *= 2
                nextnum *= 2
            result.append(result[i-num]+1)
        return result