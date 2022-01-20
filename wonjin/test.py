import collections
import heapq
from typing import List
import sys
input = sys.stdin.readline

def topKFrequent( nums: List[int], k: int) -> List[int]:
    freqs = collections.Counter(nums)
    print(freqs)
    
    freqs_heap = []
        # 힙에 음수로 삽입
    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))
    
    topk = list()
    
    # k번 만큼 추출, 민 힙 이므로 가장 작은 음수 순으로 추출
    for i in range(k):
        print(i)
        print(freqs_heap)

        t=heapq.heappop(freqs_heap)[1]
        print(freqs_heap)

        topk.append(t)
        print("t",t)
    
    return topk


if __name__ == '__main__':

    print(topKFrequent([1,1,1,2,2,3],2))
    
