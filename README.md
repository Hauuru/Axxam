# VESEMT - Site HTML Simple

## 📝 Description

Version HTML+CSS simple du site VESEMT (VIVRE (SURTOUT) ENSEMBLE ET (SI POSSIBLE) SOLIDAIRES EN MÉTROPOLE TOURANGELLE).

Ce site a été créé à partir du site original WordPress pour offrir une structure simple, facile à modifier et fidèle au contenu original.

## 🚀 Installation

### Prérequis
- Aucun prérequis particulier
- Navigateur web moderne

### Utilisation locale

#### Méthode 1 : Ouvrir directement
```bash
# Ouvrir le fichier index.html dans votre navigateur
file:///chemin/vers/vesemt-simple/index.html
```

#### Méthode 2 : Serveur local
```bash
# Avec Python 3
python3 -m http.server 8000

# Puis ouvrir : http://localhost:8000
```

#### Méthode 3 : Avec Node.js
```bash
# Installer http-server
npm install -g http-server

# Lancer le serveur
http-server -p 8000

# Puis ouvrir : http://localhost:8000
```

## 📁 Structure du projet

```
vesemt-simple/
├── vesemt-css/
│   └── style.css              # Feuille de style principale
├── images/                    # 20 images du site
│   ├── 1er-tour-Definitif-200x300.png
│   ├── 1er-tour-Definitif-5-800x445.png
│   ├── Bandeau-2-800x445.jpg
│   ├── Comparatif-ok.png
│   ├── Decoupage-electoral.jpg
│   ├── Gemini_Generated_Image_izuzpaizuzpaizuz.png
│   ├── Illustration-800x445.png
│   ├── Illustration.png
│   ├── Ilustration-300x200.png
│   ├── Ilustration-800x445.png
│   ├── Ilustration.png
│   ├── Imaege-Municipales-800x445.jpg
│   ├── Image-800x445.jpg
│   ├── Image.jpg
│   ├── Les-electeurs-fuient-les-promesses-politiques-800x445.png
│   ├── Les-electeurs-fuient-les-promesses-politiques.png
│   ├── Logo.jpg
│   ├── New-bandeau-SITE.jpg
│   ├── Nouvelle-image.png
│   ├── Resultats-premier-tours-2026-municpales-1.jpg
│   └── Resultats-premier-tours-2026-municpales.jpg
├── articles/                  # 11 articles
│   ├── anatomie-rapport-force-autopsie-illusion.html
│   ├── bilan-mandat-2020-2026.html
│   ├── communique-bravo-deux-cotes-intervalles.html
│   ├── communique-clarification-positionnement-olivier-conte.html
│   ├── communique-presse-fermetures-classes.html
│   ├── mise-au-point-cimetiere-interet-metropolitain.html
│   ├── municipales-2026-premier-tour-voter-blanc.html
│   ├── municipales-alternance-sans-alternative.html
│   ├── rapport-vesemt-autopsie-vote-discipline-desordre.html
│   └── resultats-2026-1er-2nd-tour.html
├── author-le-plombier.html     # Page de l'auteur
├── contacter-reseaux.html       # Page de contact
├── elections-municipales-2026.html  # Page élections
├── index.html                  # Page d'accueil
├── le-quotidien-le-vrai.html  # Catégorie
├── page-2.html                 # Page de pagination
├── politique-confidentialite.html  # Politique de confidentialité
├── qui-sommes-nous.html        # Page "Qui sommes nous ?"
├── saint-pierre-des-corps.html  # Catégorie
├── vesemt-localement.html      # Page VESEMT localement
├── README.md                   # Ce fichier
├── RAPPORT_ANALYSE.md          # Rapport d'analyse détaillé
└── .gitignore                  # Fichiers ignorés par Git
```

## 📄 Pages principales

### 1. **index.html** - Page d'accueil
- Présentation des 10 derniers articles
- Navigation vers toutes les sections du site

### 2. **qui-sommes-nous.html** - Qui sommes nous ?
- Présentation de VESEMT
- Mission et valeurs

### 3. **elections-municipales-2026.html** - Elections Municipales 2026
- Informations sur les élections municipales
- Résultats et analyses

### 4. **contacter-reseaux.html** - Contacter- réseaux
- Coordonnées de contact
- Réseaux sociaux

### 5. **politique-confidentialite.html** - Politique de confidentialité
- Politique de protection des données
- Conditions d'utilisation

### 6. **vesemt-localement.html** - VESEMT LOCALEMENT
- Activités locales
- Initiatives de proximité

## 📝 Articles

Le site contient 11 articles sur les thèmes suivants :

1. **Rapport VESEMT : Autopsie d'un vote discipliné dans le désordre**
   - Analyse des résultats électoraux

2. **Communiqué : Demande de clarification du positionnement politique d'Olivier Conte**
   - Positionnement sur l'union des droites

3. **COMMUNIQUÉ DE PRESSE – VESEMT Fermetures de classes**
   - Contenu sur les fermetures de classes

4. **BILAN DE MANDAT 2020-2026**
   - Bilan détaillé de Fatiha Kendri et Nabil Benzaït

5. **Communiqué de VESEMT : BRAVO DES DEUX CÔTÉS… ET DES INTERVALLES**
   - Analyse du vote

6. **Résultats 2026 (1er et 2nd Tour)**
   - Images des résultats

7. **Mise au point sur le Cimetière d'intérêt métropolitain**
   - Synthèse administrative

8. **Anatomie d'un rapport de force… et autopsie d'une illusion**
   - Analyse du premier tour

9. **Municipales 2026 : Premier tour : voter blanc**
   - Appel au vote blanc

10. **Municipales : l'alternance sans l'alternative**
    - Comparatif des programmes

## 🎨 Personnalisation

### Modifier le CSS
Le fichier `vesemt-css/style.css` contient tous les styles du site. Vous pouvez modifier :
- Les couleurs
- Les polices
- La mise en page
- Les effets visuels

### Modifier le contenu
Chaque fichier HTML peut être modifié directement avec un éditeur de texte :
- `index.html` pour la page d'accueil
- `articles/*.html` pour les articles
- Les autres fichiers HTML pour les pages principales

### Ajouter des images
Placez vos nouvelles images dans le dossier `images/` et mettez à jour les liens dans les fichiers HTML.

## 🌐 Déploiement

### GitHub Pages
```bash
# Initialiser le dépôt Git
git init
git add .
git commit -m "Initial commit"

# Créer un dépôt sur GitHub et pousser
git remote add origin https://github.com/votre-username/vesemt-simple.git
git branch -M main
git push -u origin main
```

### Netlify
1. Connectez-vous à [Netlify](https://www.netlify.com/)
2. Glissez-déposez le dossier `vesemt-simple`
3. Votre site sera en ligne en quelques secondes

### Vercel
```bash
# Installer Vercel CLI
npm install -g vercel

# Déployer
vercel
```

## 📱 Responsive Design

Le site est entièrement responsive et s'adapte à :
- 📱 Mobiles (320px+)
- 📱 Tablettes (768px+)
- 💻 Ordinateurs (1024px+)
- 🖥️ Écrans larges (1440px+)

## 🔧 Technologies utilisées

- **HTML5** : Structure sémantique
- **CSS3** : Mise en page et styles
- **Responsive Design** : Adaptation mobile
- **Aucun framework** : Code pur et simple

## 📊 Statistiques

- **Total de fichiers HTML** : 20
- **Total d'images** : 20
- **Total de fichiers CSS** : 1
- **Lignes de code** : ~15,000
- **Taille du projet** : 8 Mo

## 🤝 Contribution

Pour contribuer à ce projet :
1. Fork le projet
2. Créez une branche (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Pushez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📄 Licence

Ce projet est basé sur le contenu original du site VESEMT. Veuillez respecter les droits d'auteur du contenu original.

## 👥 Auteurs

- **Contenu original** : VESEMT
- **Conversion HTML+CSS** : Assistant OpenClaw

## 📞 Contact

Pour toute question ou suggestion, veuillez contacter l'équipe VESEMT via la page [Contacter- réseaux](contacter-reseaux.html).

---

**Date de création** : 1er avril 2026
**Version** : 1.1.0
**Statut** : ✅ Complet et fonctionnel

## 📋 Corrections effectuées (1er avril 2026)

### ✅ Corrections visuelles majeures

1. **Bandeau d'accueil (Hero Banner)**
   - Ajout du hero banner sur toutes les pages (20 fichiers HTML)
   - Image `New-bandeau-SITE.jpg` (177KB) téléchargée depuis le site original
   - Correction visuelle majeure - le site a maintenant son identité visuelle

2. **Image manquante dans "Qui sommes nous ?"**
   - Téléchargement de l'image `Gemini_Generated_Image_izuzpaizuzpaizuz.png` (2.8MB)
   - Restauration complète du contenu visuel de la page

### 📖 Documentation

- Création du rapport d'analyse détaillé (`RAPPORT_ANALYSE.md`)
- Propositions d'amélioration pour la maintenabilité (humain + IA)
- Plan d'action recommandé pour les évolutions futures

Pour plus de détails, consultez le [RAPPORT_ANALYSE.md](RAPPORT_ANALYSE.md).
