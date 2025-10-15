
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2
        return dummy.next
if __name__=="__main__":
    s=Solution()
    l1=ListNode(1)
    l1.next=ListNode(2)
    l1.next.next=ListNode(4)
    l2=ListNode(1)
    l2.next=ListNode(3)
    l2.next.next=ListNode(4)
    res=s.mergeTwoLists(l1,l2)
    while res:
        print(res.val,end=" ")
        res=res.next    
    