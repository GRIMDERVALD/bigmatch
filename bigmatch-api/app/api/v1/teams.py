from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas import team as schemas
from app.crud import team as crud

router = APIRouter(prefix="/teams", tags=["teams"])

@router.get("/tournaments/{tournament_id}/teams", response_model=List[schemas.Team])
def get_tournament_teams(tournament_id: str, db: Session = Depends(get_db)):
    """Récupérer toutes les équipes d'un tournoi"""
    teams = crud.get_teams_by_tournament(db, tournament_id=tournament_id)
    return teams

@router.get("/tournaments/{tournament_id}/pools/{pool_id}/teams", response_model=List[schemas.Team])
def get_pool_teams(tournament_id: str, pool_id: int, db: Session = Depends(get_db)):
    """Récupérer toutes les équipes d'une poule"""
    teams = crud.get_teams_by_pool(db, tournament_id=tournament_id, pool_id=pool_id)
    return teams

@router.get("/{team_id}", response_model=schemas.TeamWithPlayers)
def get_team(team_id: str, db: Session = Depends(get_db)):
    """Récupérer une équipe par ID avec ses joueurs"""
    team = crud.get_team(db, team_id=team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

@router.put("/{team_id}", response_model=schemas.Team)
def update_team(
    team_id: str,
    team_update: schemas.TeamUpdate,
    db: Session = Depends(get_db)
):
    """Mettre à jour une équipe"""
    team = crud.update_team(db=db, team_id=team_id, team_update=team_update)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team