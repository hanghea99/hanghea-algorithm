# 원형 큐 디자인 [Python]


### py code
```py
class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None]*k
        self.maxlen=k
        self.p1=0
        self.p2=0

    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2+1)%self.maxlen
            return True
        return False

    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        
        self.q[self.p1] = None
        self.p1 = (self.p1+1)%self.maxlen
        return True

    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self) -> int:
        return -1 if self.q[self.p2-1] is None else self.q[self.p2-1]
        

    def isEmpty(self) -> bool:
        return self.p2 == self.p1 and self.q[self.p1] is None


    def isFull(self) -> bool:
        return self.p2 == self.p1 and self.q[self.p1] is not None



if __name__ == '__main__':
    circularQueue = MyCircularQueue(5)
    print(circularQueue.enQueue(10) )
    print(circularQueue.enQueue(20) )
    print(circularQueue.enQueue(30) )
    print(circularQueue.enQueue(40) )
    print(circularQueue.Rear())
    print(circularQueue.isFull())
    print(circularQueue.deQueue())
    print(circularQueue.deQueue())
    print(circularQueue.enQueue(50))
    print(circularQueue.enQueue(60))
    print(circularQueue.Rear())
    print(circularQueue.Front())

```