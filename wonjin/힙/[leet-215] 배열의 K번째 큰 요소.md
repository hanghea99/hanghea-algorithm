#  [leet-215] 배열의 K번째 큰 요소 [python] 

## [문제](https://leetcode.com/problems/kth-largest-element-in-an-array/)

### 의사코드 
- 파이썬의 힙은 최소 힙으로 구현되었다.
- heap의 삽입과 삭제는 모두 요소의 마지막에서 수행한다.
- 삽입과 삭제 후 힙의 특성을 만족하도록 바꿔주는 연산을 계속 수행한다. 

### python Code

```py
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap_list = []

        for n in nums:
            heapq.heappush(heap_list, -n)

        pop_list = []
        for i in range(1, k+1):
            pop_list.append(-heapq.heappop(heap_list))

        return pop_list[-1]
```
