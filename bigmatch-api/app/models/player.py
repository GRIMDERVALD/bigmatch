from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base
import uuid

class Player(Base):
    __tablename__ = "players"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tournament_id = Column(UUID(as_uuid=True), ForeignKey("tournaments.id"), nullable=False)
    name = Column(String(100), nullable=False)
    contact = Column(String(100), nullable=True)
    team_id = Column(UUID(as_uuid=True), ForeignKey("teams.id"), nullable=True)
    
    # Relations
    tournament = relationship("Tournament", back_populates="players")
    team = relationship("Team", back_populates="players")