
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
