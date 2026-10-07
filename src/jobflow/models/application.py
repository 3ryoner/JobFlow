from datetime import datetime
from enum import StrEnum
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from jobflow.core.database import Base

if TYPE_CHECKING:
    from jobflow.models import Candidate, Vacancy


class ApplicationStatus(StrEnum):
    SUBMITTED = "submitted"
    SCREENING = "screening"
    TECH_INTERVIEW = "tech_interview"
    OFFER = "offer"
    REJECTED = "rejected"


class Application(Base):
    __tablename__ = "applications"
    vacancy_id: Mapped[int] = mapped_column(ForeignKey("vacancies.id"))
    candidate_id: Mapped[int] = mapped_column(ForeignKey("candidates.id"))
    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[ApplicationStatus] = mapped_column(
        default=ApplicationStatus.SUBMITTED
    )
    cover_letter: Mapped[str | None] = mapped_column(Text, default=None)
    match_score: Mapped[float | None]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(onupdate=func.now())

    vacancy: Mapped["Vacancy"] = relationship()
    candidate: Mapped["Candidate"] = relationship()
