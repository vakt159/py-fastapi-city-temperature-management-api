from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from city.crud import get_all_cities, update_city, delete_city
from db.session import get_db
from city.schema import City, CityCreate

router = APIRouter()


@router.get("/cities/", response_model=List[City])
def get_cities(db: Annotated[Session, Depends(get_db)]):
    return get_all_cities(db)


@router.post("/cities/", response_model=City)
def create_city(db: Annotated[Session, Depends(get_db)], city_data: CityCreate):
    return create_city(db=db, city_data=city_data)


@router.get("/cities/{city_id}", response_model=City)
def get_city(city_id: int, db: Annotated[Session, Depends(get_db)]):
    result = get_city(db=db, city_id=city_id)

    if not result:
        raise HTTPException(status_code=404, detail="City not found")

    return result


@router.put("/cities/{city_id}", response_model=City)
def get_city(city_id: int,
             db: Annotated[Session, Depends(get_db)],
             city_data: CityCreate):
    city_to_update = get_city(db=db, city_id=city_id)

    if not city_to_update:
        raise HTTPException(status_code=404, detail="City not found")

    return update_city(db=db, city_id=city_id, city_data=city_data)


@router.delete("/cities/{city_id}", response_model=City)
def get_city(city_id: int, db: Annotated[Session, Depends(get_db)]):
    city_to_delete = get_city(db=db, city_id=city_id)

    if not city_to_delete:
        raise HTTPException(status_code=404, detail="City not found")

    return delete_city(db=db, city_id=city_id)
