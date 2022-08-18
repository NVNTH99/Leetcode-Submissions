class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def check2(board, word, i, j, l1, l2, l, wordpos=0):
            if wordpos >= l:
                return True
            if i < 0 or j < 0 or i >= l1 or j >= l2:
                return False
            result = False
            if board[i][j] == word[wordpos]:
                board[i][j] = 0
                result = result or check2(board, word, i + 1, j, l1, l2, l, wordpos + 1)
                result = result or check2(board, word, i - 1, j, l1, l2, l, wordpos + 1)
                result = result or check2(board, word, i, j + 1, l1, l2, l, wordpos + 1)
                result = result or check2(board, word, i, j - 1, l1, l2, l, wordpos + 1)
                if result is False:
                    board[i][j] = word[wordpos]
            return result
        
        result = False
        l1 = len(board)
        l2 = len(board[0])
        l = len(word)
        for i in range(l1):
            for j in range(l2):
                result = result or check2(board, word, i, j, l1, l2, l)
                if result is True:
                    return result
        return result