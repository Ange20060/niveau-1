# Exercice 3 — Provoquer et résoudre un conflit

Objectif : ne plus paniquer devant un conflit de fusion. C'est normal et ça se
résout calmement.

## À faire

1. Sur `main`, dans ton `README.md`, repère une ligne précise (par ex. la
   première).
2. Crée une branche `version-a`, modifie cette ligne d'une certaine façon, et
   commit.
3. Reviens sur `main`, modifie **la même ligne** différemment, et commit.
4. Essaie de fusionner `version-a` dans `main`. Git va refuser : c'est un
   **conflit**.
5. Ouvre le fichier : observe les marqueurs `<<<<<<<`, `=======`, `>>>>>>>`.
   Choisis la version finale, supprime les marqueurs, puis termine la fusion.

## Questions

- Pourquoi Git ne peut-il pas décider tout seul quelle version garder ?
- Que représentent les trois marqueurs de conflit ?
- Quelles étapes fais-tu après avoir résolu le conflit dans le fichier ?

## Indices

- Après avoir édité le fichier, il faut `git add` le fichier résolu puis
  terminer avec un `git commit`.
