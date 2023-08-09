from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean

from database.main import Base


class Sites(Base):
    __tablename__ = 'sites'

    id = Column(Integer, primary_key=True)
    system_name = Column(String(255), nullable=False, unique=True)
    site_name = Column(String(255), nullable=False, unique=True)
    url = Column(String(255), nullable=False, unique=False)
    vendor_tag = Column(String(255), nullable=False, unique=False)
    # field_tags = relan
    is_enabled = Column(Boolean, nullable=False, default=True)
    updated_on = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    created_on = Column(DateTime, default=datetime.now)
