from sqlalchemy.orm import Session
from app.models.team import Team
from app.schemas.team import TeamCreate, TeamUpdate
from typing import Optional, List, Dict

def get_team(db: Session, team_id: str) -> Optional[Team]:
    return db.query(Team).filter(Team.id == team_id).first()

def get_teams_by_tournament(db: Session, tournament_id: str) -> List[Team]:
    return db.query(Team).filter(Team.tournament_id == tournament_id).all()

def get_teams_by_pool(db: Session, tournament_id: str, pool_id: int) -> List[Team]:
    return db.query(Team).filter(
        Team.tournament_id == tournament_id,
        Team.pool_id == pool_id
    ).all()

def create_team(db: Session, team_data: Dict, tournament_id: str = None) -> Team:
    db_team = Team(
        tournament_id=tournament_id or team_data["tournament_id"],
        pool_id=team_data["pool_id"],
        name=team_data["name"]
    )
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

def update_team(
    db: Session, 
    team_id: str, 
    team_update: TeamUpdate
) -> Optional[Team]:
    team = get_team(db, team_id)
    if not team:
        return None
    
    update_data = team_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(team, key, value)
    
    db.commit()
    db.refresh(team)
    return team

def delete_team(db: Session, team_id: str) -> bool:
    team = get_team(db, team_id)
    if not team:
        return False
    
    db.delete(team)
    db.commit()
    return True