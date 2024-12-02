from pydantic import BaseModel


class CreateTask(BaseModel):
    date: str
    payer: str
    sender: str
    recipient: str
    description: str
    urgency: str
    invoice: str
    manager: int

class UpdateTask(BaseModel):
    payer: str
    sender: str
    recipient: str
    description: str
    urgency: str
    invoice: str
    manager: int

class CreateManager(BaseModel):
    name: str
    department: str

class UpdateManager(BaseModel):
    name: str
    department: str

