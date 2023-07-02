class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = [(l_i.val, i, l_i)  for i, l_i in enumerate(lists) if l_i ]
        heapq.heapify(h)

        
        curr = ListNode()
        ans = curr

        while len(h)>0:
            heapTop = heapq.heappop(h)
            if heapTop[0] == 999999:
                break
            curr.next = ListNode(val = heapTop[0])
            curr = curr.next 
            nextNode = heapTop[2].next
            if nextNode: 
                heapq.heappush(h, (nextNode.val, heapTop[1], nextNode))

        return ans.next
