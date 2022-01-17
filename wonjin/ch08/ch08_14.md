# 두 정렬 리스트의 병합[JavaScript, python] 

## 문제 설명
두 개의 정렬된 연결 목록 list1과 list2.
두 개의 목록을 하나의 정렬된 목록 으로 병합합니다 . 목록은 처음 두 목록의 노드를 연결하여 만들어야 합니다.
병합된 연결 목록의 헤드를 반환 합니다 .
## 입출력
- 입력: list1 = [1,2,4], list2 = [1,3,4]
- 출력: [1,1,2,3,4,4]
## 제약:
- 두 목록의 노드 수는 범위 내에 있습니다 [0, 50].
- -100 <= Node.val <= 100
- list1및 둘 다 내림차순list2 으로 정렬됩니다 .
### 의사코드 

### Code
```js

```

```js
var mergeTwoLists = function(l1, l2) {
    if(!l1) return l2;
    if(!l2) return l1;
    
    if(l1.val < l2.val){
        l1.next = mergeTwoLists(l1.next, l2);
        return l1;

    }else{
        l2.next = mergeTwoLists(l1, l2.next);
        return l2;
    }

};
```

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1

        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1

```