class MyList:
    def __init__(self):
        self.length = 0
        self.data = []

    def get(self, index):
        return self.data[index]

    def append(self, element):
        self.data.append(element)
        self.length += 1

    def pop(self, index=0):
        if index:
            for i in range(index, self.length - 1):
                self.data[i] = self.data[index + 1]
        del self.data[self.length - 1]
        self.length -= 1

    def insert(self, index, element):
        last_item = self.data[self.length - 1]
        for i in range(self.length - 1, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = element
        self.append(last_item)

    def __len__(self):
        return self.length

    def __str__(self):
        return f'[{", ".join(str(x) for x in self.data)}]'


if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(0)
    print(my_list, len(my_list))
    print(my_list.get(1))
    my_list.pop()
    print(my_list, len(my_list))
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    my_list.append(5)
    print(my_list, len(my_list))
    my_list.pop(4)
    print(my_list, len(my_list))
    my_list.insert(1, 5)
    print(my_list, len(my_list))
