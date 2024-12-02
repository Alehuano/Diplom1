from db import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
import task_m



class Manager(Base):
    __tablename__ = 'managers'
    # __table_args__ = {'extend_existing': True}
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    department = Column(String)

    tasks = relationship('Task', back_populates='manager')

# from sqlalchemy.schema import CreateTable
# print(CreateTable(Manager.__table__))
