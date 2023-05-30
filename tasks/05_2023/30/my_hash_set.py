class MyHashSet:
    def __init__(self):
        self.my_hash_set = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.my_hash_set.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.my_hash_set.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.my_hash_set


if __name__ == "__main__":
    myHashSet = MyHashSet()
    myHashSet.add(1)  # set = [1]
    myHashSet.add(2)  # set = [1, 2]
    assert myHashSet.contains(1) is True  # return True
    assert myHashSet.contains(3) is False  # return False, (not found)
    myHashSet.add(2)  # set = [1, 2]
    assert myHashSet.contains(2) is True  # return True
    myHashSet.remove(2)  # set = [1]
    assert myHashSet.contains(2) is False  # return False, (already removed)
