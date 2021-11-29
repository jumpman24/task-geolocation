from decimal import Decimal

from .schemas import Location
from .config import settings


def approximate_coordinate(coordinate: Decimal, accuracy: Decimal) -> Decimal:
    """
    Removes precision of the original location,
    by removing the "too accurate" part of the value.

    Resulting value can be interpreted as some area on the map,
    which width and length are roughly equal to ACCURACY_FACTOR.
    """
    if settings.accuracy:
        return coordinate - coordinate % accuracy
    return coordinate


def approximate_location(location: Location) -> Location:
    """
    Removes precision of the original location,
    by removing the "too accurate" part of the value.

    Resulting value can be interpreted as some area on the map,
    which width and length are roughly equal to ACCURACY_FACTOR.
    """

    return Location(
        lat=approximate_coordinate(location.lat, settings.accuracy),
        lon=approximate_coordinate(location.lon, settings.accuracy),
    )
