from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


engine = create_engine('sqlite:///logistic1.db', echo=True)

SessionLocal = sessionmaker(bind=engine)
session=SessionLocal()


class Base(DeclarativeBase):
    pass
