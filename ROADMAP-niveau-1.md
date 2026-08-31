# Roadmap DevOps — Les fondations (niveau 1re année)

> L'objectif de cette première année n'est PAS d'apprendre le maximum d'outils,
> mais de construire des **bases solides**. Le DevOps, c'est d'abord bien
> comprendre comment une application vit, du code de développement jusqu'à la
> machine qui la fait tourner. Les outils à la mode (Kubernetes, Terraform,
> etc.) viendront après — et seront faciles si les fondations sont là.
>
> Conseil : ne passe pas à l'étape suivante tant que tu n'es pas capable
> d'expliquer l'étape en cours à quelqu'un d'autre.

---

## Étape 0 — La culture DevOps (à comprendre, pas à réviser)

Avant les outils, comprends *pourquoi* le DevOps existe.

- Ce que veut dire « Dev » + « Ops », et le problème que ça résout (le fameux
  « ça marche sur ma machine »).
- Les idées clés : automatiser ce qui est répétitif, livrer souvent et par
  petits pas, tout mettre sous contrôle de version, mesurer.

**Tu sais que c'est acquis quand :** tu peux expliquer en 2 minutes pourquoi une
entreprise adopte le DevOps.

---

## Étape 1 — Linux et la ligne de commande (LE socle)

C'est la base de tout. 90 % des serveurs tournent sous Linux et tout se fait au
terminal. À travailler en premier et sans se presser.

- Naviguer : `cd`, `ls`, `pwd`, arborescence des fichiers Linux.
- Manipuler fichiers/dossiers : `cp`, `mv`, `rm`, `mkdir`, `cat`, `less`.
- Rechercher : `grep`, `find`, les pipes `|` et les redirections `>` `>>`.
- Permissions : `chmod`, `chown`, comprendre `rwx`, root vs utilisateur.
- Processus : `ps`, `top`/`htop`, `kill`.
- Gérer des paquets (`apt` ou `dnf`), les variables d'environnement.
- Éditer un fichier en terminal (`nano` pour commencer, `vim` plus tard).

**Mini-projet :** installer une distribution Linux (dans une VM ou WSL) et y
faire tout le reste de la roadmap.

---

## Étape 2 — Les bases du réseau

On ne peut pas déployer sans comprendre comment les machines se parlent.

- Adresses IP, ports, différence client / serveur.
- Ce qu'est le DNS (nom de domaine → adresse IP).
- HTTP/HTTPS : requête, réponse, codes de statut (200, 404, 500...).
- SSH : se connecter à distance à un serveur (fondamental en DevOps).
- Notions de pare-feu (firewall).

**Tu sais que c'est acquis quand :** tu peux expliquer ce qui se passe, étape
par étape, quand tu tapes une URL dans un navigateur.

---

## Étape 3 — Git et le contrôle de version

Le carnet de bord de tout projet. Non négociable, à maîtriser tôt.

- `init`, `clone`, `add`, `commit`, `push`, `pull`, `status`, `log`.
- Les branches : `branch`, `checkout`/`switch`, `merge`, gérer un conflit.
- Utiliser GitHub / GitLab : dépôts distants, pull requests / merge requests.
- Écrire de bons messages de commit, comprendre le `.gitignore`.

**Mini-projet :** mettre tous ses TP sur un dépôt GitHub, travailler avec des
branches et fusionner proprement.

---

## Étape 4 — Le scripting (automatiser)

Le DevOps, c'est automatiser. Ça passe par le script.

- **Bash** : variables, conditions, boucles, arguments, écrire un script `.sh`.
- **Python** (bases) : c'est LE langage de l'automatisation et des outils DevOps.
  Variables, conditions, boucles, fonctions, lire/écrire un fichier.

**Mini-projet :** un script qui sauvegarde automatiquement un dossier dans une
archive datée.

---

## Étape 5 — Comprendre une application

Pour déployer une appli, il faut savoir comment elle est faite.

- Différence front-end / back-end / base de données.
- Ce qu'est une API et comment on la teste (`curl`, Postman).
- Bases des bases de données : SQL, une table, `SELECT`, `INSERT`.
- Variables d'environnement et fichiers de configuration.

**Mini-projet :** faire tourner localement une petite appli web + sa base de
données (par ex. le TP Docker déjà commencé).

---

## Étape 6 — Les conteneurs : Docker

Le cœur du DevOps moderne. C'est là qu'il en est déjà — parfait, cette étape
arrive au bon moment.

- Différence image / conteneur.
- Écrire un `Dockerfile`, construire une image, lancer un conteneur.
- Volumes (persistance des données), réseaux Docker.
- Orchestrer plusieurs conteneurs avec **Docker Compose**.

**Mini-projet :** le TP Docker (API + base de données lancées avec
`docker compose up`).

---

## Étape 7 — Introduction à la CI/CD

Automatiser les tests et le déploiement à chaque changement de code.

- Le principe : à chaque `push`, on teste (et éventuellement on déploie) tout
  seul.
- Découvrir **GitHub Actions** (le plus simple pour débuter) : écrire un
  workflow qui se lance à chaque push.
- Enchaîner : lancer des tests → construire une image Docker.

**Mini-projet :** un workflow GitHub Actions qui vérifie automatiquement le
code à chaque push.

---

## Étape 8 — Notions de cloud (survol)

Pour finir l'année en ouvrant sur la suite, sans entrer dans le détail.

- Ce qu'est le cloud, les grands acteurs (AWS, Azure, GCP), et l'idée de
  « payer ce qu'on utilise ».
- La différence entre une VM et un conteneur.
- Déployer sa petite appli sur un serveur distant accessible depuis Internet.

**Mini-projet :** mettre en ligne son appli conteneurisée sur un petit serveur
(offre gratuite d'un fournisseur cloud).

---

## Ce qui vient APRÈS (le niveau 2)

Une fois ces fondations posées, tout ça devient le programme du **[niveau 2](../niveau-2/)** :
Linux avancé & administration système, reverse proxy & TLS, automatisation
robuste, Docker en production, CI/CD avancé, Infrastructure as Code (Terraform,
Ansible), orchestration (Kubernetes), observabilité (Prometheus, Grafana) et
sécurité (DevSecOps). Voir [niveau-2/ROADMAP-niveau-2.md](../niveau-2/ROADMAP-niveau-2.md).

---

## Règles d'or pour l'année

1. **La pratique avant la théorie.** Chaque notion doit se terminer par un
   petit projet concret.
2. **Tout sur Git.** Chaque exercice, chaque script, chaque projet.
3. **Lire les messages d'erreur.** 80 % des réponses y sont déjà.
4. **Un fichier de notes personnel** où il réexplique chaque notion avec ses
   propres mots.
5. **Ne pas courir après les outils.** Comprendre > accumuler.
