class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        pos = -1
        while 1:
            pos = haystack.find(needle[0],pos +1)
            if needle == haystack[pos:pos+l] or pos == -1:
                return pos