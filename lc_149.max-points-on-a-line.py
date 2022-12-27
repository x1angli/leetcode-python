# Time complexity: O(n^2), 
# Space complexity O(n)

class SolutionBB:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
        
        ans = 2
        for i in range(n):
            slp_counter = Counter()
            for j in range(n):
                if j != i:
                    if abs(points[j][0] - points[i][0]) < 0.0000001:
                        slope = float('inf')
                    else:
                        slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])

                    slp_counter.update([slope])

            max_val = max(slp_counter.values()) + 1
            ans = max_val if max_val > ans else ans
        return ans

# Wrong solution. Do NOT take it, but learn from it.
class WrongSolution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
        
        slopes = []
        for i in range(n):
            for j in range(i+1, n):
                slope = math.atan2(points[j][1] - points[i][1], points[j][0] - points[i][0])
                if slope <= 0: 
                    slope += math.pi 
                slopes.append(slope)
        
        slp_counter = Counter(slopes)
        max_val = slp_counter.most_common(1)[0][1]
            
        return ceil(sqrt(max_val*2))
