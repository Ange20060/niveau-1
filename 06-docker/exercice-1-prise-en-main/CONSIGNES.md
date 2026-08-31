# Exercice 1 — Prise en main

Objectif : se familiariser avec les commandes de base, sans rien construire
pour l'instant. On utilise une image toute prête : `nginx`.

## À faire

1. Lance un conteneur `nginx` qui sert sa page par défaut, accessible sur
   `http://localhost:8080`. Ouvre ton navigateur pour vérifier.

2. Trouve la commande pour voir les conteneurs **qui tournent**, puis celle
   pour voir **aussi ceux qui sont arrêtés**. Quelle est la différence ?

3. Entre **à l'intérieur** du conteneur nginx (ouvre un shell dedans) et
   affiche le contenu du fichier `/etc/nginx/nginx.conf`. Ressors du conteneur.

4. Arrête le conteneur, puis supprime-le. Vérifie qu'il n'apparaît plus.

## À noter dans NOTES.md

- Quelle est la différence entre une **image** et un **conteneur** ?
- Pourquoi on écrit `8080:80` et pas juste `80` ? Que représente chaque nombre ?

## Indices (si tu bloques)

- Les commandes utiles tournent autour de : `docker run`, `docker ps`,
  `docker exec`, `docker stop`, `docker rm`.
- Pour mapper un port : option `-p`.
- Pour entrer dans un conteneur : un `exec` avec un shell (`sh` ou `bash`).
