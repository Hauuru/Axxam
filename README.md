# Axxam – Dépôt Multi-Sites

Bienvenue dans le dépôt **Axxam**, qui regroupe plusieurs projets web distincts : sites vitrines, applications interactives et documentation technique. Tous les sites sont déployés via GitHub Pages et accessibles sur le domaine principal `axxam.net`.

---

## 🎯 Architecture du dépôt

Le dépôt est organisé autour d'un **portail central** (à la racine) et de **5 sous-dossiers**, chacun contenant un site complet :

| Sous-dossier | Site | Déployé sur |
|-------------|------|-------------|
| `./` (racine) | Portail Axxam | https://axxam.net |
| `animation/` | axxam.net/animation | https://axxam.net/animation/ |
| `poterie/` | Poterie Axxam Touraine | https://axxam.net/poterie/ |
| `vesemt.org/` | Site VESEMT | https://axxam.net/vesemt.org/ |
| `boxingclubspdc/` | Boxing Club SPDC | https://axxam.net/boxingclubspdc/ |
| `chateauambulant/` | Château Ambulant | https://axxam.net/chateauambulant/ |

Trois **outils internes** sont également accessibles depuis la racine :
- `llm.html` – Chatbot « L'esprit de la rivière » (GLM-4.7 Flash)
- `lettre-motivation.html` – Générateur de lettres de motivation assisté par IA
- `projet-animation.html` – Générateur de projets d'animation (7 blocs)

---

## 📂 Structure détaillée du dépôt

### Racine (`./`)

| Fichier | Rôle |
|---------|------|
| `index.html` | Page hub du portail Axxam |
| `numerique.html` | Page Axxam Numérique (création sites, agents IA, automatisation, impression 3D) |
| `llm.html` | Chatbot « L'esprit de la rivière » |
| `lettre-motivation.html` | Générateur de lettre de motivation |
| `projet-animation.html` | Générateur de projet d'animation |
| `jeu-des-mots.html` | Page de jeu des mots |
| `a-propos.html` → redirige vers `animation/` | Redirection legacy |
| `services.html` → redirige vers `animation/` | Redirection legacy |
| `tarifs.html` → redirige vers `animation/` | Redirection legacy |
| `contact.html` → redirige vers `animation/` | Redirection legacy |
| `hub.css` | Feuille de style du portail |
| `numerique.css` | Feuille de style de numerique.html |
| `CNAME` | Configuration domaine axxam.net |
| `robots.txt` | Configuration robots |
| `sitemap.xml` | Plan du site |
| `favicon.png` | Favicon principal |
| `logo.jpg` | Logo Axxam |
| `googlead63fcf620184b01.html` | Vérification Google Search Console |
| `Thia.pdf` | Document PDF |
| `README.md` | Ce fichier |

---

## 🌐 Présentation des sites

### Portail Axxam (racine)
Page d'accueil unifiée avec grille de cartes donnant accès à tous les sites de l'univers Axxam. Technologie : HTML5 + CSS3 simple, sans framework.

### axxam.net/animation (`animation/`)
Site vitrine d'entrepreneur pour **Axxam, animations créatives et durables**.
- Services en catalogue avec prix (Dès 50 €/heure)
- Page tarifs dédiée (50€/h, 100€/2h, 150€/demi-journée, 250€/journée)
- Fichiers : `index.html`, `a-propos.html`, `contact.html`, `services.html`, `tarifs.html`, `style.css`, `favicon.png`, `logo.jpg`, `logo.rar`

### axxam.net/poterie (`poterie/`)
Site du **tourneur potier Axxam Touraine** : gobelets, cuisson, émaux.
- Galerie filtrable + lightbox
- **Générateur de gobelets 3D** intégré (`poterie/gobelet/`, Three.js via CDN, exports JPG/STL)
- Thème graphite/terracotta, titres Cormorant Garamond
- Fichiers : `index.html`, `pratique.html`, `galerie.html`, `style.css`, `js/galerie.js`, `img/` (placeholders SVG)

### vesemt.org (`vesemt.org/`)
Conversion statique HTML+CSS du site WordPress politique VESEMT (Vivre Surtout Ensemble et Si Possible Solidaires en Métropole Tourangelle).
- 20 pages HTML, 20 images, 1 feuille CSS
- Responsive design, aucun JavaScript (site purement statique)
- Fichiers : `index.html`, `qui-sommes-nous.html`, `politique-confidentialite.html`, `agent.html`, `contacter-reseaux.html`, `elections-municipales-2026.html`, `articles/`, `images/`, `vesemt-css/`, `documentation/`, `tools/`
- Documentation : `README.md`, `RAPPORT_ANALYSE.md`, `JOURNAL-MODIFICATIONS.md`, `RAPPORT-DEPLOIEMENT-AXXAM.md`, `VALIDATION-FOOTER.md`

### axxam.net/boxingclubspdc (`boxingclubspdc/`)
Site PWA du Boxing Club SPDC (Saint-Pierre-des-Corps), refondu en août 2026.
- One-page : disciplines, offres (45€/55€/mois), équipe, événements, galerie filtrable
- Thème noir/rouge (Oswald + Roboto), animations au scroll
- PWA opérationnelle : `manifest.json` + `service-worker.js` en chemins relatifs
- Fichiers : `index.html`, `styles.css`, `js/main.js`, `manifest.json`, `service-worker.js`, `images/`

### chateauambulant (`chateauambulant/`)
Grimoire littéraire documentant le système multi-agents « Foyer de Calcifère ».
- Architecture multi-agents, sécurité (SSRF, cercles d'influence), poésie technique, mémoire
- Thème grimoire (parchemin/or, fontes UnifrakturMaguntia + Cinzel)
- Diagrammes Mermaid.js, mode nuit via localStorage
- Fichiers : `index.html`, `architecture.html`, `securite.html`, `poesie.html`, `memoire.html`, `script.js`, `styles.css`, `README.md`

---

## 🛠️ Outils internes (racine)

### Chatbot « L'esprit de la rivière » (`llm.html`)
- Assistant IA par GLM-4.7 Flash (Zhipu AI), streaming SSE
- Fond eau animé (canvas 2D) respectant `prefers-reduced-motion`
- Parser markdown maison, anti-XSS, liens http(s) uniquement
- Clé API fournie par l'utilisateur

### Générateur de lettre de motivation (`lettre-motivation.html`)
- Application 100% navigateur, aucun backend
- Import CV (.txt/.md/.pdf) + collage offre d'emploi
- Génération streaming, échange de révision, corps d'e-mail d'envoi
- Export : presse-papiers, `.md`, impression

### Générateur de projet d'animation (`projet-animation.html`)
- Assistant IA pour rédiger des projets d'animation (7 blocs structurés)
- Formulaire interactif + chatbot guide par étape
- Explication des objectifs, activités, matériel, évaluation
- Export : presse-papiers, `.md`, impression

---

## 🛠️ Technologies utilisées

| Site / Outil | Technologies |
|-------------|--------------|
| Portail Axxam | HTML5, CSS3 (sans framework) |
| animation/ | HTML5, CSS3, responsive |
| potery/ | HTML5, CSS3, JS Vanilla, Three.js (CDN), Google Fonts |
| vesemt.org | HTML5 sémantique, CSS3 (dossier `vesemt-css/`), sans JavaScript |
| boxingclubspdc | HTML5 sémantique, CSS3, JS ES6+, PWA (Service Worker v2, manifest relatif) |
| chateauambulant | HTML5, CSS3, JS Vanilla, Mermaid.js |
| llm.html | HTML5, CSS3, JS Vanilla, SSE streaming, GLM-4.7 Flash |
| lettre-motivation.html | HTML5, CSS3, JS Vanilla, pdf.js, GLM-4.7 Flash |
| projet-animation.html | HTML5, CSS3, JS Vanilla, SSE streaming, GLM-4.7 Flash |

---

## 📝 Comment modifier les sites

### Portail Axxam (racine)
- Éditer `index.html` (structure) et `hub.css` (styles)
- Les redirections legacy (`a-propos.html`, `services.html`, etc.) pointent vers `animation/`

### animation/
- Éditer `animation/index.html`, `animation/services.html`, `animation/tarifs.html`
- Modifier `animation/style.css` pour le style global
- Les fichiers `a-propos.html`, `contact.html`, `services.html`, `tarifs.html` à la racine redirigent vers `animation/`

### potery/
- Éditer `poterie/index.html`, `poterie/pratique.html`, `poterie/galerie.html`
- Modifier `poterie/style.css` et `poterie/js/galerie.js`
- Le générateur de gobelets vit dans `poterie/gobelet/`
- Remplacer les placeholders SVG dans `poterie/img/` par les vraies photos

### vesemt.org/
- Éditer les 20 pages HTML dans `vesemt.org/`
- Modifier `vesemt.org/vesemt-css/style.css`
- Synchronisation manuelle avec le WordPress original (voir workflow ci-dessous)

### boxingclubspdc/
- Éditer `boxingclubspdc/index.html`
- Modifier `boxingclubspdc/styles.css` et `boxingclubspdc/js/main.js`
- Ajouter photos dans `boxingclubspdc/images/`

### chateauambulant/
- Éditer `chateauambulant/index.html`, `architecture.html`, `securite.html`, `poesie.html`, `memoire.html`
- Modifier `chateauambulant/styles.css` et `chateauambulant/script.js`

---

## 🚀 Déploiement

Les sites sont déployés via **GitHub Pages** :

1. Aller dans **Settings → Pages** du dépôt
2. Branche source : `main`
3. Dossier : `/ (root)`
4. Sauvegarder

Les sites sont ensuite accessibles sous 1-2 minutes :

| Site | URL GitHub Pages | URL domaine |
|------|-----------------|-------------|
| Portail | https://hauuru.github.io/Axxam/ | https://axxam.net |
| Animation | https://hauuru.github.io/Axxam/animation/ | https://axxam.net/animation/ |
| Potery | https://hauuru.github.io/Axxam/poterie/ | https://axxam.net/poterie/ |
| Vesemt | https://hauuru.github.io/Axxam/vesemt.org/ | https://axxam.net/vesemt.org/ |
| Boxing Club | https://hauuru.github.io/Axxam/boxingclubspdc/ | https://axxam.net/boxingclubspdc/ |
| Château Ambulant | https://hauuru.github.io/Axxam/chateauambulant/ | https://axxam.net/chateauambulant/ |

---

## 🔄 Workflow de synchronisation (vesemt.org)

Le dossier `vesemt.org/` est une copie HTML+CSS statique du site WordPress `vesemt.org`. Lorsqu'il évolue :

1. Vérifier les modifications sur le WordPress original
2. Appliquer les changements dans les fichiers HTML/CSS de `vesemt.org/`
3. Tester en local
4. Commiter et pousser sur GitHub
5. GitHub Pages déploie automatiquement

---

## 📚 Documentation interne

| Fichier | Contenu |
|---------|---------|
| `/vesemt.org/README.md` | Installation et structure de vesemt.org |
| `/vesemt.org/RAPPORT_ANALYSE.md` | Rapport d'analyse détaillé |
| `/vesemt.org/JOURNAL-MODIFICATIONS.md` | Historique des modifications |
| `/vesemt.org/RAPPORT-DEPLOIEMENT-AXXAM.md` | Rapport de déploiement |
| `/boxingclubspdc/README.md` | Documentation du site SPDC |
| `/chateauambulant/README.md` | Documentation du Château Ambulant |

---

## 🔧 Scripts et outils utiles

- `googlead63fcf620184b01.html` – Vérification Google Search Console
- `robots.txt`, `sitemap.xml` – SEO et indexation

---

## ⚖️ Licence et droits d'auteur

- **axxam.net** : contenu propriétaire de l'entrepreneur
- **vesemt.org** : basé sur le contenu WordPress original VESEMT – respecter les droits d'auteur originaux
- **boxingclubspdc** : contenu du club – respecter les droits d'auteur originaux
- **chateauambulant** : contenu du Foyer de Calcifère

---

## 📞 Contact

Pour toute question sur le dépôt ou les sites :
- Contacter **hauuru** (propriétaire du dépôt)
- Pour vesemt.org : voir la page `vesemt.org/contacter-reseaux.html`

---

**Dernière mise à jour** : 10 septembre 2026  
**Statut** : ✅ Opérationnel, déployé via GitHub Pages — 6 sites et 3 outils internes en ligne
