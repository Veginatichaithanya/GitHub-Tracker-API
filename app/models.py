from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class Repository(Base):
    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True, index=True)
    repo_name = Column(String, index=True)
    github_url = Column(String)
    stars = Column(Integer)
    owner = Column(String)
    note = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
