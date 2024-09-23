from sqlalchemy import Column, Integer, String, UniqueConstraint
from .base import Base

class Data(Base):
    __tablename__ = 'datas'
    id_data = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(String, nullable=False, unique=True)

    __table_args__ = (UniqueConstraint('data', name='_data_uc'),)
