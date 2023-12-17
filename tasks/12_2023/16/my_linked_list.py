class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value} -> {self.next}" if self.next else f"{self.value}"


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        node = Node(value)
        self.tail.next = node
        self.tail = node
        self.length += 1

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def insert(self, index, value):
        if index >= self.length:
            return self.append(value)

        if index == 0:
            return self.prepend(value)

        counter = 1
        current_node = self.head

        while not counter == index:
            current_node = current_node.next
            counter += 1

        new_node = Node(value)
        new_node.next = current_node.next
        current_node.next = new_node
        self.length += 1

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            return

        counter = 1
        current_node = self.head

        while not counter == index:
            current_node = current_node.next
            counter += 1

        node_to_remove = current_node.next
        current_node.next = node_to_remove.next
        self.length -= 1

    def reverse(self):
        self.tail = self.head
        first = self.head
        second = self.head.next

        while second:
            temp_node = second.next
            second.next = first
            first = second
            second = temp_node

        self.head.next = None
        self.head = first

    def __len__(self):
        return self.length

    def __str__(self):
        return str(self.head)


if __name__ == "__main__":
    my_linked_list = LinkedList(10)  # 10
    my_linked_list.append(5)  # 10 -> 5
    my_linked_list.append(16)  # 10 -> 5 -> 16
    my_linked_list.prepend(1)  # 1 -> 10 -> 5 -> 16
    print(my_linked_list)
    my_linked_list.insert(2, 99)  # 1 -> 10 -> 99 -> 5 -> 16
    print(my_linked_list)
    my_linked_list.remove(1)  # 1 -> 99 -> 5 -> 16
    print(my_linked_list)
    my_linked_list.remove(0)  # 99 -> 5 -> 16
    print(my_linked_list)
    my_linked_list.append(24)  # 99 -> 5 -> 16 -> 24
    print(my_linked_list)
    my_linked_list.reverse()  # 24 -> 16 -> 5 -> 99
    print(my_linked_list)
