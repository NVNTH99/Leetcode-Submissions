class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def check2(result, n, s="", sum=0):
            if sum < 0:
                return
            if len(s) == 2 * n:
                if sum == 0:
                    result.append(s)
                return
            check2(result, n, s + "(", sum + 1)
            check2(result, n, s + ")", sum - 1)
            
        result = list()
        check2(result, n)
        return result