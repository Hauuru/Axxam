#!/bin/bash

# Script de déploiement VESEMT Simple
# Ce script prépare le site pour le déploiement

echo "🚀 Déploiement VESEMT Simple"
echo "============================"

# Vérifier que nous sommes dans le bon dossier
if [ ! -f "index.html" ]; then
    echo "❌ Erreur : index.html non trouvé. Veuillez exécuter ce script depuis le dossier racine du projet."
    exit 1
fi

# Nettoyer les fichiers temporaires
echo "🧹 Nettoyage des fichiers temporaires..."
find . -name "*.tmp" -delete
find . -name "*.bak" -delete
find . -name "*~" -delete
find . -name ".DS_Store" -delete
find . -name "Thumbs.db" -delete

# Vérifier la structure
echo "📁 Vérification de la structure..."
if [ ! -d "vesemt-css" ]; then
    echo "❌ Erreur : dossier vesemt-css manquant"
    exit 1
fi

if [ ! -d "images" ]; then
    echo "❌ Erreur : dossier images manquant"
    exit 1
fi

if [ ! -d "articles" ]; then
    echo "❌ Erreur : dossier articles manquant"
    exit 1
fi

# Compter les fichiers
html_files=$(find . -name "*.html" | wc -l)
image_files=$(find images/ -type f | wc -l)
css_files=$(find vesemt-css/ -type f | wc -l)

echo "📊 Statistiques :"
echo "   - Fichiers HTML : $html_files"
echo "   - Images : $image_files"
echo "   - Fichiers CSS : $css_files"

# Vérifier les liens brisés
echo "🔍 Vérification des liens..."
broken_links=0

for file in $(find . -name "*.html"); do
    # Extraire les liens du fichier
    links=$(grep -o 'href="[^"]*"' "$file" | sed 's/href="//;s/"//' | grep -v "^#" | grep -v "^http" | grep -v "^mailto")
    
    for link in $links; do
        # Vérifier si le fichier existe
        if [ ! -f "$link" ] && [ ! -f "articles/$(basename $link)" ] && [ ! -f "images/$(basename $link)" ] && [ ! -f "vesemt-css/$(basename $link)" ]; then
            echo "   ⚠️  Lien brisé dans $file : $link"
            broken_links=$((broken_links + 1))
        fi
    done
done

if [ $broken_links -eq 0 ]; then
    echo "   ✅ Aucun lien brisé détecté"
else
    echo "   ⚠️  $broken_links lien(s) brisé(s) détecté(s)"
fi

# Calculer la taille du projet
size=$(du -sh . | cut -f1)
echo "📦 Taille du projet : $size"

echo ""
echo "✅ Préparation terminée !"
echo ""
echo "🌐 Options de déploiement :"
echo "   1. GitHub Pages : https://pages.github.com/"
echo "   2. Netlify : https://www.netlify.com/"
echo "   3. Vercel : https://vercel.com/"
echo ""
echo "📝 Pour déployer sur GitHub Pages :"
echo "   git init"
echo "   git add ."
echo "   git commit -m 'Initial commit'"
echo "   git remote add origin https://github.com/votre-username/vesemt-simple.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
