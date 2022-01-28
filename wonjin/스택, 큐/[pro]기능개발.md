# [pro] 기능 개발 [python] 

## [문제](https://programmers.co.kr/learn/courses/30/lessons/42586)

### 의사코드 
1. 기능이 완료될때까지 걸리는 일 수를 -(((p-100)//s))연산을 통해 구해서 배열로 저장한다.
2. 코드01에서는 count변수로 같은 날에 배포가 가능한 기능의 개수를 받는다. 코드02에서는 기능의 인덱스의 차이값으로 기능의 개수구하고 answer에 추가했다.
3. 현재 기능의 남은 일수보다 이전 기능의 일수가 작다면 이전 기능은 배포가능하기 때문에 answer에 추가하고 현재 인덱스를 front에 저장한다. (기준을 바꾼다.)

### python Code01
```py
def solution(progresses, speeds):
    answer = []
    # index()메서드를 사용하면 중복된 요소가 있을 경우 맨 앞 요소의 인덱스를 추출하는 문제

    progresses = [-(((p-100)//s)) for p, s in zip(progresses, speeds)]

    point = 0
    count = 1
    for i in range(1, len(progresses)):
        if progresses[point] >= progresses[i]:
            count += 1
        else:
            answer.append(count)

        if progresses[point] < progresses[i]:
            count = 1
            point = i
    answer.append(len(progresses) - point)
    return answer
```
### python Code02

```py
def solution5(progresses, speeds):
    answer = []
    # progresses = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]
    progresses = [-(((p-100)//s)) for p, s in zip(progresses, speeds)]

    front = 0
    for idx in range(len(progresses)):
        if progresses[idx] > progresses[front]:
            answer.append(idx - front)
            front = idx

        print(front)

    answer.append(len(progresses) - front)
    return answer
```