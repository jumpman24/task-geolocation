from decimal import Decimal
from pydantic import BaseModel, condecimal


class Location(BaseModel):
    lat: condecimal(ge=Decimal(-90), le=Decimal(90))
    lon: condecimal(ge=Decimal(-180), le=Decimal(180))

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "lat": Decimal("34.5451978986"),
                "lon": Decimal("123.245235235"),
            }
        }


class UserCreateSchema(BaseModel):
    full_name: str
    location: Location

    class Config:
        schema_extra = {
            "example": {
                "full_name": "Vasiya Poupline",
                "location": Location.Config.schema_extra["example"],
            }
        }


class UserSchema(BaseModel):
    user_id: str
    full_name: str
    location: Location

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "full_name": "Vasiya Poupline",
                "user_id": "123",
                "location": Location.Config.schema_extra["example"],
            }
        }
