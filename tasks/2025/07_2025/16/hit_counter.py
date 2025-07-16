from collections import Counter


class HitCounter:
    def __init__(self):
        """
        Initialize the HitCounter with a Counter to keep track of timestamp occurrences.
        """
        self.hits = Counter()

    def hit(self, timestamp: int) -> None:
        """
        Record a hit at a given timestamp.
        Each hit increments the count for the specific timestamp.

        :param timestamp: The current timestamp (in seconds granularity).
        """
        self.hits[timestamp] += 1

    def get_hits(self, timestamp: int) -> int:
        """
        Retrieve the number of hits in the past 5 minutes (300 seconds) from the current timestamp.

        :param timestamp: The timestamp at which to get the number of hits.
        :return: Total number of hits in the last 5 minutes.
        """
        # Filter out the timestamps that are older than 5 minutes and sum their hit counts.
        return sum(count for time, count in self.hits.items() if time > timestamp - 300)


if __name__ == "__main__":
    timestamp = 10
    hit_counter = HitCounter()
    hit_counter.hit(timestamp)
    timestamp = 410
    hit_counter.hit(timestamp)
    assert hit_counter.get_hits(timestamp) == 1
