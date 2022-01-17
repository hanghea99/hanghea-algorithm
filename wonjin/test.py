from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
            print(odd)
            print(even)

        odd.next = even_head
        return head


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(
        3, ListNode(4, ListNode(5, None)))))
    LinkedFun = Solution()
    LinkedFun.oddEvenList(head)
