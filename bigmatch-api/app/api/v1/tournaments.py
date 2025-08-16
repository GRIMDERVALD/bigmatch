from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas import tournament as schemas
from app.crud import tournament as crud
from app.services.tournament_service import TournamentService
import secrets

router = APIRouter(prefix="/tournaments", tags=["tournaments"])

@router.post("/", response_model=schemas.Tournament, status_code=status.HTTP_201_CREATED)
def create_tournament(
    tournament: schemas.TournamentCreate,
    db: Session = Depends(get_db)
):
    """Créer un nouveau tournoi"""
    # Générer un lien de partage unique
    share_link = secrets.token_urlsafe(8)
    
    db_tournament = crud.create_tournament(
        db=db, 
        tournament=tournament, 
        share_link=share_link
    )
    return db_tournament

@router.get("/{tournament_id}", response_model=schemas.TournamentWithStats)
def get_tournament(tournament_id: str, db: Session = Depends(get_db)):
    """Récupérer un tournoi par ID"""
    tournament = crud.get_tournament(db, tournament_id=tournament_id)
    if not tournament:
        raise HTTPException(status_code=404, detail="Tournament not found")
    
    # Ajouter les statistiques
    stats = TournamentService.get_tournament_stats(db, tournament_id)
    return {**tournament.__dict__, **stats}

@router.get("/share/{share_link}", response_model=schemas.Tournament)
def get_tournament_by_link(share_link: str, db: Session = Depends(get_db)):
    """Récupérer un tournoi par lien de partage"""
    tournament = crud.get_tournament_by_share_link(db, share_link=share_link)
    if not tournament:
        raise HTTPException(status_code=404, detail="Tournament not found")
    return tournament

@router.put("/{tournament_id}", response_model=schemas.Tournament)
def update_tournament(
    tournament_id: str,
    tournament_update: schemas.TournamentUpdate,
    db: Session = Depends(get_db)
):
    """Mettre à jour un tournoi"""
    tournament = crud.update_tournament(
        db=db, 
        tournament_id=tournament_id, 
        tournament_update=tournament_update
    )
    if not tournament:
        raise HTTPException(status_code=404, detail="Tournament not found")
    return tournament

@router.post("/{tournament_id}/create-pools")
def create_pools(tournament_id: str, db: Session = Depends(get_db)):
    """Créer les poules et équipes automatiquement"""
    tournament = crud.get_tournament(db, tournament_id=tournament_id)
    if not tournament:
        raise HTTPException(status_code=404, detail="Tournament not found")
    
    if tournament.status != "setup":
        raise HTTPException(status_code=400, detail="Pools already created")
    
    result = TournamentService.create_pools_and_teams(db, tournament_id)
    return {"message": "Pools created successfully", "pools": result}

@router.post("/{tournament_id}/start")
def start_tournament(tournament_id: str, db: Session = Depends(get_db)):
    """Démarrer le tournoi (générer les matchs)"""
    tournament = crud.get_tournament(db, tournament_id=tournament_id)
    if not tournament:
        raise HTTPException(status_code=404, detail="Tournament not found")
    
    if tournament.status != "pools":
        raise HTTPException(status_code=400, detail="Tournament not ready to start")
    
    matches = TournamentService.generate_matches(db, tournament_id)
    return {"message": "Tournament started", "matches_created": len(matches)}