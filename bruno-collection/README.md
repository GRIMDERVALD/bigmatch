# Collection Bruno pour BIGMATCH API

Cette collection Bruno permet de tester complètement l'API BIGMATCH pour organiser des tournois de basket.

## 🚀 Démarrage

1. **Démarrer l'API**
   ```bash
   cd ../bigmatch-api
   docker-compose up -d
   ```

2. **Ouvrir Bruno** et importer cette collection
3. **Sélectionner l'environnement "Local"**

## 🎯 Workflow de test complet

### Ordre d'exécution recommandé :

1. **Health Check** - Vérifier que l'API fonctionne
2. **API Info** - Obtenir les informations de version

### Workflow Tournoi :

3. **Create Tournament** - Créer un nouveau tournoi
   - ✅ Sauvegarde automatiquement `tournament_id` et `share_link`

4. **Get Tournament** - Récupérer les détails du tournoi

5. **Get by Share Link** - Tester l'accès par lien de partage

### Ajouter des joueurs :

6. **Add Players** - Ajouter un joueur
   - 🔄 Exécuter 8 fois avec des noms différents :
     - Jordan Smith
     - Alex Johnson  
     - Taylor Brown
     - Morgan Davis
     - Casey Wilson
     - Riley Garcia
     - Avery Martinez
     - Quinn Anderson

7. **List Players** - Vérifier la liste des joueurs

### Organiser le tournoi :

8. **Create Pools** - Créer les poules automatiquement
   - ✅ Répartit les joueurs en équipes

9. **Start Tournament** - Démarrer le tournoi
   - ✅ Génère tous les matchs (round-robin)

10. **List Teams** - Voir les équipes créées
    - ✅ Sauvegarde automatiquement `team_id`

11. **List Matches** - Voir tous les matchs générés
    - ✅ Sauvegarde automatiquement `match_id`

### Gérer les matchs :

12. **Start Match** - Démarrer un match

13. **Update Score** - Mettre à jour le score en cours

14. **Finish Match** - Terminer le match avec score final
    - ✅ Détermine automatiquement le gagnant

## 🔧 Variables automatiques

Les variables suivantes sont automatiquement sauvegardées :

- `tournament_id` - ID du tournoi créé
- `share_link` - Lien de partage du tournoi  
- `player_id` - ID du dernier joueur ajouté
- `team_id` - ID de la première équipe
- `match_id` - ID du premier match

## ✅ Tests inclus

Chaque requête inclut des tests automatiques pour vérifier :

- ✅ Codes de statut HTTP corrects
- ✅ Structure des réponses JSON
- ✅ Présence des champs requis
- ✅ Logique métier (ex: minimum 4 joueurs)
- ✅ Cohérence des données

## 🎮 Conseils d'utilisation

1. **Mode séquentiel** : Exécutez les requêtes dans l'ordre pour un workflow complet

2. **Tests multiples** : Vous pouvez relancer "Create Tournament" pour tester plusieurs tournois

3. **Variables** : Les IDs sont automatiquement stockés, pas besoin de les copier manuellement

4. **Console** : Regardez la console Bruno pour voir les logs des scripts

## 🐛 Dépannage

- **Erreur 404** : Vérifiez que l'API est démarrée (`docker-compose up -d`)
- **Variables vides** : Relancez "Create Tournament" en premier
- **Tests échoués** : Vérifiez l'ordre d'exécution des requêtes