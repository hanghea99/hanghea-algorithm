import heapq

from heap.structures import BinaryMaxHeap


def test_maxheap_we_made(lst, k):
    maxheap = BinaryMaxHeap()

    # for 문을 눈여겨봐두세요.
    # 힙정렬 시간복잡도 계산의 토대입니다.
    for elem in lst:
        maxheap.insert(elem)

    return [maxheap.extract() for _ in range(k)][k - 1]



