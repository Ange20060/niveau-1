# Exercice 3 — Les données qui survivent

Objectif : comprendre pourquoi les données d'un conteneur disparaissent par
défaut, et comment les rendre persistantes avec un **volume**.

On utilise une base PostgreSQL (image officielle `postgres`). Pas besoin
d'être un pro de SQL, deux commandes suffisent.

## Partie A — La mauvaise surprise

1. Lance un conteneur PostgreSQL avec un mot de passe (voir indices).
2. Connecte-toi à la base et crée une table simple, puis ajoute 2 ou 3 lignes.

   Exemple une fois connecté avec `psql` :
   ```sql
   CREATE TABLE stagiaires (id SERIAL PRIMARY KEY, nom TEXT);
   INSERT INTO stagiaires (nom) VALUES ('Alice'), ('Karim');
   SELECT * FROM stagiaires;
   ```
3. Supprime le conteneur, puis recrée-en un nouveau de la même façon.
   Reconnecte-toi : ta table est-elle là ?

## Partie B — Avec un volume

4. Recommence toute la manip, mais cette fois en attachant un **volume** au
   conteneur (sur le dossier où Postgres stocke ses données :
   `/var/lib/postgresql/data`).
5. Recrée les données, supprime le conteneur, recrée-le **en réutilisant le
   même volume**. Tes données doivent survivre.

## À noter dans NOTES.md

- Quelle est la différence entre un **volume** et un **bind mount** ?
- Dans quel cas utiliserais-tu l'un plutôt que l'autre ?

## Indices

- Variables d'environnement utiles pour Postgres : `POSTGRES_PASSWORD`,
  `POSTGRES_USER`, `POSTGRES_DB`.
- Pour se connecter : `docker exec -it <conteneur> psql -U postgres`.
- Pour un volume nommé : option `-v nom_du_volume:/chemin/dans/le/conteneur`.
- Pour lister / supprimer les volumes : `docker volume ls`, `docker volume rm`.
