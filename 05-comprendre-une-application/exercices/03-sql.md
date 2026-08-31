# Exercice 3 — Premières requêtes SQL

Objectif : écrire des requêtes SQL de base. Tu peux t'entraîner sur un
tutoriel SQL interactif en ligne, ou avec la base PostgreSQL que tu
manipuleras en partie 06.

## À faire

Imagine une table `etudiants` avec les colonnes : `id`, `nom`, `ville`, `age`.

1. Écris la requête qui **crée** cette table.
2. Écris les requêtes qui **insèrent** trois étudiants.
3. Récupère **tous** les étudiants.
4. Récupère uniquement les étudiants de la ville de « Lyon ».
5. Récupère les étudiants de plus de 20 ans, triés par âge.
6. Change la ville d'un étudiant précis.
7. Supprime un étudiant par son `id`.

## Questions

- À quoi sert la **clé primaire** (`id`) ?
- Quelle est la différence entre `WHERE` et `ORDER BY` ?
- Quelle est la différence entre `UPDATE` et `INSERT` ?

## Indices

- `CREATE TABLE`, `INSERT INTO ... VALUES`, `SELECT ... FROM ... WHERE`,
  `ORDER BY`, `UPDATE ... SET ... WHERE`, `DELETE FROM ... WHERE`.
- **Attention :** un `UPDATE` ou `DELETE` sans `WHERE` touche TOUTE la table.
