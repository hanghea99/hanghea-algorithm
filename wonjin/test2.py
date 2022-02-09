import sys
from typing import List
input = sys.stdin.readline


def topKFrequent(nums: List[int], k: int) -> List[int]:
    freqs = collections.Counter(nums)

    freqs_heap = []
        # 힙에 음수로 삽입
    
    print(freqs_heap)

    for f in freqs:
        print((-freqs[f], f))
        heapq.heappush(freqs_heap, (freqs[f], f))

    print(freqs_heap)
    topk = list()

    # k번 만큼 추출, 민 힙 이므로 가장 작은 음수 순으로 추출
    for i in range(k):
        t=heapq.heappop(freqs_heap)
        print(t)

        topk.append(t[1])
       
    return topk


if __name__ == '__main__':

    # 입력값 받아오기
    # n = int(input())
    # print(get_card(n))

    queue = topKFrequent([1,1,1,2,2,3],2)
    print("answer:", queue)