from decimal import Decimal

import faker
import pytest

from app.utils import approximate_coordinate


fake = faker.Faker()


@pytest.mark.parametrize(
    "coordinate, accuracy, expected", [
        (Decimal("0.0"), Decimal("0.01"), Decimal("0.0")),
        (Decimal("0.0"), Decimal("10e-17"), Decimal("0.0")),
        (Decimal("0.0"), Decimal("180"), Decimal("0.0")),

        (Decimal("90.0"), Decimal("0.1"), Decimal("90.0")),
        (Decimal("90.0"), Decimal("180"), Decimal("0.0")),
        (Decimal("-90.0"), Decimal("0.1"), Decimal("-90.0")),
        (Decimal("-90.0"), Decimal("180"), Decimal("0.0")),

        (Decimal("123.4567890123456789"), Decimal("0.0000000000000001"), Decimal("123.4567890123456789")),
        (Decimal("123.4567890123456789"), Decimal("0.000000000001"), Decimal("123.456789012345")),
        (Decimal("123.4567890123456789"), Decimal("0.00000001"), Decimal("123.45678901")),
        (Decimal("123.4567890123456789"), Decimal("0.0001"), Decimal("123.4567")),
        (Decimal("123.4567890123456789"), Decimal("0.01"), Decimal("123.45")),
        (Decimal("123.4567890123456789"), Decimal("0.02"), Decimal("123.44")),
        (Decimal("123.4567890123456789"), Decimal("0.05"), Decimal("123.45")),
        (Decimal("123.4567890123456789"), Decimal("0.1"), Decimal("123.4")),
        (Decimal("123.4567890123456789"), Decimal("1.0"), Decimal("123.0")),
        (Decimal("123.4567890123456789"), Decimal("10.0"), Decimal("120.0")),
        (Decimal("123.4567890123456789"), Decimal("100.0"), Decimal("100.0")),
        (Decimal("123.4567890123456789"), Decimal("123.456789012345679"), Decimal("0.0")),
    ]
)
def test_approximate_coordinate(coordinate, accuracy, expected):
    assert approximate_coordinate(coordinate, accuracy) == expected
