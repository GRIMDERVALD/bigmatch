from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import Tournament, Player, Team, Match
from app.crud import team as team_crud, match as match_crud
import random
from typing import List, Dict

class TournamentService:
    
    @staticmethod
    def get_tournament_stats(db: Session, tournament_id: str) -> Dict:
        """Récupérer les statistiques d'un tournoi"""
        total_players = db.query(func.count(Player.id)).filter(
            Player.tournament_id == tournament_id
        ).scalar()
        
        total_teams = db.query(func.count(Team.id)).filter(
            Team.tournament_id == tournament_id
        ).scalar()
        
        total_matches = db.query(func.count(Match.id)).filter(
            Match.tournament_id == tournament_id
        ).scalar()
        
        completed_matches = db.query(func.count(Match.id)).filter(
            Match.tournament_id == tournament_id,
            Match.status == "finished"
        ).scalar()
        
        return {
            "total_players": total_players or 0,
            "total_teams": total_teams or 0,
            "total_matches": total_matches or 0,
            "completed_matches": completed_matches or 0
        }
    
    @staticmethod
    def create_pools_and_teams(db: Session, tournament_id: str) -> Dict:
        """Créer les poules et répartir les joueurs en équipes"""
        tournament = db.query(Tournament).filter(Tournament.id == tournament_id).first()
        players = db.query(Player).filter(Player.tournament_id == tournament_id).all()
        
        if len(players) < 4:
            raise ValueError("Minimum 4 players required")
        
        teams_per_pool = tournament.settings.get("teams_per_pool", 4)
        players_per_team = 2  # Basket 2v2 pour simplicité
        
        # Calculer le nombre de poules nécessaires
        total_teams = len(players) // players_per_team
        total_pools = (total_teams + teams_per_pool - 1) // teams_per_pool
        
        # Mélanger les joueurs
        shuffled_players = players.copy()
        random.shuffle(shuffled_players)
        
        # Créer les équipes
        teams_created = []
        player_index = 0
        
        for pool_id in range(1, total_pools + 1):
            teams_in_pool = min(teams_per_pool, total_teams - len(teams_created))
            
            for team_num in range(teams_in_pool):
                team_name = f"Équipe {pool_id}-{team_num + 1}"
                
                # Créer l'équipe
                team = team_crud.create_team(db, {
                    "tournament_id": tournament_id,
                    "pool_id": pool_id,
                    "name": team_name
                })
                teams_created.append(team)
                
                # Assigner les joueurs à l'équipe
                for _ in range(players_per_team):
                    if player_index < len(shuffled_players):
                        player = shuffled_players[player_index]
                        player.team_id = team.id
                        player_index += 1
        
        # Mettre à jour le statut du tournoi
        tournament.status = "pools"
        db.commit()
        
        return {
            "pools_created": total_pools,
            "teams_created": len(teams_created),
            "players_assigned": player_index
        }
    
    @staticmethod
    def generate_matches(db: Session, tournament_id: str) -> List[Match]:
        """Générer tous les matchs du tournoi"""
        tournament = db.query(Tournament).filter(Tournament.id == tournament_id).first()
        teams = db.query(Team).filter(Team.tournament_id == tournament_id).all()
        
        # Grouper les équipes par poule
        pools = {}
        for team in teams:
            if team.pool_id not in pools:
                pools[team.pool_id] = []
            pools[team.pool_id].append(team)
        
        matches_created = []
        
        # Générer les matchs pour chaque poule
        for pool_id, pool_teams in pools.items():
            # Round-robin dans chaque poule
            for i in range(len(pool_teams)):
                for j in range(i + 1, len(pool_teams)):
                    match = match_crud.create_match(db, {
                        "tournament_id": tournament_id,
                        "pool_id": pool_id,
                        "team_a_id": pool_teams[i].id,
                        "team_b_id": pool_teams[j].id
                    })
                    matches_created.append(match)
        
        # Mettre à jour le statut du tournoi
        tournament.status = "active"
        db.commit()
        
        return matches_created