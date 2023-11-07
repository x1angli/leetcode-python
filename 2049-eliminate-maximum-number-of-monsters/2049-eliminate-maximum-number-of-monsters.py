class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        

        n = len(dist)
        ttc = [dist[i]/speed[i] for i in range(n)]
        ttc.sort()
        for ans in range(n):
            if ttc[ans] <= ans:
                return ans


        return n
        