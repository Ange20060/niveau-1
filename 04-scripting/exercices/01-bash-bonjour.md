# Exercice 1 — Bash : dis-moi bonjour

Objectif : écrire, rendre exécutable et lancer ton premier script Bash.

## À faire

1. Crée un fichier `bonjour.sh` commençant par le shebang approprié.
2. Fais-lui afficher `Bonjour !`.
3. Rends-le exécutable et lance-le avec `./bonjour.sh`.
4. Modifie-le pour qu'il salue par un prénom passé en argument :
   `./bonjour.sh Alice` doit afficher `Bonjour Alice !`.
5. Ajoute un cas : si aucun prénom n'est donné, il affiche `Bonjour inconnu !`.

## Questions

- Que se passe-t-il si tu oublies de rendre le script exécutable ?
- Que contient `$1` ? Et `$0` ?
- Comment tester si un argument a été fourni ?

## Indices

- `#!/bin/bash`, `chmod +x`, `echo`, `$1`, une condition `if [ -z "$1" ]`.
