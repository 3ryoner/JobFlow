from datetime import datetime
from enum import StrEnum

from sqlalchemy import Text, func
from sqlalchemy.orm import Mapped, mapped_column

from jobflow.core.database import Base


class VacancyStatus(StrEnum):
    DRAFT = "draft"
    PUBLISHED = "published"
    CLOSED = "closed"


class Vacancy(Base):
    __tablename__ = "vacancies"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str] = mapped_column(Text)
    salary_min: Mapped[int | None]
    salary_max: Mapped[int | None]
    status: Mapped[VacancyStatus] = mapped_column(default=VacancyStatus.DRAFT)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )
