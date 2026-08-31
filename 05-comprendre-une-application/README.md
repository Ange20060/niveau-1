# Partie 05 — Comprendre une application

Pour déployer une application, il faut savoir de quoi elle est faite et comment
elle fonctionne. Tu n'as pas besoin de savoir la **développer** de A à Z, mais
tu dois comprendre ses **morceaux** et comment ils communiquent.

## Objectifs

À la fin, tu sauras :
- distinguer front-end, back-end et base de données ;
- expliquer ce qu'est une API et la tester ;
- lire et écrire des requêtes SQL simples ;
- comprendre le rôle des variables d'environnement et des fichiers de config.

## Ce que tu dois apprendre

1. **L'architecture d'une appli web :**
   - **Front-end** : ce que voit l'utilisateur (navigateur, HTML/CSS/JS).
   - **Back-end** : la logique côté serveur (traite les requêtes, applique les
     règles).
   - **Base de données** : là où les données sont stockées durablement.
   - Comment ces trois-là dialoguent.

2. **Les API :**
   - Ce qu'est une API (une interface pour que des programmes se parlent).
   - Le style **REST** et les méthodes HTTP (`GET`, `POST`, `PUT`, `DELETE`).
   - Le format **JSON** (le langage d'échange le plus courant).
   - Tester une API avec `curl` (revu en partie 02) ou **Postman**.

3. **Les bases de données :**
   - Différence entre base **relationnelle** (SQL) et **NoSQL** (culture
     générale).
   - SQL de base : `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`,
     `WHERE`.
   - Notion de table, ligne, colonne, clé primaire.

4. **Configuration :**
   - Variables d'environnement : pourquoi on ne met **jamais** de mot de passe
     en dur dans le code.
   - Fichiers de config, fichier `.env`.

## Recherches à faire

- « architecture application web front back base de données »
- « qu'est-ce qu'une API REST expliqué simplement »
- « méthodes HTTP GET POST PUT DELETE »
- « format JSON c'est quoi »
- « SQL pour débutant SELECT INSERT »
- « base de données relationnelle vs NoSQL »
- « pourquoi utiliser des variables d'environnement »
- « qu'est-ce qu'un fichier .env »

Entraînement recommandé : cherche un « tutoriel SQL interactif en ligne » pour
pratiquer les requêtes directement dans le navigateur.

## Exercices

Détails dans [exercices/](exercices/) :

1. **Disséquer une appli** — identifier front / back / BDD sur un exemple
   ([exercices/01-anatomie.md](exercices/01-anatomie.md)).
2. **Jouer avec une API** — interroger une API publique et lire du JSON
   ([exercices/02-api.md](exercices/02-api.md)).
3. **Premières requêtes SQL**
   ([exercices/03-sql.md](exercices/03-sql.md)).

## Projet de la partie

Choisis une application que tu utilises tous les jours (messagerie, réseau
social, site de streaming...) et décris dans ton `JOURNAL.md` : quel serait son
front-end, son back-end, ce que stockerait sa base de données, et deux ou trois
appels d'API qu'elle fait probablement. Pas besoin d'avoir raison à 100 %,
l'objectif est de raisonner en termes d'architecture.

## Auto-évaluation

Sans notes :
- Quelle est la différence entre le front-end et le back-end ?
- Qu'est-ce qu'une API, et à quoi sert le format JSON ?
- Écris une requête SQL qui récupère tous les utilisateurs dont la ville est
  « Paris ».
- Pourquoi ne met-on pas un mot de passe directement dans le code ?

➡️ Partie suivante : [06 — Docker](../06-docker/)
