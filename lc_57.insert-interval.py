class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        ans = []

        pos_l = bisect_left(intervals, newInterval[0], key=itemgetter(1))
        # [pos_l][1] >= newInterval[0]
        pos_r = bisect_left(intervals, newInterval[1], key=itemgetter(0))
        # [pos_r][0] >= newInterval[1]
        if pos_r < n and intervals[pos_r][0] == newInterval[1]:
            pos_r += 1

        # Mainflow Starts
        # Attaching left
        if pos_l >= 1: 
            ans.extend(intervals[0:pos_l])
        
        print(pos_l)
        print(pos_r)
        # Preparing middle
        new_intv = newInterval
        if pos_r > pos_l:
            new_intv=[min(new_intv[0], intervals[pos_l][0]), max(new_intv[1], intervals[pos_r-1][1])]
        print(new_intv)
        # Attaching middle
        ans.append(new_intv)
        
        # Attaching right
        if pos_r < n: 
            ans.extend(intervals[pos_r:n])

        # Mainflow Ends
        return ans
