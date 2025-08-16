from sqlalchemy.orm import Session
from app.models.player import Player
from app.schemas.player import PlayerCreate, PlayerUpdate
from typing import Optional, List

def get_player(db: Session, player_id: str) -> Optional[Player]:
    return db.query(Player).filter(Player.id == player_id).first()

def get_players_by_tournament(db: Session, tournament_id: str) -> List[Player]:
    return db.query(Player).filter(Player.tournament_id == tournament_id).all()

def create_player(db: Session, player: PlayerCreate, tournament_id: str) -> Player:
    db_player = Player(
        tournament_id=tournament_id,
        name=player.name,
        contact=player.contact
    )
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def update_player(
    db: Session, 
    player_id: str, 
    player_update: PlayerUpdate
) -> Optional[Player]:
    player = get_player(db, player_id)
    if not player:
        return None
    
    update_data = player_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(player, key, value)
    
    db.commit()
    db.refresh(player)
    return player

def delete_player(db: Session, player_id: str) -> bool:
    player = get_player(db, player_id)
    if not player:
        return False
    
    db.delete(player)
    db.commit()
    return True