# Partie 06 — Docker & les conteneurs

C'est le cœur du DevOps moderne. Un **conteneur** permet d'empaqueter une
application avec tout ce dont elle a besoin, pour qu'elle tourne **exactement
pareil** sur n'importe quelle machine. Fini le « ça marche sur ma machine ».

Toutes les parties précédentes t'ont préparé à celle-ci : Linux (les conteneurs
sont du Linux), le réseau (les conteneurs communiquent par IP/ports), une
application (c'est ce qu'on va conteneuriser), et Git (pour versionner tes
fichiers).

## Objectifs

À la fin, tu sauras :
- expliquer la différence entre une image et un conteneur ;
- écrire un `Dockerfile` et construire ta propre image ;
- persister des données avec des volumes ;
- faire communiquer plusieurs conteneurs ;
- orchestrer une appli complète avec **Docker Compose**.

## Ce que tu dois apprendre

1. **Pourquoi les conteneurs.** Le problème qu'ils résolvent, et la différence
   avec une machine virtuelle (VM).
2. **Image vs conteneur.** L'image est le « modèle » (comme une classe), le
   conteneur est une instance qui tourne.
3. **Les commandes de base :** `docker run`, `docker ps`, `docker images`,
   `docker exec`, `docker stop`, `docker rm`, `docker logs`.
4. **Le Dockerfile :** `FROM`, `WORKDIR`, `COPY`, `RUN`, `EXPOSE`, `CMD`. La
   notion de **cache de build** et pourquoi l'ordre des instructions compte.
5. **Les volumes :** persister les données au-delà de la vie d'un conteneur.
   Différence volume nommé / bind mount.
6. **Les réseaux Docker :** comment deux conteneurs se parlent par leur nom.
7. **Docker Compose :** décrire plusieurs services dans un seul fichier
   `docker-compose.yml` et tout lancer d'une commande.

## Recherches à faire

- « conteneur vs machine virtuelle différence »
- « docker image vs conteneur »
- « dockerfile expliqué instructions »
- « docker cache de build ordre des couches »
- « docker volume persistance données »
- « docker réseau communication entre conteneurs »
- « docker compose tutoriel débutant »

## Le TP pratique

Cette partie s'appuie sur un **TP complet** déjà structuré : tu vas héberger une
mini API + une base de données, d'abord à la main puis avec Docker Compose.

Commence par lire les consignes générales, puis fais les exercices **dans
l'ordre** :

1. [exercice-1 — Prise en main](exercice-1-prise-en-main/CONSIGNES.md)
2. [exercice-2 — Ta première image](exercice-2-premiere-image/CONSIGNES.md)
3. [exercice-3 — Les données qui survivent](exercice-3-donnees/CONSIGNES.md)
4. [exercice-4 — Faire communiquer deux conteneurs](exercice-4-reseau/CONSIGNES.md)
5. [exercice-5 — Docker Compose](exercice-5-compose/CONSIGNES.md)
6. [bonus (facultatif)](bonus/CONSIGNES.md)

Le mini-code des applications (Python/Flask) est fourni dans les dossiers `app/`.
Note tout dans [NOTES.md](NOTES.md).

## Projet de la partie

L'aboutissement du TP : une commande `docker compose up` qui lance ton API et
sa base de données, avec réseau et volume, les mots de passe dans un `.env`.
Committe le tout sur Git.

## Auto-évaluation

Sans notes :
- Quelle est la différence entre une image et un conteneur ?
- Pourquoi met-on l'installation des dépendances AVANT la copie du code dans un
  Dockerfile ?
- Que se passe-t-il pour les données d'une base si on supprime son conteneur
  sans volume ?
- Pourquoi `localhost` ne marche pas pour joindre un autre conteneur ?
- Qu'apporte Docker Compose par rapport aux commandes `docker` à la main ?

➡️ Partie suivante : [07 — CI/CD](../07-ci-cd/)
