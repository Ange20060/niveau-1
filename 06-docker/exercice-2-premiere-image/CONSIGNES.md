# Exercice 2 — Ta première image

Objectif : empaqueter une petite application dans une image Docker que tu
construis toi-même.

Le code de l'appli est fourni dans le dossier `app/`. C'est une mini API en
Python (Flask) qui répond « Hello » sur le port **5000**. Tu n'as pas besoin de
connaître Python : regarde juste le code, il est court.

## À faire

1. Écris un `Dockerfile` (à placer dans `app/`) qui construit l'image de cette
   appli. À toi de choisir l'image de base, d'installer les dépendances listées
   dans `requirements.txt`, et de lancer l'appli.

2. Construis l'image en la nommant `mon-api:v1`.

3. Lance-la et vérifie qu'elle répond bien sur `http://localhost:5000`.

4. Modifie le message dans `app.py`, reconstruis l'image, relance. Tu dois voir
   ton nouveau message.

## Le test du cache (important)

1. Dans ton Dockerfile, mets **volontairement** la copie du code *avant*
   l'installation des dépendances. Construis. Modifie le code. Reconstruis.
   Regarde le temps de build : Docker réinstalle-t-il les dépendances ?

2. Maintenant remets les lignes dans le « bon » ordre (dépendances d'abord,
   code ensuite). Refais le même test.

## À noter dans NOTES.md

- À quel moment Docker a réutilisé le cache, et à quel moment il a tout
  reconstruit ?
- Pourquoi l'ordre des instructions dans un Dockerfile a de l'importance ?

## Indices

- Instructions utiles : `FROM`, `WORKDIR`, `COPY`, `RUN`, `EXPOSE`, `CMD`.
- Pour installer les dépendances Python : `pip install -r requirements.txt`.
