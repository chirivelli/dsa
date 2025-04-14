class MinHeap:
    def __init__(self):
        self.pq = []

    def append(self, val: int):
        self.pq.append(val)
        k = len(self.pq) - 1

        while k:
            if self.pq[k] < self.pq[k//2]:
                self.pq[k], self.pq[k // 2] = self.pq[k//2], self.pq[k]
            k = k//2

    # def popleft(self):
    #     res = self.pq[0]
    #     self.pq[0] = self.pq[-1]
    #     self.pq.pop()

    def display(self):
        print(self.pq)

def main():
    minHeap = MinHeap()


if __name__ == '__main__':
    main()