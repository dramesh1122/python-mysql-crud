from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Employee(Base):

    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(String(100))

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        index=True
    )

    department: Mapped[str] = mapped_column(String(100))

    salary: Mapped[float]