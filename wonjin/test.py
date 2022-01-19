import sys
input = sys.stdin.readline
from collections import deque


def get_card(num):
    # 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.

    # 1 ~ N번까지 카드를 데크로 생성
    queue = deque([n for n in range(1, num+1)])
    print('1 ~ N번까지 카드 : ', queue) 

    i=1
    print("==========================")

    # 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다.
    while len(queue) > 1:
        print(f"반복횟수: {i}")
        i += 1

        # 제일 위에 있는 카드를 바닥에 버린다. 제거한다.
        print('제일 위에 있는 카드 제거 전 : ', queue) 
        queue.popleft()
        print('제일 위에 있는 카드 제거 후 : ', queue) 
        
        #  제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
        queue.append(queue.popleft())
        print('위에 있는 카드 -> 아래로 옮긴다. : ', queue) 
        print("queue len:", len(queue))
        print("==========================")
    return queue.pop()


if __name__ == '__main__':

    # 입력값 받아오기
    # n = int(input())
    # print(get_card(n))
    
    queue = get_card(6)
    print("answer:",queue)

    
    