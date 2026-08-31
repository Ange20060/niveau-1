# Partie 03 — Git & le contrôle de version

Git, c'est le carnet de bord de tout projet informatique : il garde l'historique
de chaque changement, permet de revenir en arrière, et de travailler à plusieurs
sans s'écraser. **À partir de maintenant, tout ce que tu produis dans ce guide
doit aller sur Git.**

## Objectifs

À la fin, tu sauras :
- créer un dépôt, enregistrer des versions (commits) ;
- travailler avec des branches et fusionner ;
- utiliser GitHub (dépôt distant, pull requests) ;
- résoudre un conflit de fusion sans paniquer.

## Ce que tu dois apprendre

1. **Le concept.** Qu'est-ce qu'un contrôle de version ? Pourquoi c'est
   indispensable (historique, retour arrière, collaboration).

2. **Les 3 zones de Git.** Le répertoire de travail → la zone d'index
   (staging, `git add`) → le dépôt (`git commit`). Bien comprendre ce trajet
   est la clé pour ne jamais être perdu.

3. **Les commandes de base :**
   - `git init`, `git clone`
   - `git status` (à taper tout le temps !), `git diff`
   - `git add`, `git commit -m "message"`
   - `git log`
4. **Le dépôt distant :** `git remote`, `git push`, `git pull`, `git fetch`.
5. **Les branches :** `git branch`, `git switch` (ou `git checkout`),
   `git merge`. Pourquoi on ne travaille pas directement sur `main`.
6. **Les conflits :** ce qu'est un conflit de fusion, comment le lire et le
   résoudre.
7. **GitHub / GitLab :** créer un compte, un dépôt distant, lier ton dépôt
   local, ouvrir une **pull request** (demande de fusion).
8. **Bonnes pratiques :** écrire des messages de commit clairs, le rôle du
   `.gitignore` (ne pas versionner mots de passe, fichiers générés, etc.).

## Recherches à faire

- « contrôle de version c'est quoi »
- « git add commit push expliqué débutant »
- « les 3 zones de git staging area »
- « git branches tutoriel »
- « résoudre un conflit git »
- « créer un dépôt github et pousser son code »
- « bien écrire un message de commit »
- « à quoi sert un fichier .gitignore »

Ressource classique à connaître : le mini-jeu **« Learn Git Branching »**
(cherche ce nom) pour visualiser les branches.

## Exercices

Détails dans [exercices/](exercices/) :

1. **Premiers pas** — init, add, commit, log
   ([exercices/01-premiers-commits.md](exercices/01-premiers-commits.md)).
2. **Branches et fusion** — créer une branche, la fusionner
   ([exercices/02-branches.md](exercices/02-branches.md)).
3. **Provoquer et résoudre un conflit**
   ([exercices/03-conflit.md](exercices/03-conflit.md)).
4. **Sur GitHub** — pousser ton dépôt et ouvrir une pull request
   ([exercices/04-github.md](exercices/04-github.md)).

## Projet de la partie

Mets **tout ce guide** (tes réponses, ton `JOURNAL.md`, tes exercices des
parties précédentes) dans un dépôt Git, pousse-le sur ton GitHub. À partir de
là, prends l'habitude de committer à chaque fois que tu finis un exercice.

## Auto-évaluation

Sans notes :
- Explique le trajet d'un fichier depuis sa modification jusqu'au commit.
- Quelle est la différence entre `git add` et `git commit` ?
- Quelle est la différence entre `commit` et `push` ?
- Pourquoi travaille-t-on sur des branches plutôt que directement sur `main` ?
- Que mets-tu dans un `.gitignore` et pourquoi ?

➡️ Partie suivante : [04 — Scripting](../04-scripting/)
