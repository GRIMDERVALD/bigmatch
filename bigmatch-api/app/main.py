from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import tournaments, players, teams, matches
from app.database import engine, Base

# Créer les tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="BIGMATCH API",
    description="API pour organiser des tournois de basket",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(tournaments.router, prefix="/api/v1")
app.include_router(players.router, prefix="/api/v1")
app.include_router(teams.router, prefix="/api/v1")
app.include_router(matches.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "BIGMATCH API", "version": "1.0.0"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}