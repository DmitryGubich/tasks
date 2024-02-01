from typing import List


def average_salary(salaries: List[int]) -> float:
    # salaries.sort()
    # return (sum(salaries) - salaries[0] - salaries[-1]) / (len(salaries) - 2)
    salaries.remove(max(salaries))
    salaries.remove(min(salaries))
    return sum(salaries) / len(salaries)


if __name__ == "__main__":
    assert average_salary(salaries=[4000, 3000, 1000, 2000]) == 2500.00000
    assert average_salary(salaries=[1000, 2000, 3000]) == 2000.00000
