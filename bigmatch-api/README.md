# BIGMATCH API

API FastAPI pour organiser des tournois de basket 2v2.

## 🚀 Démarrage rapide

### Avec Docker Compose (Recommandé)

```bash
# Démarrer tous les services
docker-compose up -d

# L'API sera disponible sur http://localhost:8000
# La documentation automatique sur http://localhost:8000/docs
```

### Installation manuelle

1. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

2. **Configurer la base de données**
```bash
# Créer le fichier .env
cp .env.example .env

# Démarrer PostgreSQL (ou utiliser une instance existante)
# Modifier l'URL dans .env si nécessaire
```

3. **Initialiser la base de données**
```bash
# Initialiser Alembic
alembic init alembic

# Créer la première migration
alembic revision --autogenerate -m "Initial migration"

# Appliquer les migrations
alembic upgrade head
```

4. **Démarrer l'API**
```bash
uvicorn app.main:app --reload
```

## 📖 Documentation

- **API Documentation**: http://localhost:8000/docs
- **Alternative docs**: http://localhost:8000/redoc

## 🏗️ Structure du projet

```
app/
├── main.py              # Point d'entrée FastAPI
├── database.py          # Configuration base de données
├── models/              # Modèles SQLAlchemy
│   ├── tournament.py
│   ├── player.py
│   ├── team.py
│   └── match.py
├── schemas/             # Schémas Pydantic
├── crud/                # Opérations CRUD
├── api/v1/              # Routes API
└── services/            # Logique métier
```

## 🎯 Endpoints principaux

### Tournois
- `POST /api/v1/tournaments/` - Créer un tournoi
- `GET /api/v1/tournaments/{id}` - Récupérer un tournoi
- `POST /api/v1/tournaments/{id}/create-pools` - Créer les poules
- `POST /api/v1/tournaments/{id}/start` - Démarrer le tournoi

### Joueurs
- `POST /api/v1/players/tournaments/{id}/players` - Ajouter un joueur
- `GET /api/v1/players/tournaments/{id}/players` - Liste des joueurs

### Équipes et Matchs
- `GET /api/v1/teams/tournaments/{id}/teams` - Liste des équipes
- `GET /api/v1/matches/tournaments/{id}/matches` - Liste des matchs
- `PUT /api/v1/matches/{id}` - Mettre à jour un match

## 🔄 Workflow typique

1. **Créer un tournoi**
2. **Ajouter des joueurs**
3. **Créer les poules** (répartition automatique)
4. **Démarrer le tournoi** (génération des matchs)
5. **Mettre à jour les scores**

## 🛠️ Technologies

- **FastAPI** - Framework web moderne
- **SQLAlchemy 2.0** - ORM Python
- **PostgreSQL** - Base de données
- **Pydantic** - Validation des données
- **Alembic** - Migrations de base de données