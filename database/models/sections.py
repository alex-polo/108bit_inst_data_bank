from sqlalchemy.orm import mapped_column, Mapped

from database import Base


class Sections(Base):
    __tablename__ = 'sections'

    id: Mapped[int] = mapped_column(primary_key=True)
    # section_name
    # site_id
    # description
    # url

