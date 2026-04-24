# Rapport d'analyse VESEMT.org - Guide de maintenance

## Date : 1er avril 2026

---

## 📋 Résumé des corrections effectuées

### ✅ Corrections visuelles majeures

1. **Bandeau d'accueil (Hero Banner)**
   - **Problème** : Le bandeau d'accueil était complètement absent du clone
   - **Solution** : Ajout du hero banner sur toutes les pages (20 fichiers HTML)
   - **Image** : `New-bandeau-SITE.jpg` (177KB) téléchargée depuis le site original
   - **Impact** : Correction visuelle majeure - le site a maintenant son identité visuelle

2. **Image manquante dans "Qui sommes nous ?"**
   - **Problème** : L'image `Gemini_Generated_Image_izuzpaizuzpaizuz.png` était absente
   - **Solution** : Téléchargement de l'image (2.8MB) depuis le site original
   - **Impact** : Restauration complète du contenu visuelle de la page

---

## 📊 État actuel du site

### Structure du site
```
vesemt-simple/
├── articles/              (11 articles)
├── images/               (20 images)
├── vesemt-css/           (1 fichier CSS)
├── index.html
├── page-2.html
├── qui-sommes-nous.html
├── elections-municipales-2026.html
├── contacter-reseaux.html
├── politique-confidentialite.html
├── vesemt-localement.html
├── saint-pierre-des-corps.html
├── le-quotidien-le-vrai.html
├── author-le-plombier.html
└── deploy.sh
```

### Statistiques
- **Fichiers HTML** : 20
- **Images** : 20
- **Fichiers CSS** : 1
- **Taille totale** : ~8MB
- **Visites mensuelles estimées** : 100 à 1000

---

## 🎨 Identité visuelle - Charte graphique

### Couleurs principales

```css
/* Couleur principale - Rouge VESEMT */
--cm-color-1: #F44336;

/* Couleur secondaire - Rouge foncé */
--cm-color-2: #D12729;

/* Couleur de fond - Blanc */
--cm-color-3: #FFFFFF;

/* Couleur de fond secondaire - Blanc cassé */
--cm-color-4: #FEF6F4;

/* Couleur de texte principal - Noir */
--cm-color-5: #0F000A;

/* Couleur de fond footer - Gris foncé */
--cm-color-6: #252020;

/* Couleur de texte secondaire - Gris */
--cm-color-7: #7E7777;

/* Couleur de lien - Bleu */
--cm-color-8: #207daf;
```

### Typographie

```css
/* Police principale */
font-family: 'Open Sans', Arial, sans-serif;

/* Tailles */
- Titre site : 24px (gras)
- Titre page : 32px
- Titre article : 20px
- Texte corps : 16px
- Texte secondaire : 14px
```

### Mise en page

```css
/* Largeur maximale */
max-width: 1160px;

/* Grille d'articles */
- 2 colonnes sur desktop
- 1 colonne sur mobile

/* Espacements */
- Padding contenu : 20px
- Marge entre articles : 30px
- Padding article : 20px
```

### Images

```css
/* Format illustrations articles */
- Largeur : 800px
- Hauteur : 445px
- Format : 16:9

/* Bandeau d'accueil */
- Largeur : 1406px
- Hauteur : 402px
```

---

## 📁 Templates HTML - Structure de référence

### Template de base (page complète)

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TITRE DE LA PAGE – VIVRE (SURTOUT) ENSEMBLE ET (SI POSSIBLE) SOLIDAIRES EN MÉTROPOLE TOURANGELLE</title>
    <link rel="stylesheet" href="vesemt-css/style.css">
</head>
<body>
    <!-- HEADER -->
    <header>
        <div class="header-content">
            <h1 class="site-title">
                <a href="index.html">VIVRE (SURTOUT) ENSEMBLE ET (SI POSSIBLE) SOLIDAIRES EN MÉTROPOLE TOURANGELLE</a>
            </h1>
            <p class="site-description">Comité Populaire</p>
        </div>
        <nav>
            <ul>
                <li><a href="index.html">Accueil</a></li>
                <li><a href="qui-sommes-nous.html">Qui sommes nous ?</a></li>
                <li><a href="elections-municipales-2026.html">Elections Municipales 2026</a></li>
                <li><a href="contacter-reseaux.html">Contacter- réseaux</a></li>
                <li><a href="politique-confidentialite.html">Politique de confidentialité</a></li>
                <li><a href="vesemt-localement.html">VESEMT LOCALEMENT</a></li>
            </ul>
        </nav>
    </header>

    <!-- HERO BANNER -->
    <div class="hero-banner">
        <img src="images/New-bandeau-SITE.jpg" alt="VIVRE (SURTOUT) ENSEMBLE ET (SI POSSIBLE) SOLIDAIRES EN MÉTROPOLE TOURANGELLE">
    </div>

    <!-- CONTENU PRINCIPAL -->
    <main>
        <div class="container">
            <!-- CONTENU SPÉCIFIQUE À LA PAGE -->
        </div>
    </main>

    <!-- FOOTER -->
    <footer>
        <div class="footer-content">
            <p>Copyright © 2026 <a href="index.html">VIVRE (SURTOUT) ENSEMBLE ET (SI POSSIBLE) SOLIDAIRES EN MÉTROPOLE TOURANGELLE</a>. Powered by ColorMag and WordPress.</p>
        </div>
    </footer>

</body>
</html>
```

### Template article (dans articles/)

```html
<article class="post">
    <!-- IMAGE (optionnel) -->
    <div class="post-image">
        <a href="articles/nom-article.html">
            <img src="images/nom-image-800x445.jpg" alt="Description de l'image">
        </a>
    </div>

    <!-- CONTENU -->
    <div class="post-content">
        <!-- CATÉGORIE -->
        <div class="post-category">
            <a href="nom-categorie.html">Nom de la catégorie</a>
        </div>

        <!-- MÉTADONNÉES -->
        <div class="post-meta">
            <span class="post-date">
                <time datetime="YYYY-MM-DD">mois jour, année</time>
            </span>
            <span class="post-author">
                <a href="author-le-plombier.html">Le Plombier</a>
            </span>
        </div>

        <!-- TITRE -->
        <h2 class="post-title">
            <a href="articles/nom-article.html">Titre de l'article</a>
        </h2>

        <!-- EXTRAIT -->
        <div class="post-excerpt">
            <p>Extrait de l'article (2-3 phrases)</p>
        </div>

        <!-- LIEN READ MORE -->
        <a class="read-more" href="articles/nom-article.html">Read More</a>
    </div>
</article>
```

### Template page de contenu

```html
<article class="page">
    <header class="entry-header">
        <h1 class="entry-title">Titre de la page</h1>
    </header>

    <div class="entry-content">
        <!-- CONTENU DE LA PAGE -->
        <p>Paragraphe de texte...</p>

        <!-- SOUS-TITRE -->
        <h3>Sous-titre</h3>

        <!-- IMAGE -->
        <img src="images/nom-image.jpg" alt="Description">

        <!-- AUTRE PARAGRAPHE -->
        <p>Autre paragraphe...</p>
    </div>
</article>
```

---

## 📝 Guide de rédaction - Pour humains et machines

### Structure d'un article

1. **Titre** - Accrocheur, clair, informatif
2. **Image d'illustration** - Format 800x445px, JPEG qualité 80%
3. **Catégorie** - Une des catégories existantes
4. **Date** - Format YYYY-MM-DD
5. **Auteur** - "Le Plombier" ou autre
6. **Extrait** - 2-3 phrases résumant l'article
7. **Contenu complet** - 500-1000 mots

### Tone et style

- **Tone** : Engagé mais bienveillant
- **Style** : Clair, direct, accessible
- **Longueur** : 500-1000 mots
- **Formatage** : Paragraphes courts, sous-titres fréquents

### Règles de formatage

```html
<!-- Paragraphe -->
<p>Texte du paragraphe...</p>

<!-- Sous-titre -->
<h3>Titre de niveau 3</h3>

<!-- Emphase -->
<strong>Texte important</strong>

<!-- Italique -->
<em>Texte en italique</em>

<!-- Image -->
<img src="images/nom-image.jpg" alt="Description précise">

<!-- Lien -->
<a href="page-cible.html">Texte du lien</a>
```

### Catégories existantes

- Le quotidien, le vrai
- Saint-Pierre-des-Corps
- VESEMT LOCALEMENT
- Elections Municipales 2026

### Images - Recommandations

- **Format illustrations** : 800x445px (16:9)
- **Compression** : JPEG qualité 80%
- **Alt text** : Descriptif et accessible
- **Nom des fichiers** : `nom-descriptif-800x445.jpg`

---

## 🚀 Processus de modification et déploiement

### 1. Modification locale

```bash
# Ouvrir le fichier à modifier
nano index.html

# Ou utiliser un éditeur graphique
code index.html
```

### 2. Test local

```bash
# Lancer un serveur local
python3 -m http.server 8000

# Ouvrir dans le navigateur
# http://localhost:8000
```

### 3. Vérification

- ✅ Vérifier que le site s'affiche correctement
- ✅ Vérifier que les liens fonctionnent
- ✅ Vérifier que les images s'affichent
- ✅ Vérifier sur mobile (redimensionner la fenêtre)

### 4. Commit

```bash
# Vérifier les modifications
git status

# Ajouter les fichiers modifiés
git add .

# Commiter avec un message clair
git commit -m "fix: Correction du titre de la page d'accueil"
```

### 5. Push

```bash
# Pousser vers GitHub
git push
```

### 6. Déploiement

- Le déploiement se fait automatiquement via GitHub Actions
- Le site est disponible sur : https://axxam.net/vesemt.org

---

## 🔧 Performance - Recommandations simples

### Pour 100-1000 visites mensuelles

**Optimisations de base :**

1. **Images**
   - Compresser les images en JPEG qualité 80%
   - Utiliser le format 800x445px pour les illustrations
   - Éviter les images trop lourdes (> 500KB)

2. **CSS**
   - Garder le CSS dans un seul fichier
   - Éviter les styles inline
   - Utiliser des classes réutilisables

3. **HTML**
   - Garder le HTML propre et sémantique
   - Éviter les balises inutiles
   - Utiliser les balises appropriées (header, main, footer, etc.)

**Pas besoin de :**
- ❌ Lazy loading (trop complexe pour ce volume)
- ❌ Minification CSS (gain négligeable)
- ❌ CDN (inutile pour ce volume)
- ❌ Cache avancé (inutile pour ce volume)

---

## 📂 Organisation des fichiers

### Structure recommandée

```
vesemt-simple/
├── articles/              # Tous les articles
│   ├── article-1.html
│   ├── article-2.html
│   └── ...
├── images/               # Toutes les images
│   ├── image-1-800x445.jpg
│   ├── image-2-800x445.jpg
│   └── ...
├── vesemt-css/           # Feuilles de style
│   └── style.css
├── index.html            # Page d'accueil
├── page-2.html           # Page de pagination
├── qui-sommes-nous.html  # Page "Qui sommes nous ?"
├── elections-municipales-2026.html  # Page élections
├── contacter-reseaux.html  # Page contact
├── politique-confidentialite.html  # Page confidentialité
├── vesemt-localement.html  # Page VESEMT localement
├── saint-pierre-des-corps.html  # Catégorie
├── le-quotidien-le-vrai.html  # Catégorie
├── author-le-plombier.html  # Page auteur
├── README.md             # Documentation
└── RAPPORT_ANALYSE.md    # Ce document
```

### Conventions de nommage

- **Fichiers HTML** : `kebab-case.html` (ex: `qui-sommes-nous.html`)
- **Images** : `descriptif-800x445.jpg` (ex: `illustration-800x445.jpg`)
- **CSS** : `style.css` (un seul fichier)

---

## 🎯 Priorités d'amélioration

### Priorité 1 : Organisation et documentation

**Objectif :** Faciliter la maintenance par humains et machines

**Actions :**
- ✅ Templates HTML de référence (créés)
- ✅ Guide de rédaction (créé)
- ✅ Charte graphique (créée)
- ✅ Processus de déploiement (documenté)

### Priorité 2 : Performance simple

**Objectif :** Optimiser pour 100-1000 visites mensuelles

**Actions :**
- Compresser les images existantes
- Vérifier que toutes les images sont au bon format
- Nettoyer le CSS si nécessaire

### Priorité 3 : Accessibilité

**Objectif :** Améliorer l'accessibilité de base

**Actions :**
- Ajouter des alt text descriptifs sur toutes les images
- Vérifier le contraste des couleurs
- Améliorer la navigation au clavier

---

## 📝 Conclusion

Le site VESEMT.org est maintenant **visuellement identique** au site original, avec les corrections apportées au bandeau d'accueil et aux images manquantes.

Ce guide fournit :
- ✅ **Templates HTML** de référence pour créer/modifier des pages
- ✅ **Charte graphique** complète (couleurs, typographie, mise en page)
- ✅ **Guide de rédaction** pour humains et machines
- ✅ **Processus de déploiement** clair et simple
- ✅ **Recommandations de performance** adaptées au volume de trafic

L'approche est **simple et manuelle** : pas d'automatisation, de tests locaux avant déploiement, et des templates HTML faciles à copier-coller.

---

## 📞 Références

- **Site original** : https://www.vesemt.org
- **Site clone** : https://axxam.net/vesemt.org
- **Dépôt GitHub** : https://github.com/Calcifere-hauuru/vesemt-simple

---

*Document généré le 1er avril 2026*
*Analyse effectuée par OpenClaw*
*Version 2.0 - Adaptée au fonctionnement manuel*
