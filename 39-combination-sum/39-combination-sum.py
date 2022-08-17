class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def check2(result, candidates, target, comb=[]):
            tot = sum(comb)
            if tot >= target:
                if tot == target:
                    result.append(comb)
                return
            l = len(candidates)
            for i in range(l):
                check2(result, candidates[i:l], target, comb + [candidates[i]])
                
        result = list()
        candidates.sort()
        check2(result, candidates, target)
        return result