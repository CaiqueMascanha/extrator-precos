from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

# Define a URL de conexão para o PostgreSQL
DATABASE_URL = str(os.getenv('DATABASE_URL'))

# Cria o engine do SQLAlchemy
engine = create_engine(DATABASE_URL)

# Cria a base declarativa
Base = declarative_base()

# Cria uma sessão
Session = sessionmaker(bind=engine)

class Precos(Base):
    __tablename__ = 'produtos'

    id_produto = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    link = Column(String, nullable=False)
    data = Column(DateTime, nullable=False)

# Cria a tabela no banco de dados
Base.metadata.create_all(engine)
