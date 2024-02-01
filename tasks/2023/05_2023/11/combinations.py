import itertools


def decapitalize(s):
    if not s:
        return s
    return s[0].lower() + s[1:]


def password_combination(key_words):
    capitalize_list = [x.capitalize() for x in key_words if isinstance(x, str)]
    decapitalize_list = [decapitalize(x) for x in key_words if isinstance(x, str)]
    int_list = [str(x) for x in key_words if not isinstance(x, str)]

    result = [x for x in itertools.permutations({*decapitalize_list, *int_list})] + [
        x for x in itertools.permutations({*capitalize_list, *int_list})
    ]
    return ["".join(x) for x in result]


if __name__ == "__main__":
    print(*password_combination(key_words=["Michael", 25, "!", "@", 12]), sep="\n")
