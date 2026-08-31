# Exercice 2 — Tester automatiquement

Objectif : faire vérifier ton code automatiquement à chaque push.

## À faire

1. Reprends un de tes scripts Python (ex. la calculatrice de la partie 04) et
   place-le dans un dépôt GitHub.
2. Écris un petit test simple (cherche « pytest exemple basique ») qui vérifie
   qu'une fonction renvoie le bon résultat.
3. Crée un workflow qui, à chaque push :
   - installe Python ;
   - installe les dépendances de test ;
   - lance les tests.
4. Pousse et vérifie dans l'onglet Actions que les tests passent (coche verte).
5. Casse volontairement ta fonction, pousse, et observe l'échec (croix rouge).
   Puis corrige.

## Questions

- Pourquoi est-ce utile que les tests tournent automatiquement plutôt que « à
  la main quand j'y pense » ?
- Que se passe-t-il, dans une équipe, si quelqu'un pousse du code qui casse les
  tests ?

## Indices

- Étape utile toute prête : `actions/checkout` (pour récupérer ton code),
  `actions/setup-python`.
- Framework de test le plus simple pour débuter : `pytest`.
