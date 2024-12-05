from db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
import manager_m


class Task(Base):
    __tablename__ = 'tasks'
    #__table_args__ = {'keep_existing': True}
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    date = Column(String)
    payer = Column(String)
    sender = Column(String)
    recipient = Column(String)
    description = Column(Text)
    urgency = Column(String)
    invoice = Column(String)
    manager_id = Column(Integer, ForeignKey('managers.id'))

    manager = relationship('Manager', back_populates='tasks')

    def __str__(self):
        return f'{self.payer}{self.sender}{self.recipient}'
