class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        words=[]
        for i in range(numRows):
            words.append('')
        side = -1
        l=len(s)
        k=0
        for i in range(l):
            words[k]=words[k]+s[i]
            if i%(numRows-1)==0:
                side *= -1
            k = k + side
        word = ''
        for i in range(numRows):
            word += words[i]
        return word            