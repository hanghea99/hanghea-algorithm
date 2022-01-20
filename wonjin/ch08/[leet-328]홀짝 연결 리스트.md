# 홀짝 연결 리스트 [JavaScript, python] 

## 문제 설명
단일 연결 목록이 주어지면 head홀수 인덱스를 가진 모든 노드를 그룹화하고 짝수 인덱스를 가진 노드를 그룹화 하고 재정렬된 목록을 반환합니다 .
첫 번째 노드는 홀수 로 간주 되고 두 번째 노드는 짝수 로 간주 됩니다.
짝수 및 홀수 그룹 내부의 상대적 순서는 입력에서와 같이 유지되어야 합니다.
O(1) 추가 공간 복잡도와 O(n)시간 복잡도 문제를 해결해야 합니다 .

## 입출력
- Input: head = [1,2,3,4,5]
- Output: [5,4,3,2,1]
## 제약:
- n == 연결 리스트의 노드 수
- 0 <= n <= 104
- -106 <= Node.val <= 106
### 의사코드 

### JavaScript Code
```js
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var oddEvenList = function(head) {
    //비어있는 연결리스트 예외처리
    if(head === null){
        return null;
    }
    
    let odd = head;
    let even = head.next;
    let even_head = head.next;
    
    //각각 홀수번째, 짝수번째끼리 노드 연결
    while (even && even.next){
        odd.next = odd.next.next;
        even.next = even.next.next;
        odd = odd.next;
        even = even.next;
    }
    
    // 만들어진 홀수 리스트에 짝수 리스트 연결
    odd.next = even_head;
    return head;
    
};
```
### python Code

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
        
        odd = head
        even = head.next
        even_head = head.next
        
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
            
        odd.next = even_head
        return head
```