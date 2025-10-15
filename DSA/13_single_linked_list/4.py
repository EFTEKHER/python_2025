from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def printList(self, head: Optional[ListNode], label: str = "List"):
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        print(f"{label}: {values}")

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            
            return True


        self.printList(head, "Head")

        # Find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Print the second half before reverse
        self.printList(slow, "Second half before reverse")

        # Reverse second half
        c2 = self.reverseList(slow)
        self.printList(c2, "Second half after reverse")

        # Compare both halves
        c1 = head
        while c2:
            if c1.val != c2.val:
                return False
            c1 = c1.next
            c2 = c2.next
        return True


# --- Helper functions for testing locally ---
def build_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


# --- Test cases ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    head1 = build_linked_list([1,2,3,4,5,6])
    
    print("Test 1 Result:", sol.isPalindrome(head1))  # Expected: True

    # Example 2
    head2 = build_linked_list([1, 2])
    print("Test 2 Result:", sol.isPalindrome(head2))  # Expected: False

    # Example 3
    head3 = build_linked_list([])
    print("Test 3 Result:", sol.isPalindrome(head3))  # Expected: True
    #EXAMPLE 4
    head4 = build_linked_list([1, 2, 3, 2, 1])
    print("Test 4 Result:", sol.isPalindrome(head4))  # Expected: True
