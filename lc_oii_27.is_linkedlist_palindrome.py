# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# An efficient solution with O(n) time-complexity and O(n) memory footprint
class Solution:   
    def __init__(self):
        self.restore = True
        
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        
        def end_of_first_half(head):
            fast, slow = head, head
            while fast.next is not None and fast.next.next is not None:
                fast = fast.next.next
                slow = slow.next
            return slow

        def reverse_list(head):
            prev, curr = None, head
            while curr is not None:
                curr_next = curr.next
                curr.next = prev
                prev = curr
                curr = curr_next
            return prev

        tail_1st = end_of_first_half(head)
        head_2nd = reverse_list(tail_1st.next)

        curr_1st = head
        curr_2nd = head_2nd
        while curr_2nd is not None:
            if curr_1st.val != curr_2nd.val:
                return False
            curr_1st = curr_1st.next
            curr_2nd = curr_2nd.next

        
        if(self.restore): # Optional
            tail_1st.next = reverse_list(head_2nd)
        
        return True    

            
class SolutionResursive:
    def isPalindrome(self, head: ListNode) -> bool:

        slow_node = head

        def recursively_check(curr):
            nonlocal slow_node
            if curr is None:
                return True
            if not recursively_check(curr.next):
                return False
            if slow_node.val != curr.val:
                return False
            else: # when slow_node.val == curr.val
                slow_node = slow_node.next
                return True

        return recursively_check(head)
    
    
class SolutionPlainArray:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]
    
