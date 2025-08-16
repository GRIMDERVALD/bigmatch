from sqlalchemy.orm import Session
from app.models.match import Match
from app.schemas.match import MatchCreate, MatchUpdate
from typing import Optional, List, Dict

def get_match(db: Session, match_id: str) -> Optional[Match]:
    return db.query(Match).filter(Match.id == match_id).first()

def get_matches_by_tournament(db: Session, tournament_id: str) -> List[Match]:
    return db.query(Match).filter(Match.tournament_id == tournament_id).all()

def get_matches_by_pool(db: Session, tournament_id: str, pool_id: int) -> List[Match]:
    return db.query(Match).filter(
        Match.tournament_id == tournament_id,
        Match.pool_id == pool_id
    ).all()

def create_match(db: Session, match_data: Dict, tournament_id: str = None) -> Match:
    db_match = Match(
        tournament_id=tournament_id or match_data["tournament_id"],
        pool_id=match_data["pool_id"],
        team_a_id=match_data["team_a_id"],
        team_b_id=match_data["team_b_id"]
    )
    db.add(db_match)
    db.commit()
    db.refresh(db_match)
    return db_match

def update_match(
    db: Session, 
    match_id: str, 
    match_update: MatchUpdate
) -> Optional[Match]:
    match = get_match(db, match_id)
    if not match:
        return None
    
    update_data = match_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(match, key, value)
    
    db.commit()
    db.refresh(match)
    return match

def delete_match(db: Session, match_id: str) -> bool:
    match = get_match(db, match_id)
    if not match:
        return False
    
    db.delete(match)
    db.commit()
    return True