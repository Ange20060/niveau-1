# Exercice 3 — Détective (recherche et pipes)

Objectif : extraire de l'information en combinant des commandes.

## Préparation

Crée un fichier `journal.log` contenant plusieurs lignes, dont certaines
contiennent le mot `ERROR` et d'autres `INFO`. (Utilise `echo` avec `>>`, ou
`nano`.)

## À faire

1. Affiche uniquement les lignes qui contiennent `ERROR`.
2. Compte combien de lignes contiennent `ERROR`.
3. Affiche les lignes qui **ne** contiennent **pas** `INFO`.
4. Dans ton dossier personnel, trouve tous les fichiers qui se terminent par
   `.txt`.
5. Combine : liste le contenu d'un dossier et ne garde que les lignes qui
   contiennent `.log`, le tout en une seule commande avec un pipe.

## Questions

- Que fait le caractère `|` exactement ? D'où vient l'entrée de la commande de
  droite ?
- Quelle option de `grep` permet d'inverser la sélection ?
- Quelle est la différence entre `find` et `grep` ?

## Indices

- `grep` (options `-c`, `-v`, `-i`), `find`, `wc -l`, `ls`, `|`.
