from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Document(Base):
    __tablename__ = 'document'

    id: Mapped[int] = mapped_column(primary_key=True)