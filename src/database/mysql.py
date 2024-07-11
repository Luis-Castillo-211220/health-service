# src/database/mysql.py
import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Leer la URL de la base de datos desde las variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

# Crear el motor de la base de datos asíncrono
engine = create_async_engine(DATABASE_URL, echo=True)

# Crear una sesión asíncrona
AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# Declarativa base para modelos ORM
Base = declarative_base()

# Dependencia que crea y cierra sesiones de la base de datos
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
