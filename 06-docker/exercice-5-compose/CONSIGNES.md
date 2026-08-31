# Exercice 5 — Docker Compose

Objectif : tout ce que tu as fait à la main aux exercices 2, 3 et 4 (construire
l'image, lancer la base, créer le réseau, le volume, brancher les variables),
tu vas maintenant le décrire dans **un seul fichier** et le lancer en **une
seule commande**.

Le dossier `app/` contient la même API qu'à l'exercice 4. Un fichier
`.env.example` te montre les variables à utiliser.

## À faire

1. Crée ton fichier `.env` à partir de `.env.example` (et mets un vrai mot de
   passe).

2. Écris un `docker-compose.yml` à la racine de ce dossier qui définit **deux
   services** :
   - `db` : la base PostgreSQL, avec un **volume** pour persister les données
     et ses variables lues depuis le `.env`.
   - `api` : ton API, **construite** à partir du dossier `app/`, qui expose le
     port 5000 et reçoit les bonnes variables d'environnement pour joindre `db`.

3. Mets en place une **dépendance** : l'API ne doit pas démarrer avant la base.

4. Lance tout avec une seule commande, puis arrête tout proprement.

5. Vérifie sur `http://localhost:5000` que ça répond, puis supprime les
   conteneurs et relance : grâce au volume, les données doivent toujours être là.

## À noter dans NOTES.md

- Combien de commandes te fallait-il pour faire tourner l'ensemble aux
  exercices 2 à 4 ? Et maintenant avec Compose ? C'est ça tout l'intérêt.

## Indices

- Démarrer : `docker compose up` (ajoute `-d` pour le mode détaché).
- Arrêter et nettoyer : `docker compose down`.
- Mots-clés utiles dans le yaml : `services`, `build`, `image`, `ports`,
  `environment`, `volumes`, `depends_on`.
- Compose charge automatiquement le fichier `.env` du dossier courant.
- Pas besoin de créer un réseau à la main : Compose en crée un tout seul, et les
  services s'y joignent par leur **nom de service** (`db`).
