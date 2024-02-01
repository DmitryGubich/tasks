def get_latest_k_requests(requests, K):
    result = []

    for request in reversed(requests):
        if len(result) >= K:
            break
        if request not in result:
            result.append(request)

    return result


if __name__ == "__main__":
    assert get_latest_k_requests(
        requests=["item1", "item2", "item2", "item1", "item3"], K=3
    ) == ["item3", "item1", "item2"]
    assert get_latest_k_requests(requests=["item1", "item2"], K=3) == ["item2", "item1"]
