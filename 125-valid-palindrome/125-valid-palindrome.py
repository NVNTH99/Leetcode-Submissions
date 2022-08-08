class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = len(s)
        i = 0
        while i < l:
            if s[i].isalnum() == False:
                s = s.replace(s[i], "", 1)
                l -= 1
                i -= 1
            i += 1
        l = len(s)-1
        i = 0
        while i <= l:
            if s[i] != s[l]:
                return False
            i += 1
            l -= 1
        return True