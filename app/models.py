import os

from sqlmodel import SQLModel, Field, create_engine


class Flight(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    origen: str
    destino: str
    precio: float


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///flights.db")
engine = create_engine(DATABASE_URL)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
