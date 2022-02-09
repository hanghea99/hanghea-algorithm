from heap.structures import BinaryMaxHeap

import heapq as hq
import sys
sys.stdin = open(
    "C:\WonJin\pythonalgorithm\hanghea-algorithm\wonjin\input.txt", 'r')
# input = sys.stdin.readline


# 힙을 만들려면, []로 초기화된 리스트를 사용하거나, 함수 heapify()를 통해 값이 들어 있는 리스트를 힙으로 변환 할 수 있습니다.

# 제출 코드
def solution(N):
    heap = []
    result = ''
    for i in range(N):
        num = int(input())

        if num == 0:
            # if len(heap) > 0:
            try:
                result += f'{-hq.heappop(heap)}\n'
            # else:
            except:
                result += '0\n'
        else:
            hq.heappush(heap, -num)

    return result

# maxheap
def test_maxheap_we_made(N):
    hq = BinaryMaxHeap()

    result = ''
    for i in range(N):
        num = int(input())

        print('=====================================')
        print(f'반복횟수 : {i+1} || num : {num}')

        if num == 0:
            if len(hq) > 0:
                result += f'{hq.extract()}\n'
            else:
                result += '0\n'
        else:
            hq.insert(num)

    print("========answer========")
    return result



# 연산의 개수
N = int(input())

# sol_maxheap(N)

print(solution(N).rstrip())

print(test_maxheap_we_made(N))

# assert canFinish(numCourses=2, prerequisites=[[3, 0], [0, 1], [2, 3], [3, 1]]) == True
