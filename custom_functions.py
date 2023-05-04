import random


def custom_max(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value


def custom_most_common(numbers):
    # max(set(lst), key=lst.count)
    common = {}
    for number in numbers:
        if common.get(number) is None:
            common[number] = 1
        else:
            common[number] += 1

    most_common = next(iter(common))
    for key, value in common.items():
        if value > common[most_common]:
            most_common = key
    return most_common


def custom_average(numbers):
    sum = 0
    len = 0
    for i, number in enumerate(numbers):
        sum += number
        len = i + 1
    return sum / len


def custom_sort(numbers):
    if len(numbers) < 2:
        return numbers

    low, same, high = [], [], []
    pivot = numbers[random.randint(0, len(numbers) - 1)]

    for item in numbers:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return custom_sort(low) + same + custom_sort(high)


def main():
    numbers = [-11, 22, 13, 35, 65, 7, -6, 16, -16, 27, 78, 49]
    print("numbers:", numbers)
    print("max", custom_max(numbers))
    print("most common", custom_most_common(numbers))
    print("average", custom_average(numbers))
    print("sort", custom_sort(numbers))


if __name__ == "__main__":
    main()
