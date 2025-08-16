from pydantic import BaseModel, UUID4
from typing import Optional, List

class TeamCreate(BaseModel):
    name: str
    pool_id: int

class TeamUpdate(BaseModel):
    name: Optional[str] = None
    pool_id: Optional[int] = None

class Team(BaseModel):
    id: UUID4
    tournament_id: UUID4
    pool_id: int
    name: str
    
    class Config:
        from_attributes = True

class TeamWithPlayers(Team):
    players: List["Player"] = []
    
    class Config:
        from_attributes = True

# Import here to avoid circular imports
from .player import Player
TeamWithPlayers.model_rebuild()