#  [pro] 더 맵게 [python] 

## [문제](https://programmers.co.kr/learn/courses/30/lessons/42626)

### 의사코드 
- heap의 삽입과 삭제는 모두 요소의 마지막에서 수행한다.
1. 스코빌 리스트를 힙으로 변환한다.
2. 가장 안매운 스코빌은 힙의 첫번째 요소 scoville[0]이고 이값이 K보다 클때까지 반복한다. 반복문이 실행 될때마다 연산 횟수 체크한다.
3. 스코빌 힙에서 1번째와 2번째 요소를 제거해서 연산을 수행한 후 다시 힙에 추가한다.

### python Code

```py
import heapq as hq

def solution(scoville, K):
    hq.heapify(scoville)
    cnt = 0; sum = 0
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        cnt += 1
        # try:
        sum = hq.heappop(scoville) + hq.heappop(scoville)*2
        hq.heappush(scoville, sum)
        # except:
        #     return -1
    return cnt

# code 02
def solution(scoville, k):
    heap = []
    for num in scoville:
        hq.heappush(heap, num)

    cnt = 0
    sum = 0
    while heap[0] < k:
        if len(heap) < 2:
            return -1
        cnt += 1
        sum = hq.heappop(heap) + hq.heappop(heap)*2
        hq.heappush(heap, sum)

    return cnt
```
