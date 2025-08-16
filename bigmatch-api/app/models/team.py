from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base
import uuid

class Team(Base):
    __tablename__ = "teams"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tournament_id = Column(UUID(as_uuid=True), ForeignKey("tournaments.id"), nullable=False)
    pool_id = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    
    # Relations
    tournament = relationship("Tournament", back_populates="teams")
    players = relationship("Player", back_populates="team")
    home_matches = relationship("Match", foreign_keys="Match.team_a_id", back_populates="team_a")
    away_matches = relationship("Match", foreign_keys="Match.team_b_id", back_populates="team_b")