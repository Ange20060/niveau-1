#!/bin/bash

compteur=0

for f in *; do
    if [ -f "$f" ]; then
        extension="${f##*.}"

        mkdir -p "$extension"
        mv "$f" "$extension/"

        echo "$f → $extension/"
        compteur=$((compteur + 1))
    fi
done

echo "Nombre de fichiers rangés : $compteur"
