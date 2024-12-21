class WorkItemProcessor:
    def __init__(self, start: int):
        self.highest_water_rank = start
        self.pending_acks = set()

    def process_ack(self, ack: int) -> None:
        if self.highest_water_rank + 1 == ack:
            self.highest_water_rank = ack
            while self.highest_water_rank + 1 in self.pending_acks:
                self.highest_water_rank += 1
                self.pending_acks.remove(self.highest_water_rank)
        elif ack > self.highest_water_rank + 1:
            self.pending_acks.add(ack)

    def get_highest_water_rank(self) -> int:
        return self.highest_water_rank


if __name__ == "__main__":
    processor = WorkItemProcessor(start=5)
    assert processor.get_highest_water_rank() == 5
    processor.process_ack(ack=8)
    assert processor.get_highest_water_rank() == 5
    processor.process_ack(ack=6)
    assert processor.get_highest_water_rank() == 6
