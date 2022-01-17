from typing import Optional
from suzy.day2_linkedList.genLinkedList import *

# solutions

# 홀수번째 노드들은 무조건 앞으로, 짝수번째 노드들은 무조건 뒤로
# 마지막에 홀수/짝수번째 노드 정리되면 마지막 홀수번째 노드랑 첫번째 짝수 노드랑 연결
def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None

    odd_node = head
    even_node = head.next
    even_node_head = head.next

    while even_node and even_node.next:
        odd_node.next, even_node.next = odd_node.next.next, even_node.next.next
        odd_node, even_node = odd_node.next, even_node.next

    # 다 정리하고, 홀수번째 마지막 노드.next = 짝수번째 첫번째 노드
    odd_node.next = even_node_head
    return head

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

    new_head = oddEvenList(head)
    node = new_head
    print("output >>>")
    while node.next:
        print(node.val)
        node = node.next
    print(node.val)
