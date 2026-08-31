# Exercice 2 — Rangement (fichiers et dossiers)

Objectif : créer, copier, déplacer et supprimer, entièrement au clavier.

## À faire

1. Crée cette structure en partant d'un dossier `atelier/` :
   ```
   atelier/
     documents/
     images/
     archives/
   ```
2. Crée trois fichiers texte vides dans `documents/` : `note1.txt`,
   `note2.txt`, `note3.txt`.
3. Écris une ligne de texte dans `note1.txt` **sans ouvrir d'éditeur**
   (cherche comment faire avec `echo` et une redirection).
4. Copie `note1.txt` dans `archives/`.
5. Déplace `note2.txt` et `note3.txt` dans `images/` en une seule commande.
6. Renomme `archives/note1.txt` en `archives/sauvegarde.txt`.
7. Supprime le dossier `images/` et tout son contenu.

## Questions

- Quelle commande sert à la fois à déplacer ET à renommer ? Pourquoi ?
- Quelle est la différence entre `>` et `>>` ?
- Comment supprimer un dossier non vide, et pourquoi est-ce dangereux ?

## Indices

- `mkdir` (cherche l'option pour créer plusieurs niveaux d'un coup),
  `touch`, `cp`, `mv`, `rm`, `echo`.
