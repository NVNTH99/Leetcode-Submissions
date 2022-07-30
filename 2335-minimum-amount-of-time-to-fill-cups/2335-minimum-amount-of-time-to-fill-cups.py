class Solution:
    def fillCups(self, amount: List[int]) -> int:
        k = 0
        l = len(amount)
        while l != 0:
            if 0 in amount:
                amount.remove(0)
                l = l - 1
                continue
            if l != 1:
                amount[amount.index(min(amount))] -= 1
                amount[amount.index(max(amount))] -= 1
                k += 1
            else:
                k += amount[0]
                amount[0] = 0
        return k
            