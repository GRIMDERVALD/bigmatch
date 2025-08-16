from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional

class MatchCreate(BaseModel):
    pool_id: int
    team_a_id: UUID4
    team_b_id: UUID4

class MatchUpdate(BaseModel):
    score_a: Optional[int] = None
    score_b: Optional[int] = None
    status: Optional[str] = None
    winner_id: Optional[UUID4] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None

class Match(BaseModel):
    id: UUID4
    tournament_id: UUID4
    pool_id: int
    team_a_id: UUID4
    team_b_id: UUID4
    score_a: int
    score_b: int
    status: str
    winner_id: Optional[UUID4]
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    
    class Config:
        from_attributes = True

class MatchWithTeams(Match):
    team_a: Optional["Team"] = None
    team_b: Optional["Team"] = None
    winner: Optional["Team"] = None
    
    class Config:
        from_attributes = True

# Import here to avoid circular imports
from .team import Team
MatchWithTeams.model_rebuild()