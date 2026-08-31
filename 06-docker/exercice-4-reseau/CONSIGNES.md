# Exercice 4 — Faire communiquer deux conteneurs

Objectif : connecter ton API à la base de données. C'est l'exercice le plus
costaud, c'est normal de bloquer. Prends ton temps.

Le dossier `app/` contient une nouvelle version de l'API : elle se connecte à
PostgreSQL et affiche la liste des stagiaires enregistrés. Elle lit l'adresse
de la base dans des **variables d'environnement** (regarde le haut de `app.py`).

## À faire

1. Construis l'image de cette nouvelle API (comme à l'exercice 2, avec un
   Dockerfile).

2. Lance un conteneur PostgreSQL (réutilise ce que tu sais de l'exercice 3).

3. **Première tentative (qui va échouer) :** lance l'API en lui disant que la
   base est sur `localhost`. Regarde l'erreur. Pourquoi ça ne marche pas ?

4. Crée un **réseau Docker**, attache la base ET l'API dessus, et fais en sorte
   que l'API trouve la base **par son nom de conteneur** (pas par `localhost`,
   pas par une adresse IP).

5. Vérifie sur `http://localhost:5000` que l'API affiche bien les données.

## À noter dans NOTES.md

- Pourquoi `localhost` à l'intérieur d'un conteneur ne pointe-t-il PAS vers les
  autres conteneurs ? Vers quoi pointe-t-il alors ?

## Indices

- Crée un réseau : `docker network create ...`.
- Attache un conteneur à un réseau au lancement : option `--network`.
- Sur un réseau Docker, un conteneur est joignable par son **nom**
  (`--name`). C'est cette valeur que tu passes dans `DB_HOST`.
- Variables d'environnement attendues par l'API : `DB_HOST`, `DB_NAME`,
  `DB_USER`, `DB_PASSWORD`. Passe-les avec l'option `-e`.
