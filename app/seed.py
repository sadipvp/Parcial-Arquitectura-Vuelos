from sqlmodel import Session, delete

from models import Flight, engine, create_db_and_tables

vuelos = [
    Flight(origen="Bogota", destino="Madrid", precio=850.5),
    Flight(origen="Medellin", destino="Miami", precio=420.0),
    Flight(origen="Cali", destino="Lima", precio=210.75),
    Flight(origen="Bogota", destino="Buenos Aires", precio=540.0),
    Flight(origen="Cartagena", destino="Panama", precio=180.25),
    Flight(origen="Bogota", destino="Mexico DF", precio=470.9),
    Flight(origen="Medellin", destino="Madrid", precio=910.0),
    Flight(origen="Bogota", destino="Nueva York", precio=620.5),
    Flight(origen="Cali", destino="Santiago", precio=350.0),
    Flight(origen="Barranquilla", destino="Curazao", precio=150.0),
]


def seed():
    create_db_and_tables()
    with Session(engine) as session:
        session.exec(delete(Flight))
        session.add_all(vuelos)
        session.commit()
    print(f"{len(vuelos)} vuelos insertados")


if __name__ == "__main__":
    seed()
