class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def check2(result,candidates,l,target,comb=[],tot =0):
            if tot >= target:
                if tot == target:
                    result.append(comb)
                return
            i = 0
            done = set()
            while i<l:
                if candidates[i] not in done:
                    check2(result,candidates[i+1:l],l-i-1,target,comb + [candidates[i]], tot + candidates[i])
                    done.add(candidates[i])
                i += 1

                
        result = list()
        candidates.sort()
        l = len(candidates)
        check2(result, candidates, l,target)
        return result
