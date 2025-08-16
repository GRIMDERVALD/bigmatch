from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional, List, Dict, Any

class TournamentSettings(BaseModel):
    teams_per_pool: int = 4
    matches_per_team: int = 3
    score_limit: Optional[int] = 21
    time_limit: Optional[int] = None

class TournamentCreate(BaseModel):
    name: str
    location: str
    date: datetime
    organizer: str
    settings: Optional[TournamentSettings] = TournamentSettings()

class TournamentUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    date: Optional[datetime] = None
    status: Optional[str] = None
    settings: Optional[TournamentSettings] = None

class Tournament(BaseModel):
    id: UUID4
    name: str
    location: str
    date: datetime
    organizer: str
    share_link: str
    status: str
    settings: Dict[str, Any]
    
    class Config:
        from_attributes = True

class TournamentWithStats(Tournament):
    total_players: int
    total_teams: int
    total_matches: int
    completed_matches: int