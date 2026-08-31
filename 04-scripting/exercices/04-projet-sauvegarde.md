# Exercice 4 (Projet) — Le script de sauvegarde

Objectif : ta première vraie automatisation utile. Tu peux le faire en Bash ou
en Python, à toi de choisir.

## Cahier des charges

Écris un script qui :

1. prend en entrée le chemin d'un dossier à sauvegarder ;
2. crée une **archive compressée** de ce dossier ;
3. nomme l'archive avec la **date et l'heure** du moment
   (ex. `sauvegarde-2026-07-01_14h30.tar.gz`) ;
4. range l'archive dans un dossier `sauvegardes/` (créé s'il n'existe pas) ;
5. affiche un message de confirmation avec le chemin de l'archive créée ;
6. gère au moins une erreur : si le dossier à sauvegarder n'existe pas,
   afficher un message clair et s'arrêter proprement.

## Pour aller plus loin (facultatif)

- Supprimer automatiquement les sauvegardes de plus de X jours.
- Faire tourner ce script automatiquement chaque jour (cherche « cron » /
  « crontab » — c'est un excellent réflexe DevOps).

## Questions

- Comment génère-t-on une date formatée en Bash ? En Python ?
- Quelle commande crée une archive `.tar.gz` ?
- Comment vérifies-tu qu'un dossier existe avant d'agir ?

## Indices

- Bash : `tar -czf`, `date +%Y-%m-%d_%Hh%M`, une condition sur `-d`.
- Python : modules `os`, `datetime`, `tarfile` ou `shutil`.
- N'oublie pas de committer ton script sur Git une fois fini.
