from sqlalchemy import Column, String, DateTime, Integer, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base
import uuid

class Tournament(Base):
    __tablename__ = "tournaments"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(200), nullable=False)
    location = Column(String(500), nullable=False)
    date = Column(DateTime, nullable=False)
    organizer = Column(String(100), nullable=False)
    share_link = Column(String(100), unique=True, nullable=False)
    status = Column(String(20), default="setup")  # setup, pools, active, finished
    settings = Column(JSON, default={
        "teams_per_pool": 4,
        "matches_per_team": 3,
        "score_limit": 21,
        "time_limit": None
    })
    
    # Relations
    players = relationship("Player", back_populates="tournament", cascade="all, delete-orphan")
    teams = relationship("Team", back_populates="tournament", cascade="all, delete-orphan")
    matches = relationship("Match", back_populates="tournament", cascade="all, delete-orphan")