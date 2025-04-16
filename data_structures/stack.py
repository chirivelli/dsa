class MonoStack:
    def __init__(self):
        self.stack = []

    def append(self, val: int):
        while self.stack and val > self.stack[-1]:
            self.stack.pop()
        self.stack.append(val)

    def display(self):
        print(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

def main():
    mono = MonoStack()
    mono.append(5)
    mono.append(3)
    mono.append(6)
    mono.append(7)
    mono.append(1)
    mono.display()


if __name__ == '__main__':
    main()