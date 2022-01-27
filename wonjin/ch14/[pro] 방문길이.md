# [pro] 방문길이 [python] 

## [문제](https://programmers.co.kr/learn/courses/30/lessons/49994)

### 의사코드 
1. U, L, D, R 을 하나씩 입력받으며, 그냥 순차적으로 트래킹하면 된다.
2. check 를 set 자료구조로 두어, 이미 지나간 길인지 아닌지 체크하면 된다.
3. 주의해야할 점은, 트래킹에는 '단방향성' 이 존재하지만, 길 자체는 '양방향' 이라는 점이다.
4. 출발지점과 도착지점이 반대여도 같은 간선이므로 한번 저장할때 **(출발지점x, 출발지점y, 도착지점x, 도착지점y), (도착지점x, 도착지점y, 출발지점x, 출발지점y)** 로 두 튜플로 저장하여 예외처리 해준다.



### python Code01
```py
def solution(dirs):
    move = {'U':[0,1], 'D':[0,-1],'R':[1,0],'L':[-1,0]}
    check = set()
    now = [0,0]

    for i in range(len(dirs)):
        mov_x = now[0]+move[dirs[i]][0]
        mov_y = now[1]+move[dirs[i]][1]

        if mov_x>5 or mov_x <-5 or mov_y>5 or mov_y<-5:continue

        check.add((now[0],now[1], mov_x, mov_y))
        check.add((mov_x, mov_y, now[0], now[1]))

        now= [mov_x,mov_y]
    
    return len(check)//2
```
