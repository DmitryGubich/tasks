# Board: "Travel", Pins: - ["Mountain", "Lake", "Lodge"]
# Board: "Decorations", Pins: - ["House", "Patio", "Lodge"]
# Board: "Paintings", Pins: - ["Picasso", "Lake", "Patio"]

from collections import deque, defaultdict


class RelationManager:
    def __init__(self, *, boards: dict) -> None:
        self.graph = defaultdict(list)

        for pins in boards.values():
            for i in range(len(pins)):
                for j in range(i + 1, len(pins)):
                    pin1, pin2 = pins[i], pins[j]
                    self.graph[pin1].append(pin2)
                    self.graph[pin2].append(pin1)

    def is_connected(self, *, pin1: str, pin2: str) -> bool:
        return bool(self._find_path(start=pin1, finish=pin2))

    def distance(self, *, pin1: str, pin2: str) -> int:
        return self._find_path(start=pin1, finish=pin2)

    def relations(self) -> dict:
        relation_mapping = {}
        all_pins = list(self.graph.keys())

        for i in range(len(all_pins)):
            for j in range(i + 1, len(all_pins)):
                pin1, pin2 = all_pins[i], all_pins[j]
                score = self._find_path(start=pin1, finish=pin2)
                if score is not None:
                    relation_mapping[(pin1, pin2)] = score
                    relation_mapping[(pin2, pin1)] = score
        return relation_mapping

    def _find_path(self, *, start: str, finish: str) -> int | None:
        if start == finish:
            return 0

        visited = set(start)
        queue = deque([(start, 0)])

        while queue:
            current_pin, distance = queue.popleft()

            for neighbor in self.graph[current_pin]:
                if neighbor == finish:
                    return distance + 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))

        return None


if __name__ == "__main__":
    boards = {
        "Travel": ["Mountain", "Lake", "Lodge"],
        "Decorations": ["House", "Patio", "Lodge"],
        "Paintings": ["Picasso", "Lake", "Patio"],
    }
    relation_manager = RelationManager(boards=boards)

    assert relation_manager.is_connected(pin1="Mountain", pin2="Patio") is True
    assert relation_manager.distance(pin1="Mountain", pin2="Lake") == 1
    print(relation_manager.relations())
