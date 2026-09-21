from pydantic import BaseModel, ConfigDict, EmailStr


class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr
    department: str
    salary: float


class EmployeeUpdate(BaseModel):
    name: str
    email: EmailStr
    department: str
    salary: float


class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: str
    department: str
    salary: float

    model_config = ConfigDict(from_attributes=True)