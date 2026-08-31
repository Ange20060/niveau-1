# Partie 01 — Linux & la ligne de commande

C'est **le socle**. La quasi-totalité des serveurs tournent sous Linux, et tout
le travail DevOps se fait au terminal. Prends vraiment ton temps ici : chaque
heure investie maintenant t'en fera gagner dix plus tard.

## Objectifs

À la fin, tu sauras :

- naviguer et manipuler des fichiers entièrement au clavier ;
- comprendre l'arborescence Linux et les permissions ;
- enchaîner des commandes avec les pipes et les redirections ;
- gérer des processus et installer des logiciels.

## Prérequis : avoir un Linux sous la main

Tu as besoin d'un environnement Linux. Trois options (recherche « comment
installer » celle que tu choisis) :

- **WSL** si tu es sous Windows (le plus simple pour commencer).
- Une **machine virtuelle** (VirtualBox + Ubuntu).
- Une **double installation** ou un vrai PC sous Linux (plus tard).

## Ce que tu dois apprendre

Dans l'ordre :

1. **Se repérer :** `pwd`, `ls` (et ses options `-l`, `-a`, `-h`), `cd`,
   chemins absolus vs relatifs, `.` et `..`, `~`.
2. **L'arborescence Linux :** à quoi servent `/`, `/home`, `/etc`, `/var`,
   `/tmp`, `/bin`. Tout est fichier sous Linux.
3. **Manipuler fichiers et dossiers :** `mkdir`, `touch`, `cp`, `mv`, `rm`
   (attention, pas de corbeille !), `cat`, `less`, `head`, `tail`.
4. **Chercher :** `grep`, `find`, `wc`.
5. **Pipes et redirections :** `|`, `>`, `>>`, `<`. Comprendre comment on
   chaîne des commandes.
6. **Permissions :** lire un `ls -l`, comprendre `rwx`, `chmod`, `chown`,
   la différence entre root et un utilisateur normal, `sudo`.
7. **Processus :** `ps`, `top` ou `htop`, `kill`, la différence entre un
   programme au premier plan et en arrière-plan (`&`).
8. **Paquets :** installer/mettre à jour des logiciels avec `apt` (Debian/
   Ubuntu) ou `dnf` (Fedora).
9. **Variables d'environnement :** `echo $PATH`, `export`, à quoi sert le
   `PATH`.
10. **Éditer un fichier au terminal :** commence par `nano`. Tu apprendras
    `vim` plus tard (au minimum : comment y entrer et... comment en sortir).

## Recherches à faire

- « commandes Linux de base débutant »
- « arborescence système de fichiers Linux expliquée »
- « permissions Linux chmod rwx explication »
- « pipe et redirection bash exemples »
- « différence sudo et root »
- « gestionnaire de paquets apt tutoriel »
- « nano éditeur raccourcis »

Astuce à découvrir tôt : la commande `man` (ex. `man ls`) affiche le manuel
d'une commande. Apprends à le lire, c'est ta première source d'aide.

## Exercices

Les énoncés détaillés sont dans [exercices/](exercices/). En résumé :

1. **Chasse au trésor** — te déplacer dans l'arborescence et retrouver des
   fichiers ([exercices/01-navigation.md](exercices/01-navigation.md)).
2. **Rangement** — créer, copier, déplacer, supprimer une structure de dossiers
   ([exercices/02-fichiers.md](exercices/02-fichiers.md)).
3. **Détective** — utiliser `grep`, `find` et les pipes pour extraire de
   l'information ([exercices/03-recherche-pipes.md](exercices/03-recherche-pipes.md)).
4. **Gardien** — jouer avec les permissions
   ([exercices/04-permissions.md](exercices/04-permissions.md)).

## Projet de la partie

Sans utiliser la souris ni l'explorateur de fichiers graphique, organise un
dossier `projet-linux/` contenant une arborescence que tu inventes (par
thème), remplis quelques fichiers texte, puis écris dans ton `JOURNAL.md` la
liste exacte des commandes que tu as utilisées, dans l'ordre.

## Auto-évaluation

Sans notes :

- Quelle est la différence entre un chemin absolu et un chemin relatif ?
- Que fait `ls -l | grep ".txt"` ? Décompose.
- Que signifie `-rw-r--r--` ?
- Pourquoi faut-il se méfier de `rm` ?

➡️ Partie suivante : [02 — Réseau](../02-reseau/)
