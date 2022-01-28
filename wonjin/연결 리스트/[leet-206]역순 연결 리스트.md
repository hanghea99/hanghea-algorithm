
# 역순 연결 리스트[JavaScript, python] 

## 문제 설명
head단일 연결 목록이 주어지면 목록을 뒤집고 역 목록을 반환합니다 .
## 입출력
- Input: head = [1,2,3,4,5]
- Output: [5,4,3,2,1]
## 제약:
- 목록의 노드 수는 범위 [0, 5000]입니다.
- -5000 <= Node.val <= 5000
### 의사코드 

### Code
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

var reverseList = function(head) {
    let node = head;
    let prev = null;
    
    while(node){
        let next = node.next;
        node.next = prev;
        prev = node;
        node = next;
    }
    return prev
};
```
```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None
        
        while node:
            next= node.next
            print("next:", next)

            node.next = prev
            print("node.next:", node.next)

            prev = node
            print("prev:", prev)
            node = next
            print("node:", node)

        return prev
```