# Exercice 2 — Branches et fusion

Objectif : comprendre pourquoi et comment on travaille sur des branches.

## À faire

1. Dans ton dépôt de l'exercice 1, crée une nouvelle branche `nouvelle-section`
   et bascule dessus.
2. Vérifie sur quelle branche tu es.
3. Ajoute un nouveau paragraphe au `README.md`, commit sur cette branche.
4. Reviens sur la branche `main`. Regarde le `README.md` : ton paragraphe est-
   il là ? Pourquoi ?
5. Fusionne `nouvelle-section` dans `main`.
6. Vérifie que le paragraphe est maintenant présent sur `main`, puis supprime
   la branche `nouvelle-section`.

## Questions

- Que représente une branche, concrètement ?
- Pourquoi ton paragraphe « disparaît » quand tu reviens sur `main` avant la
  fusion ?
- Dans un vrai projet, pourquoi ne pas tout faire sur `main` ?

## Indices

- `git branch`, `git switch` (ou `git checkout`), `git merge`,
  `git branch -d`.
