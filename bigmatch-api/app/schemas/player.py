from pydantic import BaseModel, UUID4
from typing import Optional

class PlayerCreate(BaseModel):
    name: str
    contact: Optional[str] = None

class PlayerUpdate(BaseModel):
    name: Optional[str] = None
    contact: Optional[str] = None
    team_id: Optional[UUID4] = None

class Player(BaseModel):
    id: UUID4
    tournament_id: UUID4
    name: str
    contact: Optional[str]
    team_id: Optional[UUID4]
    
    class Config:
        from_attributes = True