from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas import player as schemas
from app.crud import player as crud

router = APIRouter(prefix="/players", tags=["players"])

@router.post("/tournaments/{tournament_id}/players", response_model=schemas.Player, status_code=status.HTTP_201_CREATED)
def create_player(
    tournament_id: str,
    player: schemas.PlayerCreate,
    db: Session = Depends(get_db)
):
    """Ajouter un joueur à un tournoi"""
    db_player = crud.create_player(db=db, player=player, tournament_id=tournament_id)
    return db_player

@router.get("/tournaments/{tournament_id}/players", response_model=List[schemas.Player])
def get_tournament_players(tournament_id: str, db: Session = Depends(get_db)):
    """Récupérer tous les joueurs d'un tournoi"""
    players = crud.get_players_by_tournament(db, tournament_id=tournament_id)
    return players

@router.get("/{player_id}", response_model=schemas.Player)
def get_player(player_id: str, db: Session = Depends(get_db)):
    """Récupérer un joueur par ID"""
    player = crud.get_player(db, player_id=player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player

@router.put("/{player_id}", response_model=schemas.Player)
def update_player(
    player_id: str,
    player_update: schemas.PlayerUpdate,
    db: Session = Depends(get_db)
):
    """Mettre à jour un joueur"""
    player = crud.update_player(db=db, player_id=player_id, player_update=player_update)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player

@router.delete("/{player_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_player(player_id: str, db: Session = Depends(get_db)):
    """Supprimer un joueur"""
    success = crud.delete_player(db, player_id=player_id)
    if not success:
        raise HTTPException(status_code=404, detail="Player not found")