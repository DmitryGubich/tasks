def is_number_valid(num):
    if 0 <= num < 2**20 - 1:
        return True
    else:
        return False


def word_machine(string: str):
    new_stack = []
    for command in string.split():
        if command.isdigit():
            new_stack.append(int(command))

        elif command == "DUP":
            if len(new_stack) > 0:
                x = new_stack.pop()
                new_stack.append(x)
                new_stack.append(x)
            else:
                return -1

        elif command == "POP":
            if len(new_stack) > 0:
                new_stack.pop()
            else:
                return -1

        elif command == "+":
            if len(new_stack) < 2:
                return -1
            else:
                x = new_stack.pop()
                y = new_stack.pop()
                res = x + y
                if is_number_valid(res):
                    new_stack.append(res)
                else:
                    return -1

        elif command == "-":
            if len(new_stack) < 2:
                return -1
            else:
                x = new_stack.pop()
                y = new_stack.pop()
                res = x - y
                if is_number_valid(res):
                    new_stack.append(res)
                else:
                    return -1

    if len(new_stack) == 0:
        return -1
    else:
        return new_stack.pop()


if __name__ == "__main__":
    assert word_machine(string="13 DUP 4 POP 5 DUP + DUP + -") == 7
    assert word_machine(string="10 10 +") == 20
