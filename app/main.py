from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import SQLBase, engine
from app.dependencies import get_db_session, check_token
from app.models import User, Location
from app.schemas import UserSchema, UserCreateSchema
from app.utils import approximate_location

SQLBase.metadata.create_all(bind=engine)  # create DB
app = FastAPI(debug=True)


@app.post("/user", response_model=UserSchema)
def create_user(data: UserCreateSchema, db: Session = Depends(get_db_session)):
    user = User(
        full_name=data.full_name,
        location=Location(lat=str(data.location.lat), lon=str(data.location.lon)),
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@app.get("/user/{user_id}", response_model=UserSchema)
def get_user(user_id: str, db: Session = Depends(get_db_session), is_admin: bool = Depends(check_token)):
    user: User = db.query(User).get(user_id)

    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    user_data: UserSchema = UserSchema.from_orm(user)

    if not is_admin:
        user_data.location = approximate_location(user_data.location)

    return user_data


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", reload=True, debug=True, host="0.0.0.0", port=8000)
