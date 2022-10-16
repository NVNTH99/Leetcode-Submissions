class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        for i in range(n, 0, -1):
            fact *= i
        a = n
        nums = list()
        num = ""
        for i in range(1, n + 1):
            nums.append(i)
        while a != 0:
            fact = fact / a
            a -= 1
            num += str(nums.pop(math.ceil(k / fact) - 1))
            k = k % fact
            if k == 0:
                k += fact
        return num