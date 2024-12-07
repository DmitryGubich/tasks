# queues are often using for cache !!!
from collections import deque

TIME_INTERVAL = 3000


class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - TIME_INTERVAL:
            self.queue.popleft()
        return len(self.queue)


if __name__ == "__main__":
    obj = RecentCounter()
    assert obj.ping(1) == 1
    assert obj.ping(100) == 2
    assert obj.ping(3001) == 3
    assert obj.ping(3002) == 3
