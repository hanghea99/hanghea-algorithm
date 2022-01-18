# Algorithm Day3

## 739. [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

1차 시도(시간 초과)

```py
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for _ in range(len(temperatures))]
        stack = [0]

        for i in range(1, len(temperatures)):
            if temperatures[i] <= temperatures[i - 1]:
                stack.append(i)
                continue

            temp = []

            for idx, j in enumerate(stack):
                if temperatures[i] > temperatures[j]:
                    answer[j] = i - j
                    temp.append(idx)

            for t in temp[::-1]:
                stack.pop(t)
            stack.append(i)
        return answer
```

다른 풀이

```py
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for _ in range(len(temperatures))]
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                answer[stack[-1]] = idx - stack[-1]
                stack.pop()
            stack.append(idx)

        return answer
```

## 316. [Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/)

```py
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''
```

## 232. [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

```py
class MyQueue:

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        self.peek()
        self.push_stack.append(x)

    def pop(self) -> int:
        if self.pop_stack:
            return self.pop_stack.pop()
        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())
        if self.pop_stack:
            return self.pop_stack.pop()

    def peek(self) -> int:
        if self.pop_stack:
            return self.pop_stack[-1]
        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())
        if self.pop_stack:
            return self.pop_stack[-1]


    def empty(self) -> bool:
        return not(self.push_stack or self.pop_stack)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```

## 622. [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)

```py
class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.stack = [None for _ in range(k)]
        self.head = 0
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.stack[self.tail] = value
        self.tail = (self.tail + 1) % self.size
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.stack[self.head] = None
        self.head = (self.head + 1) % self.size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.stack[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.stack[self.tail - 1]

    def isEmpty(self) -> bool:
        return self.stack[self.head] is None

    def isFull(self) -> bool:
        return self.stack[self.tail] is not None


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
```
