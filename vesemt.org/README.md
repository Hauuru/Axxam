# VESEMT - Site HTML statique

## 📝 Description

Version HTML+CSS statique du site VESEMT (VIVRE (SURTOUT) ENSEMBLE ET (SI POSSIBLE) SOLIDAIRES EN MÉTROPOLE TOURANGELLE), convertie depuis le site WordPress original.

**Site en ligne :** https://axxam.net/vesemt.org/

## 🚀 Utilisation locale

```bash
# Depuis le dossier du site
python3 -m http.server 8000
# Puis ouvrir : http://localhost:8000
```

## 📁 Structure du projet

```
vesemt.org/
├── vesemt-css/                  # 3 feuilles de style
│   ├── style.css                # Styles principaux (nav, hero, grille, footer)
│   ├── article.css              # Styles des articles
│   └── dossiers.css             # Styles des dossiers métropolitains
├── images/                      # 28 images (JPEG, compressées ~3,5 Mo)
├── articles/                    # 20 articles
├── index.html                   # Accueil (15 cartes d'articles)
├── qui-sommes-nous.html         # Page "Qui sommes nous ?"
├── elections-municipales-2026.html  # Élections Municipales 2026
├── dossiers-metropolitains.html # Dossiers métropolitains
├── contacter-reseaux.html       # Contact et réseaux
├── politique-confidentialite.html  # Politique de confidentialité
├── vesemt-localement.html       # Page VESEMT LOCALEMENT
├── saint-pierre-des-corps.html  # Catégorie
├── le-quotidien-le-vrai.html    # Catégorie
├── author-le-plombier.html      # Page auteur
├── sitemap.xml                  # Sitemap (30 URLs)
└── robots.txt
```

## 🌐 Déploiement

Le site est publié via GitHub Pages sur `https://axxam.net/vesemt.org/` (domaine custom axxam.net, dépôt `Hauuru/Axxam`).

## 📊 Statistiques

- **Total de fichiers HTML** : 30 (10 pages + 20 articles)
- **Total d'images** : 28 (3,5 Mo, toutes en JPEG)
- **Total de fichiers CSS** : 3
- **Taille du projet** : ~4 Mo
- **Liens internes** : 0 cassé (vérifié)

## 🛠️ Maintenance (août 2026)

- **Liens réparés** : article résiduel du clone WordPress reconstruit (header, CSS, catégorie, tags, image) ; les 5 archives `articles/archives/*` promues vers `articles/` avec chemins corrigés ; 0 fichier cassé (check automatique)
- **Fragments supprimés** : `template-article.html`, `new_posts_grid.html`, `page-2.html`, scripts obsolètes (`deploy.sh`, `add-footer-credits.sh`, `documentation/optimize-images.sh`)
- **Métadonnées unifiées** : tous les `og:*`/`twitter:*` pointent vers `https://axxam.net/vesemt.org/...` (231 références) ; seuls les liens `https://www.vesemt.org/?p=N` vers l'article WordPress d'origine sont conservés
- **Sitemap + robots** créés pour `https://axxam.net/vesemt.org/`
- **Images allégées** : 17 PNG convertis en JPEG (qualité 85), Gemini redimensionnée 1408×752 → 800×427 : 8,8 Mo → 3,5 Mo (−60 %)

## 📄 Licence

Basé sur le contenu original du site VESEMT. Respecter les droits d'auteur du contenu original.

## 👥 Auteurs

- **Contenu original** : VESEMT
- **Conversion HTML+CSS** : Assistant OpenClaw

## 📞 Contact

via la page [Contacter- réseaux](contacter-reseaux.html) ou **vesemt@gmail.com**
