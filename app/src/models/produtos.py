from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Produtos(Base):
    __tablename__ = 'produtos'
    id_produto = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    preco = Column(String, nullable=False)
    link = Column(String, nullable=False)
    id_data = Column(Integer, ForeignKey('datas.id_data'), nullable=False)

    data = relationship("Data", backref="produtos")
