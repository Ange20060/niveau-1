# Exercice 1 — Ton premier workflow

Objectif : voir GitHub Actions se déclencher tout seul à chaque push.

## À faire

1. Dans un dépôt GitHub, crée le dossier `.github/workflows/`.
2. Ajoute un fichier `hello.yml` qui définit un workflow :
   - déclenché à chaque `push` ;
   - avec un job qui tourne sur un runner Ubuntu ;
   - dont l'unique étape affiche un message (ex. `echo "Salut depuis la CI !"`).
3. Pousse le fichier sur GitHub.
4. Va dans l'onglet **Actions** du dépôt et regarde ton workflow s'exécuter.
   Ouvre les logs et retrouve ton message.

## Questions

- Qu'est-ce qui a déclenché l'exécution ?
- Sur quelle machine ton `echo` s'est-il exécuté ? D'où vient-elle ?
- Quelle est la hiérarchie : workflow → ? → ? (retrouve les 3 niveaux)

## Indices

- La structure YAML tourne autour de : `on:`, `jobs:`, `runs-on:`, `steps:`.
- Recopie un exemple minimal trouvé dans la doc officielle, puis modifie-le
  pour bien comprendre chaque ligne (ne te contente pas de copier).
