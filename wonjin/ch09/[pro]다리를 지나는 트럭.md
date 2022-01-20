# 다리를 지나는 트럭

## [문제](https://programmers.co.kr/learn/courses/30/lessons/42583)

### 의사코드

1. bridge 변수에 다리 길이만큼 0으로 초기화된 배열을 선언합니다.
2. 큐에 요소가 다 없어질 때까지 시간 측정하고, 반복문을 수행합니다.
3. 현재 다리에 있는 무게와 추가될 트럭의 무게를 더한 후 weight보다 작으면 bridge에 추가하고 아니면 0을 추가합니다.
4. 트럭 배열의 요소가 없어질 때까지 3번과정을 수행합니다.
5. while문을 반복하다가 bridge의 길이가 0이 되면 time이 최소 걸린 시간입니다.

### py Code 01

```py
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    queue = [0]*bridge_length

    while len(queue):
        time += 1
        queue.pop(0)

        if truck_weights:
            if sum(queue) + truck_weights[0] <= weight:
                queue.append(truck_weights.pop(0))
            else:
                queue.append(0)
    return time

```

### py Code 02
- 시간 점프
```py
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    weightOnBridge = 0
    # 큐 [트럭무게, 얘가 나갈 시간].
    queue = deque([[0, 0]])

    waiting = deque(truck_weights)  # 대기 트럭 큐
    #  대기 트럭, 다리를 건너는 트럭이 모두 0일 때 까지 다음 루프 반복
    while len(queue) > 0 or len(waiting) > 0:
        
        #   1. 현재 시간이, 큐 맨 앞의 차의 '나갈 시간'과 같다면 내보내주고, 다리 위 트럭 무게 합에서 빼준다.
        if queue[0][1] == time:
            weightOnBridge -= queue.popleft()[0]

        # 2. 다리 위 트럭 무게 합 + 대기중인 트럭의 첫 무게가 감당 무게 이하면 다리 위 트럭 무게 업데이트, 큐 뒤에[트럭무게, 이 트럭이 나갈 시간] 추가.
        if len(waiting) > 0 and weightOnBridge + waiting[0] <= weight:
            weightOnBridge += waiting[0]
            queue.append([waiting.popleft(), time + bridge_length])
        else:
            #   3. 다음 트럭이 못올라오는 상황이면 얼른 큐의 첫번째 트럭이 빠지도록 그 시간으로 점프한다. 참고: if 밖에서 1 더하기 때문에 -1 해줌
            if len(queue) > 0 and queue[0]:
                time = queue[0][1]-1
        time += 1
    return time

```
