from datetime import datetime, timedelta

DATE_FORMAT = "%H:%M:%S"


def process_trades(lines):
    result = []
    for line in lines:
        try:
            str_time, stock, price = line.split()
            price = float(price)
            time = datetime.strptime(str_time, DATE_FORMAT).time()
            ten_min_ago_time = (
                datetime.strptime(str_time, DATE_FORMAT) - timedelta(minutes=10)
            ).time()

            prices = {}
            for new_line in lines:
                try:
                    new_time, new_stock, new_price = new_line.split()
                    prices[new_stock] = prices.get(new_stock, [])
                    new_price = float(new_price)
                    if (
                        ten_min_ago_time <= datetime.strptime(new_time, DATE_FORMAT).time() <= time
                        and new_stock == stock
                    ):
                        prices.get(new_stock).append(new_price)
                except Exception:
                    pass

            low = min(prices.get(stock, [price]))
            high = max(prices.get(stock, [price]))
            average = round(sum(prices.get(stock, [price])) / len(prices.get(stock, [price])), 3)
            result.append(f"{str_time} {stock} {price:.2f} {low:.2f} {high:.2f} {average:.3f}")
        except Exception:
            result.append("ERROR")
    return result


if __name__ == "__main__":
    assert process_trades(
        [
            "10:00:01 IBM 137.00",
            "10:09:12 IBM 135.00",
            "10:09:12 IBM BANANA",
            "10:08:01 MSFT 270.55",
            "10:12:00 IBM 136.00",
        ]
    ) == [
        "10:00:01 IBM 137.00 137.00 137.00 137.000",
        "10:09:12 IBM 135.00 135.00 137.00 136.000",
        "ERROR",
        "10:08:01 MSFT 270.55 270.55 270.55 270.550",
        "10:12:00 IBM 136.00 135.00 136.00 135.500",
    ]
