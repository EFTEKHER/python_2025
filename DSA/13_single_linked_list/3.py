from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if head is None:
            return None
        dummy=ListNode(-1)
        dummy.next=head
        prev=dummy
        current=prev.next
        while current:
            if current.val==val:
                prev.next=current.next
                current=current.next
            else:
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


# --- Example usage (with given test cases) ---
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    head1 = build_linked_list([1, 2, 6, 3, 4, 5, 6])
    res1 = sol.removeElements(head1, 6)
    print("Test 1:", end=" ")
    print_linked_list(res1)   # Expected: [1,2,3,4,5]

    # Test Case 2
    head2 = build_linked_list([])
    res2 = sol.removeElements(head2, 1)
    print("Test 2:", end=" ")
    print_linked_list(res2)   # Expected: []

    # Test Case 3
    head3 = build_linked_list([7, 7, 7, 7])
    res3 = sol.removeElements(head3, 7)
    print("Test 3:", end=" ")
    print_linked_list(res3)   # Expected: []
