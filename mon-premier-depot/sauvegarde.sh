#!/bin/bash

# Vérifier qu'un dossier a été fourni
if [ -z "$1" ]; then
    echo "Erreur : veuillez indiquer le dossier à sauvegarder."
    exit 1
fi

DOSSIER="$1"

# Vérifier que le dossier existe
if [ ! -d "$DOSSIER" ]; then
    echo "Erreur : le dossier '$DOSSIER' n'existe pas."
    exit 1
fi

# Créer le dossier de sauvegardes
mkdir -p sauvegardes

# Générer la date et l'heure
DATE=$(date +%Y-%m-%d_%Hh%M)

# Nom de l'archive
ARCHIVE="sauvegardes/sauvegarde-$DATE.tar.gz"

# Créer l'archive compressée
tar -czf "$ARCHIVE" "$DOSSIER"

# Vérifier si la sauvegarde a réussi
if [ $? -eq 0 ]; then
    echo "Sauvegarde réussie !"
    echo "Archive créée : $ARCHIVE"
else
    echo "Erreur : la sauvegarde a échoué."
    exit 1
fi
