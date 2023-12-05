class HashTable:
    def __init__(self, size):
        self.data = [None] * size

    def _hash(self, key):
        hash_number = 0
        i = 0
        while i < len(key):
            hash_number = (hash_number + ord(key[i]) * i) % len(self.data)
            i += 1
        return hash_number

    def set(self, key, value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key, value])
        return self.data

    def get(self, key):
        address = self._hash(key)
        bucket = self.data[address]
        if bucket:
            for i in range(len(bucket)):
                if bucket[i][0] == key:
                    return bucket[i][1]
        return None

    def keys(self):
        keys_list = []
        for i in range(len(self.data)):
            if self.data[i]:
                if len(self.data) > 1:
                    for j in range(len(self.data[i])):
                        keys_list.append(self.data[i][j][0])
                else:
                    keys_list.append(self.data[i][0])

        return keys_list


if __name__ == "__main__":
    my_hash_table = HashTable(2)
    my_hash_table.set("grapes", 10000)
    assert my_hash_table.get("grapes") == 10000
    my_hash_table.set("apples", 9)
    my_hash_table.set("oranges", 2)
    assert my_hash_table.get("apples") == 9
    print(my_hash_table.keys())
