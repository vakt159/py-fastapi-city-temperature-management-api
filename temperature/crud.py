from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import *

def get_temperatures(db:Session):
    return db.scalars(select(Temperature)).all()

def get_temperature_for_city(db:Session, city_id: int):
    return db.scalars(select(Temperature).where(Temperature.city_id==city_id)).all()

def update_temperatures(db:Session, city_id:int, temperature:float):
    temp = Temperature(city_id=city_id, temperature=temperature)
    db.add(temp)
    db.commit()
    db.refresh(temp)
    return temp
