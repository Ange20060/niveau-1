# Exercice 3 — Construire une image Docker en CI

Objectif : relier la CI (partie 07) et Docker (partie 06).

## À faire

1. Mets ton projet Docker de la partie 06 (avec son `Dockerfile`) dans un dépôt
   GitHub.
2. Crée un workflow qui, à chaque push, **construit l'image Docker** de ton
   API pour vérifier qu'elle se construit sans erreur.
3. Pousse et vérifie dans l'onglet Actions.
4. Introduis une faute dans le `Dockerfile` (ex. une dépendance mal écrite),
   pousse, et observe l'échec du build. Puis corrige.

## Pour aller plus loin (facultatif)

- Publier automatiquement l'image sur un registre (Docker Hub ou GitHub
  Container Registry) après un build réussi. Cherche « github actions build push
  docker image ». Attention : cela demande de configurer un **secret** (jamais
  de mot de passe en clair dans le YAML !).

## Questions

- Quel intérêt de construire l'image en CI plutôt que seulement sur ta machine ?
- Qu'est-ce qu'un **secret** dans GitHub Actions, et pourquoi ne pas mettre un
  mot de passe directement dans le fichier de workflow ?

## Indices

- L'étape `docker build` dans un workflow, ou l'action officielle
  `docker/build-push-action`.
