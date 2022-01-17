# Algorithm_day2

## 234. [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        queue = deque()
        node = head
        count = 0
        while node is not None:
            queue.append(node.val)
            count += 1
            node = node.next
        for _ in range(count // 2):
            if queue.pop() != queue.popleft():
                return False
        return True
```

다른 풀이

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        one_step = two_step = head
        rev = None

        while two_step is not None and two_step.next is not None:
            two_step = two_step.next.next
            rev, rev.next, one_step = one_step, rev, one_step.next

        if two_step:
            one_step = one_step.next

        while one_step is not None:
            if one_step.val != rev.val:
                return False
            one_step, rev = one_step.next, rev.next

        return True
```

## 21. [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(None)
        node = answer
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        if list1 is not None:
            node.next = list1
        else:
            node.next = list2

        return answer.next
```

## 206. [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
          return head
        temp = []
        while head is not None:
            temp.append(head.val)
            head = head.next
        answer = ListNode(temp.pop())
        node = answer
        while temp:
            node.next = ListNode(temp.pop())
            node = node.next
        return answer
```

## 328. [Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        oddNode = head
        evenNode = head.next
        evenNodeHead = head.next
        Node = head

        while evenNode and evenNode.next:
            oddNode.next, evenNode.next = oddNode.next.next, evenNode.next.next
            oddNode, evenNode = oddNode.next, evenNode.next

        oddNode.next = evenNodeHead
        return head
```
