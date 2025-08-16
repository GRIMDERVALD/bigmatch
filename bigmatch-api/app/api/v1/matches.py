from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas import match as schemas
from app.crud import match as crud
from datetime import datetime

router = APIRouter(prefix="/matches", tags=["matches"])

@router.get("/tournaments/{tournament_id}/matches", response_model=List[schemas.MatchWithTeams])
def get_tournament_matches(tournament_id: str, db: Session = Depends(get_db)):
    """Récupérer tous les matchs d'un tournoi"""
    matches = crud.get_matches_by_tournament(db, tournament_id=tournament_id)
    return matches

@router.get("/tournaments/{tournament_id}/pools/{pool_id}/matches", response_model=List[schemas.MatchWithTeams])
def get_pool_matches(tournament_id: str, pool_id: int, db: Session = Depends(get_db)):
    """Récupérer tous les matchs d'une poule"""
    matches = crud.get_matches_by_pool(db, tournament_id=tournament_id, pool_id=pool_id)
    return matches

@router.get("/{match_id}", response_model=schemas.MatchWithTeams)
def get_match(match_id: str, db: Session = Depends(get_db)):
    """Récupérer un match par ID"""
    match = crud.get_match(db, match_id=match_id)
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    return match

@router.put("/{match_id}", response_model=schemas.Match)
def update_match(
    match_id: str,
    match_update: schemas.MatchUpdate,
    db: Session = Depends(get_db)
):
    """Mettre à jour un match (score, statut, etc.)"""
    match = crud.update_match(db=db, match_id=match_id, match_update=match_update)
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    return match

@router.post("/{match_id}/start")
def start_match(match_id: str, db: Session = Depends(get_db)):
    """Démarrer un match"""
    match_update = schemas.MatchUpdate(
        status="active",
        start_time=datetime.now()
    )
    match = crud.update_match(db=db, match_id=match_id, match_update=match_update)
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    return {"message": "Match started", "match_id": match_id}

@router.post("/{match_id}/finish")
def finish_match(
    match_id: str,
    score_a: int,
    score_b: int,
    db: Session = Depends(get_db)
):
    """Terminer un match avec le score final"""
    # Déterminer le gagnant
    winner_id = None
    match = crud.get_match(db, match_id)
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    
    if score_a > score_b:
        winner_id = match.team_a_id
    elif score_b > score_a:
        winner_id = match.team_b_id
    
    match_update = schemas.MatchUpdate(
        score_a=score_a,
        score_b=score_b,
        status="finished",
        winner_id=winner_id,
        end_time=datetime.now()
    )
    
    updated_match = crud.update_match(db=db, match_id=match_id, match_update=match_update)
    return {"message": "Match finished", "winner_id": winner_id}