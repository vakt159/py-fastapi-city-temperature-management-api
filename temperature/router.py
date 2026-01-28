from typing import Annotated

from fastapi.params import Depends
from fastapi.routing import APIRouter


from city import crud as city_crud
from db.session import get_db
from .crud import *
from temperature.schema import TemperatureRead
from services import weather

router = APIRouter()


@router.get("/temperatures/", response_model=TemperatureRead)
def get_all_temperatures(db: Annotated[Session, Depends(get_db)],
                         city_id: int = None):
    if city_id:
        return get_temperature_for_city(db, city_id)
    return get_temperatures(db)

@router.post("/temperature/update")
async def update(db: Annotated[Session, Depends(get_db)]):
    cities = city_crud.get_all_cities(db)
    results = []
    for city in cities:
        temp = await weather.get_weather(city.name)
        obj = update_temperatures(db, city.id, float(temp))
        results.append(obj)
    return results