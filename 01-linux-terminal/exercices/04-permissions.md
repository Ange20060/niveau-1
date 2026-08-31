# Exercice 4 — Le gardien (permissions)

Objectif : comprendre et modifier les droits d'accès aux fichiers.

## À faire

1. Crée un fichier `secret.txt` et regarde ses permissions avec `ls -l`.
2. Retire à tout le monde le droit de lecture, puis essaie de l'afficher avec
   `cat`. Que se passe-t-il ?
3. Redonne-toi le droit de lecture.
4. Crée un script `bonjour.sh` qui contient `echo "Bonjour"`. Essaie de
   l'exécuter avec `./bonjour.sh`. Ça ne marche pas : pourquoi ?
5. Rends-le exécutable, puis relance-le.

## Questions

- Décompose la chaîne `-rwxr-xr--` : qui a le droit de quoi ?
- Quelle est la différence entre les droits du **propriétaire**, du **groupe**
  et des **autres** ?
- À quoi sert `sudo` et pourquoi ne faut-il pas l'utiliser tout le temps ?

## Indices

- `ls -l`, `chmod` (essaie les deux notations : `chmod +x` et `chmod 755`),
  `chown`.
- Pour comprendre les chiffres (755, 644...), cherche « chmod notation
  octale ».
