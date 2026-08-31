# Exercice 2 — Jouer avec une API

Objectif : interroger une vraie API et comprendre la réponse.

## À faire

1. Trouve une API publique gratuite et sans authentification (cherche « API
   publique gratuite JSON » — ex. une API de blagues, de citations, de météo,
   ou l'API des utilisateurs de test « jsonplaceholder »).
2. Fais une requête `GET` dessus avec `curl` et observe le JSON renvoyé.
3. Identifie dans la réponse : les clés, les valeurs, la structure
   (objet, liste...).
4. Trouve une requête qui récupère **un seul élément** par son identifiant
   (ex. l'utilisateur numéro 3).
5. Bonus : refais la même chose depuis Postman (interface graphique) et
   compare l'expérience.

## Questions

- Quelle méthode HTTP utilises-tu pour **lire** des données ?
- Comment est structuré le JSON reçu ? Sais-tu retrouver une valeur précise
  dedans ?
- Que renvoie l'API si tu demandes un identifiant qui n'existe pas ?

## Indices

- `curl`, éventuellement passé dans un « formateur JSON » pour mieux lire
  (cherche « jq » ou un formateur JSON en ligne).
