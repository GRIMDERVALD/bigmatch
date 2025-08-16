from sqlalchemy.orm import Session
from app.models.tournament import Tournament
from app.schemas.tournament import TournamentCreate, TournamentUpdate
from typing import Optional

def get_tournament(db: Session, tournament_id: str) -> Optional[Tournament]:
    return db.query(Tournament).filter(Tournament.id == tournament_id).first()

def get_tournament_by_share_link(db: Session, share_link: str) -> Optional[Tournament]:
    return db.query(Tournament).filter(Tournament.share_link == share_link).first()

def create_tournament(
    db: Session, 
    tournament: TournamentCreate, 
    share_link: str
) -> Tournament:
    db_tournament = Tournament(
        name=tournament.name,
        location=tournament.location,
        date=tournament.date,
        organizer=tournament.organizer,
        share_link=share_link,
        settings=tournament.settings.dict() if tournament.settings else {}
    )
    db.add(db_tournament)
    db.commit()
    db.refresh(db_tournament)
    return db_tournament

def update_tournament(
    db: Session, 
    tournament_id: str, 
    tournament_update: TournamentUpdate
) -> Optional[Tournament]:
    tournament = get_tournament(db, tournament_id)
    if not tournament:
        return None
    
    update_data = tournament_update.dict(exclude_unset=True)
    if "settings" in update_data:
        update_data["settings"] = update_data["settings"].dict()
    
    for key, value in update_data.items():
        setattr(tournament, key, value)
    
    db.commit()
    db.refresh(tournament)
    return tournament