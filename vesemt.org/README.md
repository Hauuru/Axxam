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
│   ├── style.css                # Styles principaux (nav, hero, accueil, footer)
│   ├── article.css              # Styles des articles
│   └── dossiers.css             # Styles des dossiers métropolitains
├── images/                      # 57 images (JPEG, ≤ 800 px, q85)
├── articles/                    # 58 articles (dates : 01/03 → 04/08/2026)
├── tools/                       # Outils de conversion WordPress → statique
│   ├── build_registry.py        # inventaire des articles → registry.json
│   ├── backlog.py               # RSS → backlog.json (known / pending)
│   ├── convert.py               # ?p=ID → article HTML + images + slugmap.json
│   ├── wire.py                  # index, nav, prev/next, placeholders, sitemap
│   └── slugmap.json             # correspondance p:N → slug
├── documentation/
│   ├── PROPOSITION-METHODE.md   # proposition validée (structure + pipeline)
│   └── CONVERSION-METHODE.md    # playbook de conversion (à suivre pour chaque nouvel article)
├── index.html                   # Accueil : bandeau + liste de tous les articles
├── qui-sommes-nous.html         # Page "Qui sommes nous ?"
├── elections-municipales-2026.html  # Élections Municipales 2026
├── contacter-reseaux.html       # Contact et réseaux
├── politique-confidentialite.html  # Politique de confidentialité
├── sitemap.xml                  # Sitemap (63 URLs : 5 pages + 58 articles)
└── robots.txt
```

> Pages supprimées en août 2026 : catégories `dossiers-metropolitains.html`,
> `saint-pierre-des-corps.html`, `le-quotidien-le-vrai.html`,
> `vesemt-localement.html` et page auteur `author-le-plombier.html`
> (présentation simplifiée, sans catégories).

## 🌐 Déploiement

Le site est publié via GitHub Pages sur `https://axxam.net/vesemt.org/` (domaine custom axxam.net, dépôt `Hauuru/Axxam`).

## 📊 Statistiques

- **Total de fichiers HTML** : 63 (5 pages + 58 articles)
- **Total d'images** : 57 (toutes en JPEG, ≤ 800 px)
- **Total de fichiers CSS** : 3
- **Liens internes** : 0 cassé (vérifié) ; **placeholders** : 0 restant
- **Rendu** : 0 erreur JS, 0 image cassée, 0 overflow (desktop + mobile, Playwright)

## 🛠️ Maintenance (août 2026)

### Étape 5 (précédente)
- **Liens réparés** : article résiduel du clone WordPress reconstruit (header, CSS, catégorie, tags, image) ; les 5 archives `articles/archives/*` promues vers `articles/` avec chemins corrigés ; 0 fichier cassé (check automatique)
- **Fragments supprimés** : `template-article.html`, `new_posts_grid.html`, `page-2.html`, scripts obsolètes (`deploy.sh`, `add-footer-credits.sh`, `documentation/optimize-images.sh`)
- **Métadonnées unifiées** : tous les `og:*`/`twitter:*` pointent vers `https://axxam.net/vesemt.org/...` (231 références) ; seuls les liens `https://www.vesemt.org/?p=N` vers l'article WordPress d'origine sont conservés
- **Sitemap + robots** créés pour `https://axxam.net/vesemt.org/`
- **Images allégées** : 17 PNG convertis en JPEG (qualité 85), Gemini redimensionnée 1408×752 → 800×427 : 8,8 Mo → 3,5 Mo (−60 %)

### Étape 6 (simplification + conversion du backlog)
- **Présentation simplifiée** (décisions validées 04/08/2026) : accueil = bandeau conservé + liste de **tous** les articles (date, titre cliquable, résumé bref) ; navigation réduite à 5 liens (Accueil, Qui sommes-nous, Élections 2026, Contacter-réseaux, Politique de confidentialité) ; tags conservés non cliquables
- **Pages supprimées** : les 4 pages de catégories + la page auteur (plus de catégories sur le site)
- **38 articles WordPress convertis** (outils `tools/`) : 22 → 58 articles (01/03 → 04/08/2026) ; contenu nettoyé (tracking Facebook, embeds emoji, widgets, markdown `##`, placeholders `[[p:N]]` résolus)
- **Images converties** en JPEG ≤ 800 px (nommage `.jpg`), images orphelines supprimées
- **Corrections** : urls unicode (`×`), large URLs débordantes (`overflow-wrap`), images en débordement (`max-width: 100%`)
- **Méthode reproductible** : `documentation/CONVERSION-METHODE.md` — pipeline découverte RSS → conversion `?p=ID` → intégration `wire.py` → validation → publication (à suivre pour chaque nouvel article du WordPress)

## 📄 Licence

Basé sur le contenu original du site VESEMT. Respecter les droits d'auteur du contenu original.

## 👥 Auteurs

- **Contenu original** : VESEMT
- **Conversion HTML+CSS** : Assistant OpenClaw

## 📞 Contact

via la page [Contacter- réseaux](contacter-reseaux.html) ou **vesemt@gmail.com**
