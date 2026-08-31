# Exercice 1 — Premiers commits

Objectif : maîtriser le cycle de base add → commit → log.

## À faire

1. Crée un dossier `mon-premier-depot/` et transforme-le en dépôt Git.
2. Crée un fichier `README.md` avec quelques lignes.
3. Regarde l'état du dépôt. Le fichier est-il suivi ? Dans quelle zone ?
4. Ajoute le fichier à la zone d'index, puis fais ton premier commit avec un
   message clair.
5. Modifie le `README.md`, regarde la différence avec `git diff`, puis
   commit à nouveau.
6. Affiche l'historique des commits.

## Questions

- Après avoir modifié un fichier déjà commité, que dit `git status` ?
- Que se passe-t-il si tu fais `git commit` sans avoir fait `git add` avant ?
- À quoi sert `git diff` ?

## Indices

- `git init`, `git status`, `git add`, `git commit -m`, `git diff`, `git log`
  (essaie `git log --oneline`).
