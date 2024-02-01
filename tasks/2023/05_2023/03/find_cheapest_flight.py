def find_cheapest_flight(list_of_flights, start, end):
    flight_prices = []
    destinations = [start]

    for flight in list_of_flights:
        if flight.get("origin") == start:
            if flight.get("destination") == end:
                destinations.append(end) if end not in destinations else destinations
                flight_prices.append(flight.get("price"))
            else:
                con_destinations, con_price = find_cheapest_flight(
                    list_of_flights, flight.get("destination"), end
                )
                if con_destinations and con_price:
                    flight_prices.append(flight.get("price") + con_price)
                    destinations.extend(con_destinations)

    return destinations, min(flight_prices) if flight_prices else None


if __name__ == "__main__":
    flights = [
        {
            "origin": "a",
            "destination": "b",
            "price": 300,
        },
        {
            "origin": "b",
            "destination": "d",
            "price": 100,
        },
        {
            "origin": "c",
            "destination": "d",
            "price": 50,
        },
        {
            "origin": "c",
            "destination": "g",
            "price": 10,
        },
        {
            "origin": "a",
            "destination": "d",
            "price": 200,
        },
    ]
    assert find_cheapest_flight(list_of_flights=flights, start="a", end="d") == [
        "a",
        "b",
        "b",
    ], 200
