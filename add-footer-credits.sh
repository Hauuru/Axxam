#!/bin/bash

# Script pour ajouter les crédits de création dans le footer de toutes les pages VESEMT

# Liste de tous les fichiers HTML
HTML_FILES=(
    "index.html"
    "page-2.html"
    "saint-pierre-des-corps.html"
    "template-article.html"
    "author-le-plombier.html"
    "politique-confidentialite.html"
    "le-quotidien-le-vrai.html"
    "elections-municipales-2026.html"
    "qui-sommes-nous.html"
    "vesemt-localement.html"
    "contacter-reseaux.html"
    "dossiers-metropolitains.html"
    "articles/communique-bravo-deux-cotes-intervalles.html"
    "articles/resultats-2026-1er-2nd-tour.html"
    "articles/municipales-2026-premier-tour-voter-blanc.html"
    "articles/municipales-alternance-sans-alternative.html"
    "articles/anatomie-rapport-force-autopsie-illusion.html"
    "articles/dynamique-metropolitaine.html"
    "articles/bilan-mandat-2020-2026.html"
    "articles/communique-clarification-positionnement-olivier-conte.html"
    "articles/association-sportive-aubriere.html"
    "articles/communique-presse-fermetures-classes.html"
    "articles/rapport-vesemt-autopsie-vote-discipline-desordre.html"
    "articles/mise-au-point-cimetiere-interet-metropolitain.html"
)

# Répertoire de base
BASE_DIR="/home/hauuru/.openclaw/workspace/projects/active/vesemt-simple/vesemt.org"

# Texte à ajouter après le copyright
CREDITS_LINE='            <p class="footer-credits">🌱 Créé avec passion par Le Plombier, Marco, Calcifere et Hauuru</p>'

# Compteur de fichiers modifiés
MODIFIED_COUNT=0

# Pour chaque fichier HTML
for file in "${HTML_FILES[@]}"; do
    FILE_PATH="$BASE_DIR/$file"

    # Vérifier si le fichier existe
    if [ -f "$FILE_PATH" ]; then
        # Vérifier si le footer-credits existe déjà
        if ! grep -q "footer-credits" "$FILE_PATH"; then
            # Ajouter la ligne après le copyright
            sed -i '/<p>&copy; 2026 VESEMT - Tous droits réservés<\/p>/a\            '"$CREDITS_LINE" "$FILE_PATH"
            echo "✅ Modifié: $file"
            ((MODIFIED_COUNT++))
        else
            echo "⏭️  Déjà modifié: $file"
        fi
    else
        echo "❌ Fichier non trouvé: $file"
    fi
done

echo ""
echo "🎉 Modification terminée !"
echo "📊 Fichiers modifiés: $MODIFIED_COUNT / ${#HTML_FILES[@]}"
