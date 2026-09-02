
### Comparaison des exercices 2 à 4 avec Docker Compose

Aux exercices 2 à 4, il fallait effectuer plusieurs commandes manuellement : construire l'image de l'API, créer et lancer PostgreSQL, créer un réseau Docker, connecter les conteneurs au réseau, configurer les variables d'environnement, gérer le volume et lancer les conteneurs.

Cela représentait facilement **une dizaine de commandes ou plus**, selon la manière de procéder.

Avec Docker Compose, toute cette configuration est décrite dans un seul fichier `docker-compose.yml`.

Il suffit principalement d'utiliser :

```bash
docker compose up -d
```

pour construire et démarrer l'ensemble des services.

Et pour arrêter et supprimer les conteneurs :

```bash
docker compose down
```

Docker Compose crée automatiquement le réseau et gère la connexion entre les services, les volumes, les variables d'environnement et les dépendances.

**L'intérêt principal de Docker Compose est donc de transformer plusieurs opérations manuelles en une configuration reproductible et une commande simple.** Cela facilite le déploiement, le développement en équipe et la reproduction du même environnement sur une autre machine.
