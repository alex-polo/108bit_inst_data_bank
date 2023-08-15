from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Products(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
