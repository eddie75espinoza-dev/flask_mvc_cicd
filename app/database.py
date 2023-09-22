from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


db = SQLAlchemy()

# Configuración y lógica adicional de la base de datos, por ejemplo, conexión a PostgreSQL
engine = create_engine('postgresql://usuario:contraseña@localhost:5432/nombre_basedatos')
Session = sessionmaker(bind=engine)
Base = declarative_base()