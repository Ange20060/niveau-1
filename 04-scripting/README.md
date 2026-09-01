# Partie 04 — Le scripting (automatiser)

Le DevOps, c'est automatiser tout ce qui est répétitif. Ça passe par l'écriture
de scripts. On apprend deux choses : **Bash** (pour enchaîner des commandes
Linux) et **Python** (le langage roi de l'automatisation et des outils DevOps).

## Objectifs

À la fin, tu sauras :

- écrire un script Bash avec variables, conditions et boucles ;
- écrire un petit programme Python (variables, fonctions, fichiers) ;
- automatiser une tâche répétitive de bout en bout.

## Ce que tu dois apprendre

### Bash

1. Un script `.sh` : la ligne `#!/bin/bash` (shebang), le rendre exécutable.
2. Variables, lecture d'un argument (`$1`, `$2`), `read` pour demander une
   saisie.
3. Conditions (`if`, `test`/`[ ]`), comparaison de nombres et de chaînes.
4. Boucles (`for`, `while`).
5. Codes de retour (`$?`) : comment savoir si une commande a réussi.

### Python

1. Installer Python, lancer un script, utiliser l'interpréteur interactif.
2. Variables et types (texte, nombre, liste, dictionnaire).
3. Conditions et boucles.
4. Fonctions.
5. Lire et écrire un fichier.
6. Notion de module/bibliothèque et `import` (culture générale pour la suite).

> Ne cherche pas à devenir développeur Python. Tu as besoin de savoir
> **lire et écrire des scripts simples**. La maîtrise viendra avec l'usage.

## Recherches à faire

- « écrire un script bash débutant »
- « bash shebang c'est quoi »
- « bash variables arguments $1 »
- « bash boucle for while exemples »
- « code retour commande bash $? »
- « python pour débutant premier programme »
- « python lire écrire fichier »
- « bash ou python quand utiliser lequel »

## Exercices

Détails dans [exercices/](exercices/) :

1. **Bash : dis-moi bonjour** — variables et arguments
   ([exercices/01-bash-bonjour.md](exercices/01-bash-bonjour.md)).
2. **Bash : le trieur** — conditions et boucles sur des fichiers
   ([exercices/02-bash-boucle.md](exercices/02-bash-boucle.md)).
3. **Python : la calculatrice** — entrées, conditions, fonctions
   ([exercices/03-python-bases.md](exercices/03-python-bases.md)).
4. **Le script de sauvegarde** — le projet fil rouge de la partie
   ([exercices/04-projet-sauvegarde.md](exercices/04-projet-sauvegarde.md)).

## Projet de la partie

Écris un script (Bash **ou** Python, ton choix) qui **sauvegarde
automatiquement un dossier dans une archive datée** (voir exercice 4). C'est
ta première vraie automatisation DevOps.

## Auto-évaluation

Sans notes :

- À quoi sert le shebang `#!/bin/bash` ?
- Comment un script Bash récupère-t-il un argument passé en ligne de commande ?
- Écris (de tête) une boucle `for` en Bash ET en Python qui affiche les
  nombres de 1 à 5.
- Comment sais-tu qu'une commande a échoué dans un script ?

➡️ Partie suivante : [05 — Comprendre une application](../05-comprendre-une-application/)
