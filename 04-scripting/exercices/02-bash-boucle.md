# Exercice 2 — Bash : le trieur

Objectif : combiner boucles, conditions et commandes Linux.

## À faire

1. Crée un dossier de test avec plusieurs fichiers d'extensions différentes
   (`.txt`, `.log`, `.jpg`...).
2. Écris un script qui parcourt tous les fichiers du dossier et **affiche**,
   pour chacun, son nom et son extension.
3. Fais évoluer le script : il **range** chaque fichier dans un sous-dossier
   nommé d'après son extension (les `.txt` dans `txt/`, etc.). Crée le
   sous-dossier s'il n'existe pas.
4. Affiche à la fin combien de fichiers ont été rangés.

## Questions

- Comment parcourir tous les fichiers d'un dossier avec une boucle `for` ?
- Comment récupérer l'extension d'un nom de fichier ?
- Comment vérifier qu'un dossier existe avant de le créer ?

## Indices

- `for f in *; do ... done`, `mkdir -p`, `mv`, une variable compteur.
- Pour l'extension : cherche « bash extension fichier ${f##*.} ».
