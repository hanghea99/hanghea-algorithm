# 스택을 이용한 큐 구현 [Python]


### py code
```py

class MyQueue:

    def __init__(self):
        self.input=[]
        self.output=[]

    def push(self, x: int) -> None:
        self.input.append(x)        

    def pop(self) -> int:
        self.peek()
        return self.output.pop()        

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return self.input==[] and self.output==[]
        

if __name__ == '__main__':
    queue = MyQueue();

    assert queue.push(1)==None;
    assert queue.push(2)==None;
    assert queue.push(3)==None;
    assert queue.push(4)==None;
    assert queue.peek();
    assert queue.pop() == 1;
    assert queue.empty() == False;

```