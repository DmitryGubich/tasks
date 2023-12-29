class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value} -> {self.next}" if self.next else f"{self.value}"


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, value):
        node = Node(value)

        if not self.top:
            self.top = node
            self.bottom = node
        else:
            temp_node = self.top
            self.top = node
            self.top.next = temp_node

        self.length += 1

    def peek(self):
        return self.top

    def pop(self):
        if not self.top:
            return None

        if self.top == self.bottom:
            self.bottom = None

        temp_node = self.top
        self.top = self.top.next
        self.length -= 1
        return temp_node

    def __len__(self):
        return self.length

    def __str__(self):
        return str(self.top)


if __name__ == "__main__":
    stack = Stack()
    stack.push("google")
    stack.push("udemy")
    stack.push("youtube")
    print("stack: ", stack)  # youtube -> udemy -> google

    last_element = stack.peek()
    print(last_element.value)  # youtube
    print("stack: ", stack)  # youtube -> udemy -> google

    remove_last_element = stack.pop()
    print(remove_last_element.value)  # youtube
    print("stack: ", stack)  # udemy -> google

    stack.pop()
    print("stack: ", stack)  # google
    stack.pop()
    print("stack: ", stack)  # None
    stack.pop()
    print("stack: ", stack)  # None
