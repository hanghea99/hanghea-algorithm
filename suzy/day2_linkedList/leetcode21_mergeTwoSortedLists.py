from typing import Optional
from suzy.day2_linkedList.genLinkedList import *

# 모범 답안 --> 상위 90%대
# 현재 포인터가 가르키고 있는 list1 노드와 list2 노드 값들을 비교하되,
# 비교하여 작은 값들을 가진 노드들은 list1으로 몰아준다 -> 리턴은 list1의 head 노드
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # 가르키는 list1 노드가 이제 더이상 없거나(= 남아있는 나머지 list2 노드들 모두 list1으로 한방에 몰아버린다)
    # list2 노드들이 아직 남아있으면서 가르키는 list1 노드 값이 클때(= list2 노드로 바꿔치기)
    if (not list1) or (list2 and list1.val > list2.val):
        list1, list2 = list2, list1
    # 위 조건문들 통과하지 않는 케이스들(어찌되었든 공통적으로 list1이 남아있는 케이스들)
    # 다음 list1 노드로 넘기고 똑같은 프로세스 반복 -> 재귀
    if list1:
        list1.next = mergeTwoLists(list1.next, list2)
    return list1

# 무식한 방법 --> timeout
# 제 3의 linked list를 만들고 현재 포인터로 가르키고 있는 list1 노드와 list2 노드 값들을 각각 비교하여
# 작은 값을 가지는 노드들이 제 3의 노드로 간다
def mergeTwoLists_bruteforce(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    if list1.val > list2.val:
        head = list1
        node = head
    elif list1.val < list2.val:
        head = list2
        node = head
    else:
        head = list1
        head.next = list2
        node = head.next

    while node.next:
        if list1.val > list2.val:
            node.next = list1
            node = node.next
        elif list2.val > list1.val:
            node.next = list2
            node = node.next
        else:
            node.next = list1
            node.next.next = list2
            node = node.next.next

    return head

if __name__ == "__main__":
    # generate input example
    list1 = ListNode(1)
    nodes = [2,4]
    for num in nodes:
        add(list1, num)

    list2 = ListNode(1)
    nodes = [3,4]
    for num in nodes:
        add(list2, num)

    node = list1
    print("input(list1) >>>")
    while node.next:
        print(node.val)
        node = node.next
    print(node.val)

    node = list2
    print("input(list2) >>>")
    while node.next:
        print(node.val)
        node = node.next
    print(node.val)

    new_head = mergeTwoLists(list1, list2)
    node = new_head
    print("output >>>")
    while node.next:
        print(node.val)
        node = node.next
    print(node.val)

