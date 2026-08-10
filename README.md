# Axxam – Dépôt Multi-Sites

Bienvenue dans le dépôt **Axxam**, qui contient plusieurs projets web distincts :

1. **`/`** – **Portail Axxam** : page hub unifiée donnant accès à tous les sites de l'univers Axxam
2. **`/numerique.html`** – **Axxam Numérique** : activités numériques (création de sites web, agents IA locaux, automatisation, dépannage, impression 3D)
3. **`/animation/`** – Site **axxam.net/animation** : site professionnel d'entrepreneur (services en catalogue, page tarifs)
4. **`/poterie/`** – Site **Poterie Axxam Touraine** : tourneur potier, gobelets, cuisson et émaux + générateur de gobelets 3D
5. **`/vesemt.org/`** – Site **vesemt.org** : conversion HTML+CSS du site WordPress politique
6. **`/boxingclubspdc/`** – Site **Boxing Club SPDC** : one-page du club de boxe (refondu août 2026)
7. **`/chateauambulant/`** – Site **Château Ambulant** : grimoire documentant le système multi-agents « Foyer de Calcifère »

---

## 📦 Structure du dépôt

```
Axxam/
├── index.html              ← Page hub : portail vers tous les sites
├── numerique.html          ← Axxam Numérique : création de sites, agents IA, automatisation, dépannage, impression 3D
├── hub.css                 ← Feuille de style du portail
├── animation/              ← Site axxam.net/animation
│   ├── index.html          ← Page d'accueil (animations créatives)
│   ├── a-propos.html       ← À propos
│   ├── contact.html        ← Contact
│   ├── services.html       ← Services en catalogue (axxam.net/animation)
│   ├── tarifs.html         ← Page tarifs (axxam.net/animation)
│   ├── gobelet/            ← Générateur de gobelets paramétrique (dans services)
│   ├── style.css           ← Feuille de style principale
│   └── favicon.png, logo.jpg  ← Ressources
├── a-propos.html, services.html, tarifs.html, contact.html  ← Redirections vers /animation/
├── poterie/                ← Site Poterie Axxam Touraine (axxam.net/poterie/)
│   ├── index.html          ← Accueil : présentation + pièces + encart générateur
│   ├── pratique.html       ← Tournage, cuisson, émaux
│   ├── galerie.html        ← Grille filtrable + lightbox
│   ├── gobelet/            ← Générateur de gobelets paramétrique (axxam.net/poterie/gobelet/)
│   ├── style.css           ← Thème graphite/terracotta
│   ├── js/galerie.js       ← Filtres + lightbox
│   └── img/                ← Placeholders SVG (à remplacer par photos Instagram)
├── CNAME, robots.txt, sitemap.xml  ← Configuration
│
├── vesemt.org/             ← Site HTML+CSS de vesemt.org
│   ├── index.html
│   ├── articles/
│   ├── images/
│   ├── vesemt-css/style.css
│   ├── README.md           ← Documentation détaillée du site vesemt.org
│   ├── RAPPORT_ANALYSE.md
│   └── ... (20 pages HTML)
│
├── boxingclubspdc/         ← Site PWA du Boxing Club SPDC
│   ├── index.html
│   ├── styles.css
│   ├── js/main.js
│   ├── manifest.json, service-worker.js
│   ├── images/
│   ├── README.md           ← Documentation détaillée du site SPDC
│   └── ...
│
└── chateauambulant/        ← Site grimoire du Foyer de Calcifère
    ├── index.html
    ├── architecture.html
    ├── securite.html
    ├── poesie.html
    ├── memoire.html
    ├── script.js, styles.css
    └── README.md           ← Documentation détaillée du Château Ambulant
```

---

## 🌐 Sites hébergés

### Portail Axxam (racine)
- **Page hub** : donne accès à tous les sites de l'univers Axxam via une grille de cartes
- **Section Axxam Numérique** : activités numériques (création de sites web, agents IA locaux, automatisation, dépannage, impression 3D) avec page dédiée `numerique.html`
- HTML+CSS simple et léger, sans framework
- Les anciennes URLs (`/a-propos.html`, `/services.html`, `/tarifs.html`, `/contact.html`) redirigent vers `/animation/`
- Déployé via GitHub Pages sur `https://hauuru.github.io/Axxam/`
- Domaine personnalisé : `https://axxam.net` (via fichier CNAME)

### Axxam Numérique (`numerique.html`)
- Page dédiée aux activités numériques : création de pages web HTML/CSS, initiation aux agents IA hébergés sur l'ordinateur (Nanobot, OpenClaw…), automatisation de tâches simples, dépannage informatique, impression 3D
- Étapes « Comment ça se passe ? » + bandeau contact
- Accessible sur `https://axxam.net/numerique.html`

### axxam.net/animation (sous-dossier)
- Site vitrine d'entrepreneur — **Axxam, animations créatives et durables**
- Services présentés en **catalogue** avec prix (Dès 50 €/heure)
- **Page tarifs** : 50€/h, 100€/2h, 150€/demi-journée, 250€/journée, forfait travail régulier ; matériel facturé en plus
- HTML+CSS simple et léger, sans framework
- Accessible sur `https://axxam.net/animation/`

### poterie (sous-dossier) — Axxam Touraine
- Site **Poterie Axxam Touraine** : tourneur potier (gobelets, ergonomie, cuisson, émaux)
- Multi-pages : accueil, la pratique (tournage/cuisson/émaux), galerie filtrable + lightbox
- **Générateur de gobelets 3D** intégré dans le site (`/poterie/gobelet/`, ex-`/gobelet/`)
- Thème graphite/terracotta, titres Cormorant Garamond, JS vanilla
- Images : placeholders SVG — à remplacer par les photos Instagram `@axxamtouraine`
- Accessible sur `https://axxam.net/poterie/`

### vesemt.org (sous-dossier)
- Conversion statique du site WordPress politique **VESEMT** (Vivre Surtout Ensemble et Si Possible Solidaires en Métropole Tourangelle)
- 20 pages HTML + 20 images + 1 feuille CSS
- Contenu fidèle au site WordPress original
- Responsive design
- Documentation complète dans `/vesemt.org/README.md`

### boxingclubspdc (sous-dossier)
- Site **Boxing Club SPDC** (Saint-Pierre-des-Corps), refondu en août 2026
- One-page : disciplines, offres (45€/55€/mois), équipe, événements, horaires 2026-2027, galerie filtrable + lightbox, TikTok, témoignages, contact
- Thème unifié noir/rouge (Oswald + Roboto), responsive, animations au scroll
- Photos réelles (Unsplash) + favicons/icônes PWA générées
- PWA opérationnelle : manifest + service-worker en chemins relatifs (déploiement sous-sous-dossier)
- Formulaire : envoi réel par email pré-rempli (mailto), plus de Formspree fictif
- Documentation complète dans `/boxingclubspdc/README.md`

### chateauambulant (sous-dossier)
- **Château Ambulant** : grimoire littéraire documentant le système multi-agents « Foyer de Calcifère »
- Architecture multi-agents, sécurité (SSRF, cercles d'influence), poésie technique, mémoire
- Documentation complète dans `/chateauambulant/README.md`

---

## 🔄 Workflow de synchronisation

Le dossier `/vesemt.org/` est une **copie HTML+CSS** du site WordPress `vesemt.org`. Lorsque le site WordPress évolue (nouveaux articles, modifications de design), les changements sont **manuellement reflétés** dans cette version statique :

1. Vérifier les modifications sur le WordPress original
2. Appliquer les changements dans les fichiers HTML/CSS du dossier `vesemt.org/`
3. Tester en local
4. Commiter et pousser sur GitHub
5. GitHub Pages déploie automatiquement

---

## 🛠️ Technologies utilisées

### axxam.net/animation
- HTML5
- CSS3
- Aucun framework
- Responsive design (media queries)
- Catalogue de services avec prix + page tarifs dédiée

### poterie
- HTML5 + CSS3 (Flexbox, Grid, Variables CSS, animations)
- JavaScript Vanilla (filtres galerie + lightbox)
- Génome paramétrique : gobelets 3D (Three.js via CDN), exports JPG/STL
- Responsive design, SEO (Open Graph, sitemap)
- Google Fonts (Cormorant Garamond)

### vesemt.org
- HTML5 sémantique
- CSS3 (dossier `vesemt-css/`)
- Responsive design intégré
- Aucun JavaScript (site purement statique)

### boxingclubspdc
- HTML5 sémantique + CSS3 (Flexbox, Grid, Variables CSS, animations)
- JavaScript Vanilla (ES6+) + PWA (Service Worker v2, manifest relatif)
- Galerie filtrable + lightbox, formulaire mailto
- SEO (Schema.org, Open Graph, sitemap, robots)

### chateauambulant
- HTML5 + CSS3 (thème grimoire : parchemin/or, fontes UnifrakturMaguntia + Cinzel)
- JavaScript Vanilla (mode nuit localStorage) + Mermaid.js (diagrammes)

---

## 🚀 Déploiement

Les sites sont déployés via **GitHub Pages** :

1. **Portail Axxam** : Racine du dépôt → `https://hauuru.github.io/Axxam/`
2. **axxam.net/animation** : Sous-dossier → `https://hauuru.github.io/Axxam/animation/`
3. **poterie** : Sous-dossier → `https://hauuru.github.io/Axxam/poterie/`
4. **vesemt.org** : Sous-dossier → `https://hauuru.github.io/Axxam/vesemt.org/`
5. **boxingclubspdc** : Sous-dossier → `https://hauuru.github.io/Axxam/boxingclubspdc/`
6. **chateauambulant** : Sous-dossier → `https://hauuru.github.io/Axxam/chateauambulant/`

### Activation GitHub Pages
- Aller dans **Settings → Pages** du dépôt
- Branche source : `main`
- Dossier : `/ (root)`
- Sauvegarder

Attendre 1-2 minutes, puis les sites sont accessibles.

---

## 📝 Modification des sites

### Pour **axxam.net** (racine et sous-dossier `animation/`)
- Le **portail** : éditer `index.html` (racine) et `hub.css`
- Le **site animation** : éditer `animation/index.html`, `animation/services.html`, etc.
- Modifier `animation/style.css` pour le style global du site animation
- Commit & push

### Pour **poterie**
- Éditer les fichiers HTML dans `/poterie/` (index, pratique, galerie)
- Modifier `/poterie/style.css` et `/poterie/js/galerie.js`
- Remplacer les placeholders `/poterie/img/*.svg` par les photos réelles (Instagram @axxamtouraine)
- Le générateur vit dans `/poterie/gobelet/` (bouton « ← Retour » déjà intégré)
- Commit & push

### Pour **vesemt.org**
- Éditer les fichiers HTML dans `/vesemt.org/`
- Modifier `/vesemt.org/vesemt-css/style.css`
- Voir le `/vesemt.org/README.md` pour la documentation complète

### Pour **boxingclubspdc**
- Éditer les fichiers HTML dans `/boxingclubspdc/` (one-page `index.html`)
- Modifier `/boxingclubspdc/styles.css` et `/boxingclubspdc/js/main.js`
- Ajouter les photos dans `/boxingclubspdc/images/`
- Voir le `/boxingclubspdc/README.md` pour la documentation complète

### Pour **chateauambulant**
- Éditer les fichiers HTML dans `/chateauambulant/`
- Modifier `/chateauambulant/styles.css` et `/chateauambulant/script.js`
- Voir le `/chateauambulant/README.md` pour la documentation complète

---

## 📚 Documentation

- **`/boxingclubspdc/README.md`** – Documentation du site Boxing Club SPDC (structure, formulaire, maintenance)
- **`/vesemt.org/README.md`** – Documentation du site vesemt.org (installation, structure, déploiement)
- **`/vesemt.org/RAPPORT_ANALYSE.md`** – Rapport d'analyse détaillé et recommandations
- **`/vesemt.org/JOURNAL-MODIFICATIONS.md`** – Historique des modifications du site vesemt.org
- **`/chateauambulant/README.md`** – Documentation du site Château Ambulant

---

## 🔧 Scripts utiles

Dans `/vesemt.org/` :
- `deploy.sh` – Script de déploiement automatisé
- `add-footer-credits.sh` – Ajoute des crédits dans le footer

---

## 🤝 Contribution

Pour modifier ces sites :
1. Fork le dépôt
2. Créer une branche (`git checkout -b feature/ma-modif`)
3. Commiter (`git commit -m 'Ajout de X'`)
4. Pousser (`git push origin feature/ma-modif`)
5. Ouvrir une Pull Request

---

## ⚖️ Licence et droits d'auteur

- **axxam.net** : Contenu propriétaire de l'entrepreneur
- **vesemt.org** : Basé sur le contenu original de VESEMT – respecter les droits d'auteur originaux
- **boxingclubspdc** : Contenu du club – respecter les droits d'auteur originaux
- **chateauambulant** : Contenu du Foyer de Calcifère

---

## 📞 Contact

Pour toute question sur le dépôt ou les sites :
- Contacter **hauuru** (propriétaire du dépôt)
- Pour le site vesemt.org : voir la page `vesemt.org/contacter-reseaux.html`

---

**Dernière mise à jour** : 8 août 2026
**Statut** : ✅ Opérationnel, déployé via GitHub Pages — portail axxam.net, site animation/, poterie (avec générateur de gobelets) et boxingclubspdc en ligne
