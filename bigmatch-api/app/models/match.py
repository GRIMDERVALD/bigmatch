from sqlalchemy import Column, String, ForeignKey, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base
import uuid

class Match(Base):
    __tablename__ = "matches"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tournament_id = Column(UUID(as_uuid=True), ForeignKey("tournaments.id"), nullable=False)
    pool_id = Column(Integer, nullable=False)
    team_a_id = Column(UUID(as_uuid=True), ForeignKey("teams.id"), nullable=False)
    team_b_id = Column(UUID(as_uuid=True), ForeignKey("teams.id"), nullable=False)
    score_a = Column(Integer, default=0)
    score_b = Column(Integer, default=0)
    status = Column(String(20), default="pending")  # pending, active, finished
    winner_id = Column(UUID(as_uuid=True), ForeignKey("teams.id"), nullable=True)
    start_time = Column(DateTime, nullable=True)
    end_time = Column(DateTime, nullable=True)
    
    # Relations
    tournament = relationship("Tournament", back_populates="matches")
    team_a = relationship("Team", foreign_keys=[team_a_id], back_populates="home_matches")
    team_b = relationship("Team", foreign_keys=[team_b_id], back_populates="away_matches")
    winner = relationship("Team", foreign_keys=[winner_id])