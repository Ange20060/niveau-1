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

# Exercice 1 — Prise en main Docker

## Image vs conteneur

Une **image Docker** est un modèle contenant ce qui est nécessaire pour créer et exécuter une application.

Un **conteneur** est une instance créée à partir d'une image et qui peut être démarrée, arrêtée ou supprimée.

On peut donc avoir plusieurs conteneurs créés à partir de la même image.

## `8080:80`

Dans :

```bash
docker run -p 8080:80 nginx
```

le premier nombre `8080` correspond au **port de ma machine**.

Le deuxième nombre `80` correspond au **port utilisé par Nginx à l'intérieur du conteneur**.

Docker fait donc la correspondance :

```text
Machine
localhost:8080
      │
      ▼
Docker
      │
      ▼
Conteneur
port 80
      │
      ▼
Nginx
```

On utilise `8080:80` parce que le port 80 du conteneur doit être accessible depuis un port de la machine.

Le port `80` seul ne permet pas de faire cette correspondance entre le port de la machine et celui du conteneur.
