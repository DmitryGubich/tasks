from datetime import datetime, timedelta

from ryanair import Ryanair
from ryanair.types import Flight

api = Ryanair("PLN")


def parse_ryanair_flights(from_airport: str, to_airport: str) -> None:
    tomorrow = datetime.today().date() + timedelta(days=1)
    month = tomorrow + timedelta(days=30)
    flight: Flight = api.get_cheapest_flights(
        airport=from_airport,
        date_from=tomorrow,
        date_to=month,
        destination_airport=to_airport,
    )[0]
    return_flight: Flight = api.get_cheapest_flights(
        airport=to_airport,
        date_from=month,
        date_to=month + timedelta(days=30),
        destination_airport=from_airport,
    )[0]
    print(
        f"The cheapest flight from '{flight.originFull}' to '{flight.destinationFull}' is on {flight.departureTime} ({flight.price} PLN).\n"
        f"The cheapest return flight is on {return_flight.departureTime} ({return_flight.price} PLN)."
    )


if __name__ == "__main__":
    parse_ryanair_flights(from_airport="WAW", to_airport="VIE")
