class MyQueue:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        first = self.queue[0]
        del self.queue[0]
        return first

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyQueue object will be instantiated and called as such:
if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
