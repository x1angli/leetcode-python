class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return []
        
        r, i, j, di, dj = [], 0, 0, 0, 1
        h, w = len(matrix), len(matrix[0])

        for _ in range(h * w):
            r.append(matrix[i][j])
            matrix[i][j] = 0
            
            if matrix[(i + di) % h][(j + dj) % w] == 0:   # punch line!  
                di, dj = dj, -di                          # punch line! 
            
            i += di
            j += dj
            
        return r
        
