class BinaryMaxHeap:
    def __init__(self):
        # 계산 편의를 위해 0이 아닌 1번째 인덱스부터 사용한다.
        self.items = [None]

    def __len__(self):
        # len() 연산을 가능하게 하는 매직 메서드 덮어쓰기(Override).
        return len(self.items) - 1

    def _percolate_up(self):
        # percolate: 스며들다.
        cur = len(self)
        # left 라면 2*cur, right 라면 2*cur + 1 이므로 parent 는 항상 cur // 2
        parent = cur // 2

        while parent > 0:
            print('befter :', self.items)
            if self.items[cur] > self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]
            print('after :', self.items)

            cur = parent
            parent = cur // 2

    def _percolate_down(self, cur):
        biggest = cur
        left = 2 * cur
        right = 2 * cur + 1

        print('befter :', self.items)

        if left <= len(self) and self.items[left] > self.items[biggest]:
            biggest = left

        if right <= len(self) and self.items[right] > self.items[biggest]:
            biggest = right

        if biggest != cur:
            self.items[cur], self.items[biggest] = self.items[biggest], self.items[cur]
            print('after :', self.items)
            self._percolate_down(biggest)

    def insert(self, k):
        self.items.append(k)
        print(f'self.items.append({k}) :', self.items)

        print('====_percolate_up 실행====')
        self._percolate_up()
        print('====_percolate_up 종료====')

    def extract(self):
        if len(self) < 1:
            return None

        root = self.items[1]
        # self.items[1]= self.items[-1]
        self.items[1], self.items[-1] = self.items[-1], root

        print('self.items 자리바꿈 : ', self.items)

        self.items.pop()
        print('self.items.pop() : ', self.items)

        print('====_percolate_down 실행====')
        self._percolate_down(1)
        print('====_percolate_down 종료====')

        return root
