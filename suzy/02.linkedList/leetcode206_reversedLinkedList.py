from typing import Optional
from suzy.day2_linkedList.genLinkedList import *

# solutions
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    current_node = head
    previous_node = None

    # 1 -> 2 -> 3 -> 4 -> 5
    # 1 <- 2 <- 3 <- 4 <- 5
    # 2 입장에서는 previous_node = 1 -> next_node로 변경
    #           next_node = 3 -> previous_node로 변경
    # 최종적으로 5가 새로운 linked list의 head로 리턴되어야되므로 previous_node를 리턴

    # 이전 연결을 끊고, 반대로 연결
    # 다음 노드 진행을 위해서는 마지막에 node = node.next가 들어가야되므로 원래 node.next를 임시로 옮겨준다
    while current_node:
        temp = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = temp

    return previous_node


if __name__ == "__main__":
    # generate input example
    head = ListNode(1)
    for num in range(2, 6):
        add(head, num)

    node = head
    print("input >>>")
    while node.next:
        print(node.val)
        node = node.next
    print(node.val)

    new_head = reverseList(head)
    node = new_head
    print("output >>>")
    while node.next:
        print(node.val)
        node = node.next
    print(node.val)
