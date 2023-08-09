from datetime import datetime

from sqlalchemy import Integer, Column, String, TIMESTAMP, ForeignKey

from database.main import Base


class SitesTags(Base):
    __tablename__ = 'sites_tags'

    id = Column(Integer, primary_key=True)
    site_id = Column(Integer, ForeignKey('sites.id'))
    name = Column(String(255), nullable=False, unique=True)
    updated_on = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_on = Column(TIMESTAMP, default=datetime.utcnow)
