class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = 1
        i = 0
        l = len(s)
        if l == 0:
            return 0
        if s[0]=='-':
            sign = -1
            i = 1
        elif s[0] == '+':
            i = 1
        num = 0
        l = len(s)
        while i<l and ord(s[i])>=48 and ord(s[i])<=57:
            num = num*10 + ord(s[i])-48
            if num>2**31:
                break
            i += 1
        num = sign * num
        if num > 2**31 - 1:
            return 2**31 -1
        elif num < -(2**31):
            return -(2**31)
        else:
            return num