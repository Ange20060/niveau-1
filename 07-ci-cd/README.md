# Partie 07 — Introduction à la CI/CD

CI/CD, c'est l'automatisation de ce qui se passe **après** que tu écris du code :
vérifier, tester, construire, et parfois déployer — automatiquement, à chaque
changement. C'est ici que tout ce que tu as appris se rejoint (Git, scripts,
Docker).

## Objectifs

À la fin, tu sauras :
- expliquer ce que veulent dire CI et CD ;
- lire et écrire un workflow simple avec **GitHub Actions** ;
- déclencher des tests automatiques à chaque `push` ;
- enchaîner : tester puis construire une image Docker.

## Ce que tu dois apprendre

1. **Les mots :**
   - **CI (Intégration Continue)** : à chaque changement de code, on
     l'intègre et on le vérifie automatiquement (build + tests).
   - **CD (Livraison / Déploiement Continu)** : on va plus loin en préparant
     (livraison) ou en poussant automatiquement (déploiement) la nouvelle
     version.

2. **Pourquoi c'est utile :** on détecte les erreurs tout de suite, on ne
   dépend plus d'une personne qui « déploie à la main », on livre souvent et
   sereinement.

3. **Le vocabulaire d'un pipeline :** *workflow*, *job*, *step*, *runner*,
   *déclencheur* (trigger, ex. « à chaque push »).

4. **GitHub Actions (l'outil pour débuter) :**
   - le dossier spécial `.github/workflows/` ;
   - un fichier de workflow en **YAML** ;
   - déclencher sur `push` / `pull_request` ;
   - exécuter des commandes (lancer un lint, des tests, un build Docker).

5. **Le YAML :** le format de configuration utilisé partout en DevOps. Attention
   à l'indentation (des espaces, jamais de tabulations).

## Recherches à faire

- « CI CD expliqué simplement »
- « intégration continue vs déploiement continu »
- « github actions tutoriel débutant »
- « github actions workflow yaml exemple »
- « github actions déclencheur on push »
- « syntaxe yaml débutant indentation »
- « pipeline CI job step runner définition »

## Exercices

Détails dans [exercices/](exercices/) :

1. **Ton premier workflow** — un workflow qui s'exécute à chaque push et
   affiche un message ([exercices/01-premier-workflow.md](exercices/01-premier-workflow.md)).
2. **Tester automatiquement** — lancer un test/lint à chaque push
   ([exercices/02-tests-auto.md](exercices/02-tests-auto.md)).
3. **Construire une image Docker en CI** — relier à la partie 06
   ([exercices/03-build-docker.md](exercices/03-build-docker.md)).

## Projet de la partie

Reprends ton projet Docker de la partie 06. Ajoute-lui un workflow GitHub
Actions qui, à chaque `push` : vérifie que l'image se construit correctement.
Bonus : fais échouer volontairement le build pour voir GitHub te signaler
l'erreur (croix rouge), puis corrige.

## Auto-évaluation

Sans notes :
- Que veulent dire CI et CD ? En quoi diffèrent-elles ?
- Où place-t-on les fichiers de workflow dans un dépôt GitHub ?
- Qu'est-ce qu'un déclencheur (trigger) ? Donne un exemple.
- Pourquoi l'indentation est-elle critique en YAML ?

➡️ Partie suivante : [08 — Cloud](../08-cloud/)
