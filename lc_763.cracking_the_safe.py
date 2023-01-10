# Hierholzer
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        edges = []
        nodes_cnt = k ** (n - 1)
        node_edges_cnt = [k-1] * nodes_cnt         # count of unvisited edges for each node

        node = 0
        while node_edges_cnt[node] >= 0:
            edge = node_edges_cnt[node]

            edges.append(str(edge))

            node_edges_cnt[node] -= 1
            node = (node * k + edge) % nodes_cnt

        return '0' * (n - 1) + ''.join(edges)
