from fastapi import FastAPI
from sqlmodel import Session, select

from models import Flight, engine, create_db_and_tables

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/vuelos")
def crear_vuelo(vuelo: Flight):
    with Session(engine) as session:
        session.add(vuelo)
        session.commit()
        session.refresh(vuelo)
        return vuelo


@app.get("/vuelos")
def listar_vuelos():
    with Session(engine) as session:
        return session.exec(select(Flight)).all()


@app.get("/vuelos/{vuelo_id}")
def ver_vuelo(vuelo_id: int):
    with Session(engine) as session:
        return session.get(Flight, vuelo_id)
