class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        if not matrix:
            return ans

        t = 0
        b = len(matrix) - 1 
        l = 0
        r = len(matrix[0]) - 1

        while True:
            # moving along the top border all the way to the right
            for i in range(l, r+1, 1):
                ans.append(matrix[t][i])  
            t += 1
            if t > b: break

            # moving along the right border all the way to the bottom 
            for i in range(t, b+1, 1):
                ans.append(matrix[i][r])
            r -= 1
            if l > r: break

            # moving along the bottom border all the way to the left
            for i in range(r, l-1, -1):
                ans.append(matrix[b][i])
            b -= 1
            if t > b: break

            # moving along the left boarder all the way to the top
            for i in range(b, t-1, -1):
                ans.append(matrix[i][l])
            l += 1
            if l > r: break

        return ans
