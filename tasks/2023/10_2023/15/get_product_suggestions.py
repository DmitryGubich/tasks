def get_product_suggestions(products, search):
    search_result = []
    search_param = ""

    for letter in search:
        search_param += letter
        result = []
        for product in products:
            if product.startswith(search_param):
                result.append(product)
        search_result.append(sorted(result)[:3])
        products = result

    return search_result


if __name__ == "__main__":
    assert get_product_suggestions(
        products=["carpet", "cart", "car", "camera", "crate"], search="camera"
    ) == [
        ["camera", "car", "carpet"],
        ["camera", "car", "carpet"],
        ["camera"],
        ["camera"],
        ["camera"],
        ["camera"],
    ]
    assert get_product_suggestions(products=["abcd", "abdc", "abaa", "acbd"], search="abad") == [
        ["abaa", "abcd", "abdc"],
        ["abaa", "abcd", "abdc"],
        ["abaa"],
        [],
    ]
    assert get_product_suggestions(products=["abcd", "abdc", "abaa", "acbd"], search="p") == [
        [],
    ]
    assert get_product_suggestions(products=["abcd", "abdc", "abaa", "acbd"], search="sp") == [
        [],
        [],
    ]
