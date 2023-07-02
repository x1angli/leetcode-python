# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        ans = ListNode() #dummy
        ans.next = head
        curr = ans
        curr1 = ans.next

        terminated = False
        while True: 
            cache = []
            for _ in range(k):
                if curr1:
                    cache.append(curr1)
                    curr1 = curr1.next
                else:
                    terminated = True
                    break # break the inner for loop
            if terminated:
                if len(cache) > 0:
                    curr.next = cache[0]
                else:
                    curr.next = None
                break # break the outer while loop

            for i in range(1, k):
                cache[i].next = cache[i-1]
            curr.next = cache[k-1]
            curr = cache[0]
            


        return ans.next
