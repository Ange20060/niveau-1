# Exercice 2 — Parler HTTP à la main (curl)

Objectif : voir de tes yeux ce qu'est une requête et une réponse HTTP.
`curl` est un outil en ligne de commande qui fait des requêtes web.

## À faire

1. Fais une requête simple vers un site et observe le HTML renvoyé.
2. Affiche **uniquement les en-têtes** de la réponse (headers). Repère le code
   de statut.
3. Trouve une URL qui renvoie volontairement un code 404 et vérifie-le.
4. Interroge une API publique de test qui renvoie du JSON (cherche « API
   publique gratuite pour test », par ex. une API de blagues ou de météo) et
   observe la réponse.
5. Bonus : fais une requête `POST` avec des données.

## Questions

- Quelle est la différence entre une requête `GET` et une requête `POST` ?
- Où lit-on le code de statut dans la réponse ?
- Qu'est-ce qu'un en-tête (header) HTTP ? Donne deux exemples.

## Indices

- `curl` (options utiles : `-I` pour les en-têtes seuls, `-i` pour en-têtes +
  corps, `-X` pour la méthode, `-d` pour envoyer des données).
