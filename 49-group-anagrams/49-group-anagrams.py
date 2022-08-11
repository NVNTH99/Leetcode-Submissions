class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = list()
        alphabets = list()
        for i in strs:
            chars = list()
            for j in i:
                chars.append(j)
            chars.sort()
            if chars in alphabets:
                output[alphabets.index(chars)].append(i)
            else:
                output.append([i])
                alphabets.append(chars)
        return output
                