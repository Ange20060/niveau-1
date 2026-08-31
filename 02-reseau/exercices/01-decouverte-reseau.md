# Exercice 1 — Explore ta machine

Objectif : manipuler les notions d'IP et de connectivité concrètement.

## À faire

1. Trouve l'adresse IP locale de ta machine.
2. Vérifie que tu as bien accès à Internet en « pingant » un site connu.
   Observe le temps de réponse.
3. Ping `localhost`. À quelle adresse ça correspond ? Pourquoi la réponse est-
   elle quasi instantanée ?
4. Essaie de résoudre un nom de domaine en IP (trouve l'IP derrière un site).

## Questions

- Quelle différence entre ton IP **locale** et ton IP **publique** ? Comment
  trouver ta publique ?
- Que fait la commande `ping` exactement ?
- Pourquoi `localhost` répond-il sans passer par Internet ?

## Indices

- Selon le système : `ip a` ou `ifconfig`, `ping`, `nslookup` ou `dig`.
- Pour l'IP publique : un site web du type « what is my IP », ou une commande
  qui interroge un service en ligne.
