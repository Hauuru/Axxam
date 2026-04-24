#!/bin/bash

# Script d'optimisation des images pour VESEMT.org
# Ce script convertit les images PNG en JPEG et les compresse

set -e

# Configuration
UPLOADS_DIR="vesemt.org/wp-content/uploads/2026/03"
QUALITY_JPEG=85
QUALITY_PNG=75
MAX_WIDTH=1600

# Couleurs pour la sortie
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "=========================================="
echo "  Script d'optimisation des images"
echo "  VESEMT.org"
echo "=========================================="
echo ""

# Vérifier si ImageMagick est installé
if ! command -v convert &> /dev/null; then
    echo -e "${RED}Erreur: ImageMagick n'est pas installé.${NC}"
    echo "Pour installer ImageMagick :"
    echo "  Ubuntu/Debian: sudo apt-get install imagemagick"
    echo "  macOS: brew install imagemagick"
    exit 1
fi

# Vérifier si jpegoptim est installé
if ! command -v jpegoptim &> /dev/null; then
    echo -e "${YELLOW}Attention: jpegoptim n'est pas installé.${NC}"
    echo "Pour installer jpegoptim :"
    echo "  Ubuntu/Debian: sudo apt-get install jpegoptim"
    echo "  macOS: brew install jpegoptim"
    echo ""
    echo "Le script continuera sans jpegoptim (compression moins optimale)."
    echo ""
fi

# Vérifier si optipng est installé
if ! command -v optipng &> /dev/null; then
    echo -e "${YELLOW}Attention: optipng n'est pas installé.${NC}"
    echo "Pour installer optipng :"
    echo "  Ubuntu/Debian: sudo apt-get install optipng"
    echo "  macOS: brew install optipng"
    echo ""
    echo "Le script continuera sans optipng (compression moins optimale)."
    echo ""
fi

# Créer un répertoire de sauvegarde
BACKUP_DIR="backup_images_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

echo -e "${GREEN}Répertoire de sauvegarde : $BACKUP_DIR${NC}"
echo ""

# Compter les images
TOTAL_IMAGES=$(find "$UPLOADS_DIR" -type f \( -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" \) | wc -l)
echo "Nombre total d'images à traiter : $TOTAL_IMAGES"
echo ""

# Demander confirmation
read -p "Voulez-vous continuer ? (o/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Oo]$ ]]; then
    echo "Annulation."
    exit 0
fi

echo ""
echo "=========================================="
echo "  Début de l'optimisation"
echo "=========================================="
echo ""

# Compteurs
CONVERTED=0
COMPRESSED=0
SKIPPED=0
TOTAL_SAVED=0

# Traiter les images PNG
echo -e "${YELLOW}Traitement des images PNG...${NC}"
for img in $(find "$UPLOADS_DIR" -type f -name "*.png"); do
    filename=$(basename "$img")
    dirname=$(dirname "$img")

    # Ignorer les images de petite taille (thumbnails, icônes)
    width=$(identify -format "%w" "$img" 2>/dev/null || echo "0")
    if [ "$width" -lt 300 ]; then
        echo -e "  ${YELLOW}Ignoré (petite taille)${NC}: $filename"
        ((SKIPPED++))
        continue
    fi

    # Sauvegarder l'original
    cp "$img" "$BACKUP_DIR/"

    # Convertir en JPEG
    jpeg_file="${img%.png}.jpg"
    if [ ! -f "$jpeg_file" ]; then
        convert "$img" -quality $QUALITY_JPEG -resize "${MAX_WIDTH}x>" "$jpeg_file"

        # Supprimer l'original si la conversion a réussi
        if [ -f "$jpeg_file" ]; then
            original_size=$(stat -f%z "$img" 2>/dev/null || stat -c%s "$img")
            new_size=$(stat -f%z "$jpeg_file" 2>/dev/null || stat -c%s "$jpeg_file")
            saved=$((original_size - new_size))

            if [ $saved -gt 0 ]; then
                rm "$img"
                echo -e "  ${GREEN}Converti${NC}: $filename ($((original_size / 1024)) Ko → $((new_size / 1024)) Ko, -$((saved / 1024)) Ko)"
                ((CONVERTED++))
                ((TOTAL_SAVED += saved))
            else
                rm "$jpeg_file"
                echo -e "  ${YELLOW}Ignoré (pas de gain)${NC}: $filename"
                ((SKIPPED++))
            fi
        fi
    fi
done

echo ""

# Compresser les images JPEG
echo -e "${YELLOW}Compression des images JPEG...${NC}"
if command -v jpegoptim &> /dev/null; then
    for img in $(find "$UPLOADS_DIR" -type f \( -name "*.jpg" -o -name "*.jpeg" \)); do
        filename=$(basename "$img")

        # Sauvegarder l'original
        cp "$img" "$BACKUP_DIR/"

        # Compresser
        original_size=$(stat -f%z "$img" 2>/dev/null || stat -c%s "$img")
        jpegoptim --max=$QUALITY_JPEG --strip-all "$img" > /dev/null 2>&1
        new_size=$(stat -f%z "$img" 2>/dev/null || stat -c%s "$img")
        saved=$((original_size - new_size))

        if [ $saved -gt 0 ]; then
            echo -e "  ${GREEN}Compressé${NC}: $filename ($((original_size / 1024)) Ko → $((new_size / 1024)) Ko, -$((saved / 1024)) Ko)"
            ((COMPRESSED++))
            ((TOTAL_SAVED += saved))
        else
            echo -e "  ${YELLOW}Ignoré (déjà optimisé)${NC}: $filename"
            ((SKIPPED++))
        fi
    done
else
    echo -e "  ${YELLOW}jpegoptim non disponible, compression ignorée${NC}"
fi

echo ""

# Compresser les images PNG restantes
echo -e "${YELLOW}Compression des images PNG restantes...${NC}"
if command -v optipng &> /dev/null; then
    for img in $(find "$UPLOADS_DIR" -type f -name "*.png"); do
        filename=$(basename "$img")

        # Sauvegarder l'original
        cp "$img" "$BACKUP_DIR/"

        # Compresser
        original_size=$(stat -f%z "$img" 2>/dev/null || stat -c%s "$img")
        optipng -o2 -quiet "$img" > /dev/null 2>&1
        new_size=$(stat -f%z "$img" 2>/dev/null || stat -c%s "$img")
        saved=$((original_size - new_size))

        if [ $saved -gt 0 ]; then
            echo -e "  ${GREEN}Compressé${NC}: $filename ($((original_size / 1024)) Ko → $((new_size / 1024)) Ko, -$((saved / 1024)) Ko)"
            ((COMPRESSED++))
            ((TOTAL_SAVED += saved))
        else
            echo -e "  ${YELLOW}Ignoré (déjà optimisé)${NC}: $filename"
            ((SKIPPED++))
        fi
    done
else
    echo -e "  ${YELLOW}optipng non disponible, compression ignorée${NC}"
fi

echo ""
echo "=========================================="
echo "  Résumé de l'optimisation"
echo "=========================================="
echo ""
echo -e "Images converties (PNG → JPEG) : ${GREEN}$CONVERTED${NC}"
echo -e "Images compressées : ${GREEN}$COMPRESSED${NC}"
echo -e "Images ignorées : ${YELLOW}$SKIPPED${NC}"
echo -e "Espace total économisé : ${GREEN}$((TOTAL_SAVED / 1024 / 1024)) Mo${NC}"
echo ""
echo -e "Sauvegardes stockées dans : ${GREEN}$BACKUP_DIR${NC}"
echo ""

# Calculer la nouvelle taille totale
NEW_TOTAL=$(du -sh "$UPLOADS_DIR" | cut -f1)
echo "Nouvelle taille du répertoire uploads : $NEW_TOTAL"
echo ""

echo "Pour annuler les modifications et restaurer les originaux :"
echo "  cp -r $BACKUP_DIR/* $UPLOADS_DIR/"
echo ""
