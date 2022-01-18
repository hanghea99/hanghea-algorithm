# Leetcode 622. Design Circular Queue

# Implementation the MyCircularQueue class:
# MyCircularQueue(k) : Initializes the object with the size of the queue to be k.
# int Front() : Gets the front item from the queue. If the queue is empty, return -1.
# int Rear() : Gets the last item from the queue. If the queue is empty, return -1.
# boolean enQueue(int value) : Inserts an element into the circular queue. Return true if the operation is successful.
# boolean deQueue() : Deletes an element from the circular queue. Return true if the operation is successful.
# boolean isEmpty() : Checks whether the circular queue is empty or not.
# boolean isFull() : Checks whether the circular queue is full or not.


class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [None] * k
        self.queue_len = k
        self.p1 = 0
        self.p2 = 0

    # 이쪽에서 꼬였음ㅠㅠ 큐에 값 넣으면 p2는 다음 index로
    def enQueue(self, value: int) -> bool:
        if self.queue[self.p2] is None:
            self.queue[self.p2] = value
            self.p2 = (self.p2 + 1) % self.queue_len
            return True
        # if self.isFull():
        #     return False
        # elif self.isEmpty():
        #     self.queue[self.p1] = value
        #     return True
        # else:
        #     self.p2 = (self.p2+1) % self.queue_len
        #     self.queue[self.p2] = value
        #     return True

    def deQueue(self) -> bool:
        if self.queue[self.p1] is None:
            return False
        else:
            self.queue[self.p1] = None
            self.p1 = (self.p1+1) % self.queue_len
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            front = self.queue[self.p1]
            self.queue[self.p1] = None
            if self.p1 == self.p2:
                self.p1, self.p2 = 0, 0
            self.p1 = (self.p1+1) % self.queue_len
            return front

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            rear = self.queue[self.p2]
            self.queue[self.p2] = None
            if self.p1 == self.p2:
                self.p1, self.p2 = 0, 0
            self.p2 = (self.p2-1) % self.queue_len
            return rear

    def isEmpty(self) -> bool:
        # 코드 깔끔하게 좀ㅠㅠ
        return self.p1 == self.p2 and self.queue[self.p1] is None
        # if (self.p1 == self.p2) and (self.queue[self.p1] == None):
        #     return True
        # return False

    def isFull(self) -> bool:
        # 코드 깔끔하게 좀ㅠㅠ
        return self.p1 == self.p2 and self.queue[self.p1] is not None
        # if (self.p1 == (self.p2+1) % self.queue_len) and (self.queue[self.p1] != None):
        #     return True
        # else:
        #     return False

if __name__ == "__main__":
    myCircularQueue = MyCircularQueue(3)
    myCircularQueue.enQueue(1) # return True
    print("enQueue(1) >>> ",myCircularQueue.enQueue(1), myCircularQueue.queue)
    myCircularQueue.enQueue(2) # return True
    print("enQueue(2) >>> ",myCircularQueue.enQueue(2), myCircularQueue.queue)
    myCircularQueue.enQueue(3) # return True
    print("enQueue(3) >>> ",myCircularQueue.enQueue(3), myCircularQueue.queue)
    myCircularQueue.enQueue(4) # return False
    print("enQueue(4) >>> ",myCircularQueue.enQueue(4), myCircularQueue.queue)
    myCircularQueue.Rear() # return 3
    print("Rear() >>> ",myCircularQueue.Rear(), myCircularQueue.queue)
    myCircularQueue.isFull() # return True
    print("isFull() >>> ",myCircularQueue.isFull(), myCircularQueue.queue)
    myCircularQueue.deQueue() # return True
    print("deQueue() >>> ",myCircularQueue.deQueue(), myCircularQueue.queue)
    myCircularQueue.enQueue(4) # return True
    print("enQueue() >>> ",myCircularQueue.enQueue(4), myCircularQueue.queue)
    myCircularQueue.Rear() # return 4
    print("Rear() >>> ",myCircularQueue.Rear(), myCircularQueue.queue)


