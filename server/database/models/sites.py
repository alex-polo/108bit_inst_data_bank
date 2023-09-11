import datetime

from sqlalchemy import Column, String, Boolean, func
from sqlalchemy.orm import mapped_column, Mapped

from database.models.base import Base


class Sites(Base):
    __tablename__ = 'sites'

    id: Mapped[int] = mapped_column(primary_key=True)
    system_name: Mapped[String] = Column(String(255), nullable=False, unique=True)
    # site_name: Mapped[String] = Column(String(255), nullable=False, unique=True)
    # url: Mapped[String] = Column(String(255), nullable=False, unique=False)
    # vendor_tag: Mapped[String] = Column(String(255), nullable=False, unique=False)
    # is_enabled: Mapped[Boolean] = Column(Boolean, nullable=False, default=True)
    # updated_on: Mapped[datetime.datetime] = mapped_column(default=func.now, onupdate=func.now)
    # created_on: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
