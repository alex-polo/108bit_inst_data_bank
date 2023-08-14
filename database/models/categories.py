from sqlalchemy.orm import Mapped, mapped_column


class Categories:
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    # id
    # name
    # section_id
    # description
    # url