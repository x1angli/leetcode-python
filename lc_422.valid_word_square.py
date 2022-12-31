class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        collen = len(words[0])
        rowlen = len(words)
        for j in range(collen):
            col = ''
            for i in range(rowlen):
                if j < len(words[i]):
                    col += words[i][j]
            if col != words[j]:
                return False
        return True
      
class SolutionPadded:
    def validWordSquare(self, words: List[str]) -> bool:
        n = max(len(words[0]), len(words))
        words = [w + '#'*(n-len(w)) for w in words]
        words_t = [''.join(cell) for cell in zip(*words)]
        return words_t == words


# The solution below would fail the case with the input `["ball","asee","lett","le"]` 
class WrongSolution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)
        for i in range (1, n):
            j_range = min(len(words[i]), i)
            for j in range(0, j_range):
                if i >= len(words[j]):
                    return False
                if words[i][j] != words[j][i]:
                    return False        
        return True
