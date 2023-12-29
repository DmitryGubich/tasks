class Stack:
    def __init__(self):
        self.array = []

    def push(self, value):
        self.array.append(value)

    def peek(self):
        return self.array[-1]

    def pop(self):
        return self.array.pop()

    def __len__(self):
        return len(self.array)

    def __str__(self):
        return " <- ".join(self.array)


if __name__ == "__main__":
    stack = Stack()
    stack.push("google")
    stack.push("udemy")
    stack.push("youtube")
    print("stack:", stack)  # google <- udemy <- youtube

    last_element = stack.peek()
    print(last_element)  # youtube
    print("stack:", stack)  # google <- udemy <- youtube

    remove_last_element = stack.pop()
    print(remove_last_element)  # youtube
    print("stack:", stack)  # google <- udemy

    stack.pop()
    print("stack:", stack)  # google
