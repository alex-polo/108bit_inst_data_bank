from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, TIMESTAMP, func
from sqlalchemy.orm import mapped_column, Mapped

from database.models.base import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    update_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=func.now, onupdate=func.now, nullable=False)
    create_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=func.now, nullable=False)

# class User(SQLAlchemyBaseUserTable[int], Base):
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
#     hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
#     is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
#     # is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
#     # is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
#     update_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=func.now, onupdate=func.now, nullable=False)
#     create_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=func.now, nullable=False)

# class User(SQLAlchemyBaseUserTable[int], Base):
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
