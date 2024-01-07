def suitable_locations(center: list[int], d: int) -> int:
    def binary_search(left, right, flag):
        found = False
        while left <= right:
            middle = (left + right) // 2
            answer = sum(abs(c - middle) * 2 for c in center)

            if answer <= d:
                found = True
                if flag:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if flag:
                    left = middle + 1
                else:
                    right = middle - 1

        return left if found else 0

    left_corner = binary_search(left=min(center), right=max(center), flag=True)
    right_corner = binary_search(left=min(center), right=max(center), flag=False)

    return right_corner - left_corner


if __name__ == "__main__":
    assert suitable_locations(center=[2, 0, 3, -4], d=22) == 5
    assert suitable_locations(center=[-3, 2, 2], d=8) == 0
