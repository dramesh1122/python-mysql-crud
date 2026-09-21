from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app import repository


def create_employee(db: Session, data: dict):
    try:
        return repository.create_employee(db, data)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )


def get_all_employees(db: Session):
    return repository.get_all_employees(db)


def get_employee(db: Session, employee_id: int):
    employee = repository.get_employee_by_id(
        db, employee_id
    )

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


def update_employee(db: Session, employee_id: int, data: dict):
    employee = get_employee(db, employee_id)

    try:
        return repository.update_employee(db, employee, data)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )


def delete_employee(db: Session, employee_id: int):
    employee = get_employee(db, employee_id)

    repository.delete_employee(db, employee)

    return {"message": "Employee deleted successfully"}