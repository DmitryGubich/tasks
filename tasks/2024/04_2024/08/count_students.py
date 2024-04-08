from collections import deque


def count_students(students: list[int], sandwiches: list[int]) -> int:
    students = deque(students)
    sandwiches = deque(sandwiches)
    while sandwiches:
        student = students[0]
        sandwich = sandwiches[0]
        if student == sandwich:
            students.popleft()
            sandwiches.popleft()
        else:
            if sandwich not in students:
                break
            students.popleft()
            students.append(student)

    return len(students)


if __name__ == "__main__":
    assert count_students(students=[1, 1, 0, 0], sandwiches=[0, 1, 0, 1]) == 0
    assert (
        count_students(students=[1, 1, 1, 0, 0, 1], sandwiches=[1, 0, 0, 0, 1, 1]) == 3
    )
