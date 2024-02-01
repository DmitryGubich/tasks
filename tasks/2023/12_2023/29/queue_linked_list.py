class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value} <- {self.next}" if self.next else f"{self.value}"


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, value):
        node = Node(value)

        if self.length == 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

        self.length += 1

    def peek(self):
        return self.first

    def dequeue(self):
        if self.length == 0:
            return None

        if self.first == self.last:
            self.last = None

        temp_node = self.first.next
        self.first = temp_node
        self.length -= 1
        return temp_node

    def __len__(self):
        return self.length

    def __str__(self):
        return str(self.first)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue("Joy")
    queue.enqueue("Arthur")
    queue.enqueue("Matt")
    print("queue:", queue)  # Matt -> Arthur -> Joy

    first_element = queue.peek()
    print(first_element.value)  # Joy
    print("queue:", queue)  # Matt -> Arthur -> Joy

    remove_first_element = queue.dequeue()
    print(remove_first_element.value)  # Joy
    print("queue:", queue)  # Matt -> Arthur

    queue.dequeue()
    print("queue:", queue)  # Matt
    queue.dequeue()
    print("queue:", queue)  # None
    queue.dequeue()
    print("queue:", queue)  # None
