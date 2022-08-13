class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check2(s, i, j,ptable):
            if ptable[i][j] == 1:
                return True
            if ptable[i][j] is None and check2(s, i + 1, j - 1,ptable) and s[i] == s[j]:
                ptable[i][j] = 1
                return True
            ptable[i][j] = 0
            return False
        
        ptable = list()
        l = len(s)
        for i in range(l):
            prow = list()
            for j in range(l):
                if i >= j:
                    prow.append(1)
                else:
                    prow.append(None)
            ptable.append(prow)
        length = l - 1
        while length != 0:
            for i in range(l - length):
                if check2(s, i, i + length,ptable):
                    return s[i:i + length + 1]
            length -= 1
        return s[0]
