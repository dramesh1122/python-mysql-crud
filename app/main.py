from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app import services
from app.schemas import (
    EmployeeCreate,
    EmployeeUpdate,
    EmployeeResponse
)

# Create MySQL tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Management API")


@app.get("/")
def home():
    return {"message": "Employee API is running"}


# CREATE
@app.post(
    "/employees",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED
)
def create_employee(
    data: EmployeeCreate,
    db: Session = Depends(get_db)
):
    return services.create_employee(
        db, data.model_dump()
    )


# READ ALL
@app.get(
    "/employees",
    response_model=list[EmployeeResponse]
)
def get_all_employees(
    db: Session = Depends(get_db)
):
    return services.get_all_employees(db)


# READ BY ID
@app.get(
    "/employees/{employee_id}",
    response_model=EmployeeResponse
)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    return services.get_employee(db, employee_id)


# UPDATE
@app.put(
    "/employees/{employee_id}",
    response_model=EmployeeResponse
)
def update_employee(
    employee_id: int,
    data: EmployeeUpdate,
    db: Session = Depends(get_db)
):
    return services.update_employee(
        db,
        employee_id,
        data.model_dump()
    )


# DELETE
@app.delete("/employees/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    return services.delete_employee(db, employee_id)