# Top K Frequent Elements [python]
## [문제](https://leetcode.com/problems/top-k-frequent-elements/)

### 의사코드
- 힙 자료구조를 이용한 풀이한 문제이다.
1. Counter로 nums배열에서 요소하나를 키로하고 키와 같은 개수를 가진 딕셔너리를 만든다.
2. 파이썬의 heapq 모듈은 최소 힙으로 구현되어 있기 때문에 최대 힙 구현을 위해서는 트릭이 필요하다. 힙에 추가할 때 (-item, item)이처럼 -를 붙여주면 최대 힙으로 구현할 수 있다.

### py code
```py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)

        freqs_heap = []
            # 힙에 음수로 삽입
        for f in freqs:
            print((-freqs[f], f))
            heapq.heappush(freqs_heap, (-freqs[f], f))

        print(freqs_heap)
        topk = list()

        # k번 만큼 추출, 민 힙 이므로 가장 작은 음수 순으로 추출
        for i in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk

```

### py code02
```py
# Counter의 monst_common() 이용
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        print()

        return list(zip(*collections.Counter(nums).most_common(k)))[0]

```