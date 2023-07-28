class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        n = len(time)
        node_cost = [0] + time
        node_next = [[] for _ in range(n+1)]
        node_next[0] = list(range(1,n+1))
        for rel in relations:
            prev_node, next_node = rel
            node_next[prev_node].append(next_node)
        
        @cache
        def dfs(root_node):
            ans_l = 0
            for node_i in node_next[root_node]:
                ans_l = max(dfs(node_i), ans_l)
            return ans_l + node_cost[root_node]

        return dfs(0)
