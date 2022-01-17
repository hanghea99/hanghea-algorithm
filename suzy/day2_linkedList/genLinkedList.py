class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def add(head, val):
    node = head
    while node.next:
        node = node.next
    node.next = ListNode(val)