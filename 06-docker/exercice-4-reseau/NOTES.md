# Exercice 4 — Faire communiquer deux conteneurs

## Pourquoi localhost ne fonctionne pas ?

`localhost` désigne toujours la machine ou le conteneur depuis lequel on effectue la connexion.

À l'intérieur du conteneur de l'API, `localhost` désigne donc le conteneur de l'API lui-même. Il ne désigne pas le conteneur PostgreSQL.

Pour faire communiquer deux conteneurs, ils doivent être connectés au même réseau Docker.

Sur ce réseau, Docker permet de joindre un conteneur en utilisant son nom.

Dans notre cas :

```text
API
 │
 │ DB_HOST=postgres-test
 ▼
postgres-test
 │
 ▼
PostgreSQL
```

L'API peut donc communiquer avec PostgreSQL sans connaître son adresse IP.

## À retenir

```text
localhost
   ↓
le conteneur actuel

nom-du-conteneur
   ↓
un autre conteneur du même réseau Docker
```
