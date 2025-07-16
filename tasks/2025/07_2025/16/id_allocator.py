class IDAllocator:
    def __init__(self):
        self.released = set()
        self.allocated = set()
        self.next_id = 0

    def allocate(self):
        if self.released:
            id_ = self.released.pop()
        else:
            id_ = self.next_id
            self.next_id += 1

        self.allocated.add(id_)
        return id_

    def release(self, id_):
        if id_ in self.allocated:
            self.allocated.remove(id_)
            self.released.add(id_)

    def is_allocated(self, id_):
        return id_ in self.allocated


class SpaceEfficientAllocator:

    def __init__(self, max_val):
        self.max_val = max_val
        self.bool_array = [False] * max_val

    def allocate(self):
        """Returns an unallocated id"""
        for id, value in enumerate(self.bool_array):
            if value is False:  # The id has not been allocated
                self.bool_array[id] = True
                return id
        raise ValueError("No ids available")

    def release(self, id):
        """Releases the id and allows it to be allocated"""
        if (not 0 <= id < self.max_val) or (self.bool_array[id] is True):
            raise ValueError(f"The id {id} cannot be released.")
        self.bool_array[id] = False


if __name__ == "__main__":
    alloc = IDAllocator()

    a = alloc.allocate()  # 0
    b = alloc.allocate()  # 1

    alloc.release(a)

    c = alloc.allocate()  # could be 0 (from released)
    print(c)
