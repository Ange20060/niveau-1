# Bonus (facultatif)

Si tu as fini les 5 exercices et que tu te sens à l'aise, voici deux pistes
pour aller plus loin. Tu travailles à partir de ton projet de l'exercice 5.

## Bonus 1 — Attendre que la base soit vraiment prête

Tu as peut-être remarqué que `depends_on` garantit que la base **démarre**
avant l'API, mais pas qu'elle soit **prête à accepter des connexions**. Selon
les machines, l'API peut planter au premier lancement parce que Postgres
n'a pas fini de s'initialiser.

- Ajoute un **healthcheck** sur le service `db` (cherche `pg_isready`).
- Modifie le `depends_on` de l'API pour qu'il attende la condition
  « base en bonne santé » et plus seulement « base démarrée ».
- Teste : `docker compose up` doit marcher du premier coup, sans erreur de
  connexion au démarrage.

## Bonus 2 — Réduire la taille de l'image

- Regarde la taille actuelle de ton image API avec `docker images`.
- Essaie de la réduire : pars d'une image de base plus légère (variante
  `slim`), et renseigne-toi sur le **build multi-étapes** (multi-stage build).
- Compare la taille avant / après et note-la dans `NOTES.md`.

## À noter dans NOTES.md

- Quelle est la différence entre « le conteneur est démarré » et « le service
  est prêt » ?
- Combien d'octets as-tu gagné sur l'image, et comment ?
