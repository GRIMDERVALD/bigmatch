# 🏀 BIGMATCH - Web App Mobile First

Application web mobile-first pour organiser des matchs de basket avec :
- **Backend FastAPI** (Python) pour l'API REST
- **Frontend** : À développer (React mobile-first)

## 🚀 Démarrage rapide

**Backend (API):**
```bash
cd bigmatch-api
docker-compose up -d
# API disponible sur http://localhost:8000
```

**Frontend :** 
À développer - React mobile-first avec Tailwind CSS

## 📁 Structure du projet

```
basketball-app/
├── bigmatch-api/          # Backend FastAPI
│   ├── app/               # Code Python
│   ├── docker-compose.yml
│   └── requirements.txt
├── bruno-collection/      # Tests API avec Bruno
└── package.json          # Scripts globaux
```

## 🛠️ Technologies utilisées

### Backend
- **FastAPI** - Framework web moderne
- **SQLAlchemy 2.0** - ORM Python  
- **PostgreSQL** - Base de données
- **Docker** - Containerisation

### Frontend (À développer)
- **React 18** - Framework UI mobile-first
- **TypeScript** - Type safety
- **Vite** - Build tool moderne
- **Tailwind CSS** - Styling responsive
- **React Router** - Navigation
- **Axios** - HTTP client

## 🎯 Fonctionnalités

### ✅ Backend API Implémenté
- 🏆 API création de tournois
- 👥 API gestion des joueurs  
- 🔗 API partage par lien de tournoi
- 🏊 API formation automatique des poules
- 🧪 Tests API complets (Bruno)

### 🚧 À développer  
- 📱 Interface mobile-first React
- 🏀 Gestion des matchs en temps réel
- 📈 Tableaux de scores et classements
- ⚡ Progressive Web App (PWA)

## 🌐 URLs

- **API**: http://localhost:8000  
- **Documentation API**: http://localhost:8000/docs
- **Base de données**: PostgreSQL sur port 5432

## 🧪 Tests

**Tester l'API avec Bruno:**
1. Ouvrir Bruno
2. Importer la collection `bruno-collection/`
3. Exécuter "Workflow - Complete Tournament"
4. Tester tous les endpoints

## 🚀 Déploiement

**Production:**
```bash
# Deploy API  
cd bigmatch-api
docker build -t bigmatch-api .
```

## 📋 Todo

- [ ] Créer le frontend React mobile-first
- [ ] Interface de création de match
- [ ] Système de scoring en temps réel
- [ ] Progressive Web App (PWA)
- [ ] Notifications push  
- [ ] Mode hors ligne
- [ ] Export des résultats

---

🏀 **BIGMATCH** - Web app mobile-first pour vos matchs de basket !
