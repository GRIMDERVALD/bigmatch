# 🏀 BIGMATCH - Application complète

Application complète pour organiser des tournois de basket 2v2 avec :
- **Backend FastAPI** (Python) pour l'API REST
- **Frontend React** (TypeScript) pour l'interface utilisateur

## 🚀 Démarrage rapide

### Option 1: Démarrer tout ensemble
```bash
npm install
npm run dev
```

### Option 2: Démarrer séparément

**Backend (API):**
```bash
cd bigmatch-api
docker-compose up -d
# API disponible sur http://localhost:8000
```

**Frontend (React):**
```bash
cd bigmatch-frontend  
npm install
npm run dev
# Frontend disponible sur http://localhost:5173
```

## 📁 Structure du projet

```
basketball-app/
├── bigmatch-api/          # Backend FastAPI
│   ├── app/               # Code Python
│   ├── docker-compose.yml
│   └── requirements.txt
├── bigmatch-frontend/     # Frontend React
│   ├── src/
│   ├── package.json
│   └── vite.config.ts
├── bruno-collection/      # Tests API avec Bruno
└── package.json          # Scripts globaux
```

## 🛠️ Technologies utilisées

### Backend
- **FastAPI** - Framework web moderne
- **SQLAlchemy 2.0** - ORM Python  
- **PostgreSQL** - Base de données
- **Docker** - Containerisation

### Frontend  
- **React 18** - Framework UI
- **TypeScript** - Type safety
- **Vite** - Build tool moderne
- **Tailwind CSS** - Styling
- **React Router** - Navigation
- **Axios** - HTTP client

## 🎯 Fonctionnalités

### ✅ Implémenté
- 🏆 Création de tournois
- 👥 Gestion des joueurs  
- 🔗 Partage par lien de tournoi
- 🏊 Formation automatique des poules
- ⚡ Interface responsive moderne
- 🧪 Tests API complets (Bruno)

### 🚧 En développement  
- 📊 Page de détails de tournoi
- 🏀 Gestion des matchs en temps réel
- 📈 Tableaux de scores et classements
- 📱 Mode mobile optimisé

## 🌐 URLs

- **Frontend**: http://localhost:5173
- **API**: http://localhost:8000  
- **Documentation API**: http://localhost:8000/docs
- **Base de données**: PostgreSQL sur port 5432

## 🧪 Tests

**Tester l'API avec Bruno:**
1. Ouvrir Bruno
2. Importer la collection `bruno-collection/`
3. Exécuter "Workflow - Complete Tournament"
4. Tester tous les endpoints

**Tester le Frontend:**
1. Aller sur http://localhost:5173
2. Créer un tournoi
3. Rejoindre avec le code de partage

## 🚀 Déploiement

**Production:**
```bash
# Build frontend
npm run build

# Deploy API  
cd bigmatch-api
docker build -t bigmatch-api .

# Deploy frontend
cd bigmatch-frontend  
npm run build
# Servir le dossier dist/
```

## 📋 Todo

- [ ] Page de gestion de tournoi complète
- [ ] Système de matchs en temps réel
- [ ] Notifications push  
- [ ] Mode hors ligne
- [ ] Export des résultats
- [ ] Statistiques avancées

---

🏀 **BIGMATCH** - La solution complète pour vos tournois de basket !
