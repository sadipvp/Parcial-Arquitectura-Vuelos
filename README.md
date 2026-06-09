# Sistema de Compra de Vuelos

API REST en FastAPI + SQLModel con base de datos PostgreSQL, todo orquestado con Docker Compose.

## Requisitos

- Docker y Docker Compose

## Levantar el proyecto

```bash
docker compose up -d --build
```

Esto arranca dos contenedores:

- `vuelos_app` → la API (FastAPI), expuesta en el puerto **8000**
- `vuelos_db` → PostgreSQL, expuesto en el puerto **5433** (host) → 5432 (contenedor)

## Poblar la base de datos (10 vuelos de ejemplo)

```bash
docker compose exec app python seed.py
```

## Endpoints

La IP pública del servidor es **`10.220.58.162`**. Reemplaza por `localhost` si lo pruebas desde la misma máquina.

| Método | Endpoint           | Descripción                  |
|--------|--------------------|------------------------------|
| GET    | `/vuelos`          | Lista todos los vuelos       |
| GET    | `/vuelos/{id}`     | Muestra un vuelo por su id   |
| POST   | `/vuelos`          | Crea un vuelo                |

### Documentación interactiva (Swagger)

```
http://10.220.58.162:8000/docs
```

### Ejemplos con `curl`

**Listar todos los vuelos:**
```bash
curl http://10.220.58.162:8000/vuelos
```

**Ver un vuelo por id:**
```bash
curl http://10.220.58.162:8000/vuelos/1
```

**Crear un vuelo:**
```bash
curl -X POST http://10.220.58.162:8000/vuelos \
  -H "Content-Type: application/json" \
  -d '{"origen": "Bogota", "destino": "Madrid", "precio": 850.5}'
```

## Comandos útiles

```bash
docker compose logs -f app     # ver logs de la API
docker compose ps              # estado de los contenedores
docker compose down            # detener (los datos persisten en el volumen pgdata)
docker compose down -v         # detener y borrar también la base de datos
```
