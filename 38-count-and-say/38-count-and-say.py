class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        string = self.countAndSay(n-1)
        str2 = ''
        digit = string[0]
        count = 0
        i = 0
        l = len(string)
        while i < l:
            if string[i] == digit:
                count += 1
                i += 1
            else:
                str2 = str2+str(count)+digit
                digit = string[i]
                count = 0
        str2 = str2 + str(count) + digit
        return str2