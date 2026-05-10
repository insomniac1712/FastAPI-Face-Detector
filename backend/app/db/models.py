from sqlalchemy import Column, Integer, DateTime
from datetime import datetime

from app.db.database import Base


class ROI(Base):

    __tablename__ = "rois"

    id = Column(Integer, primary_key=True, index=True)

    x = Column(Integer, nullable=False)
    y = Column(Integer, nullable=False)

    width = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )