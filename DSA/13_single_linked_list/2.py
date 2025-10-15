from typing import Optional,List,Set

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        dummy=ListNode(-1)
        dummy.next=head
        prev=dummy 
        current=prev.next 
        s2=set()
        while current:
            if current.val in s2:
                prev.next=current.next
                current=current.next
            else:
                s2.add(current.val)
                prev=current
                current=current.next      
        return dummy.next    
        


# --- Helper functions for testing locally ---
def build_linked_list(values):
    """Builds a linked list from a Python list and returns the head."""
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def print_linked_list(head):
    """Prints the linked list in a readable form."""
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)


# --- Example usage (you can edit/extend for testing) ---
if __name__ == "__main__":
    nums = [1, 1, 2, 3, 3]   # sample input
    head = build_linked_list(nums)

    sol = Solution()
    new_head = sol.deleteDuplicates(head)

    print_linked_list(new_head)  # expected: [1,2,3] once you implement the logic
