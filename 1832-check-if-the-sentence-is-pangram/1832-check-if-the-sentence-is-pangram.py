class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = set()
        for i in sentence:
            alphabets.add(i)
        if len(alphabets) == 26:
            return True
        return False