class Solution:
    def longestValidParentheses(self, s: str) -> int:
        mark = list()
        indofzero = list()
        for i in s:
            if i == "(":
                mark.append(0)
                indofzero.append(len(mark) - 1)
            else:
                if len(indofzero) != 0:
                    mark.append(1)
                    mark[indofzero.pop()] = 1
                else:
                    mark.append(0)
        max = 0
        count = 0
        for i in mark:
            if i == 1:
                count += 1
            else:
                if max<count:
                    max = count
                count = 0
        if max < count:
            max = count
            count = 0
        return max