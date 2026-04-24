# Analyse Technique - VESEMT.org
## Étape 2 - Téléchargement partiel

---

## Informations générales

**URL** : https://vesemt.org
**Type** : WordPress
**Version WordPress** : 6.9.4 (très récente)
**Date d'analyse** : 01/04/2026

---

## Stack technique

### CMS
- **WordPress 6.9.4** : Version récente et maintenue

### Thème
- **ColorMag 4.1.2** (ThemeGrill)
  - Thème magazine/blog populaire
  - Header builder intégré
  - Footer builder intégré
  - Responsive design
  - Support des blocs WordPress (Gutenberg)

### Plugins détectés
1. **Use Any Font**
   - Permet d'utiliser des polices personnalisées
   - Fichier : `uaf.css`

2. **My Calendar 3.7.6**
   - Gestion d'événements/calendrier
   - Scripts : `mcjs.min.js`, `accessible-modal-window-aria.min.js`
   - CSS : `list-presets.css`, `reset.css`

3. **Font Awesome 6.2.4**
   - Icônes vectorielles
   - Deux versions chargées (v4 et v6)

### Bibliothèques JavaScript
- **jQuery 3.7.1** + **jQuery Migrate 3.4.1**
- **BXSlider** (carrousel)
- **News Ticker** (défilement d'actualités)
- **FitVids** (vidéos responsives)
- **WordPress Core JS** (DOM ready, hooks, i18n, a11y)

### Polices
- **Open Sans** (Google Fonts) - Police principale
- **DM Sans** (Google Fonts)
- **Public Sans** (Google Fonts)
- **Roboto** (Google Fonts)
- **IBM Plex Serif** (locale)
- **Inter** (locale)

---

## Structure du site

### Navigation
- Menu principal avec sous-menus
- Navigation mobile responsive
- 7 sections principales :
  1. Accueil
  2. Qui sommes nous ?
  3. Elections Municipales 2026 (avec 3 sous-catégories)
  4. Contacter- réseaux
  5. Politique de confidentialité
  6. VESEMT LOCALEMENT

### Layout
- **Header** : Logo, titre, description, image de bandeau
- **Contenu** : Grille 2 colonnes d'articles
- **Footer** : Copyright minimaliste

### Catégories
- Le quotidien, le vrai
- Saint-Pierre-des-Corps
- Elections Municipales 2026
  - Le quotidien, le vrai
  - La Gôche Unie et Ecologiste
  - Saint-Pierre Autrement
- VESEMT LOCALEMENT

---

## Palette de couleurs personnalisée

```css
--cm-color-1: #F44336    /* Rouge principal */
--cm-color-2: #D12729    /* Rouge foncé */
--cm-color-3: #FFFFFF    /* Blanc */
--cm-color-4: #FEF6F4    /* Blanc cassé */
--cm-color-5: #0F000A    /* Noir très foncé */
--cm-color-6: #252020    /* Gris foncé */
--cm-color-7: #7E7777    /* Gris moyen */
--cm-color-8: #FFFFFF    /* Blanc */
--cm-color-9: #C1BDBD    /* Gris clair */
```

Couleur d'accentuation : `#207daf` (bleu)

---

## Points techniques positifs

✅ **WordPress à jour** : Version 6.9.4 (dernière stable)
✅ **Thème maintenu** : ColorMag est activement développé
✅ **Responsive** : Design mobile-first
✅ **Accessibilité** : Scripts A11y WordPress chargés
✅ **Performance** : Pas de scripts lourds inutiles détectés
✅ **Structure sémantique** : HTML5 bien structuré

---

## Points techniques à améliorer

⚠️ **Plugins multiples** :
- Font Awesome chargé 2 fois (v4 et v6)
- Possibles conflits ou redondances

⚠️ **Polices externes** :
- 4 polices Google Fonts chargées
- Peut impacter les performances sur connexion lente

⚠️ **jQuery** :
- jQuery + jQuery Migrate chargés
- WordPress moderne peut s'en passer

⚠️ **Pas de cache détecté** :
- Pas d'indication de plugin de cache (WP Rocket, W3 Total Cache, etc.)
- Peut impacter les performances

⚠️ **Mixed content** :
- Certaines ressources en HTTP (`http://vesemt.org/...`)
- Devrait être en HTTPS pour la sécurité

⚠️ **Pas d'optimisation d'images** :
- Images chargées directement sans indication de compression
- Pas de plugin d'optimisation d'images détecté

---

## Structure des URLs

**Format actuel** : `?p=XXX` (paramètres de requête)
**Recommandé** : URLs propres (`/titre-de-l-article/`)

WordPress est configuré en mode "par défaut" pour les permaliens.

---

## Taille estimée du projet

**Téléchargé** : ~104 Ko (HTML uniquement)
**Estimation totale** : ~50-200 Mo
- Thème ColorMag : ~5-10 Mo
- Plugins : ~10-20 Mo
- Uploads (images) : ~30-150 Mo
- WordPress core : ~20-30 Mo

---

## Recommandations techniques

### Immédiat (facile)
1. **Activer les permaliens propres** dans WordPress
2. **Forcer HTTPS** pour toutes les ressources
3. **Désactiver Font Awesome v4** (garder v6 uniquement)
4. **Installer un plugin de cache** (WP Rocket ou W3 Total Cache)

### Court terme
1. **Optimiser les images** (Smush ou EWWW Image Optimizer)
2. **Réduire le nombre de polices Google** (garder Open Sans uniquement)
3. **Supprimer jQuery Migrate** si non nécessaire
4. **Activer la compression GZIP** (via .htaccess ou plugin)

### Moyen terme
1. **Audit de sécurité** (Wordfence ou iThemes Security)
2. **Optimisation de la base de données** (WP-Optimize)
3. **CDN pour les assets statiques** (Cloudflare ou KeyCDN)

---

## Décision

**Continue → Étape 3**

Le site est un WordPress standard avec une complexité technique gérable. Aucune contrainte technique majeure détectée. L'estimation de taille (~50-200 Mo) reste bien dans la limite des 20 Go.

L'étape 3 (clone complet) permettra :
- D'analyser les fichiers de configuration
- De tester localement
- De proposer des modifications concrètes
- D'optimiser les performances

---

## Contraintes respectées

✅ Taille estimée : < 20 Go
✅ Complexité technique : WordPress standard
✅ Pas de dépendances externes complexes
✅ Pas de services requis (base de données accessible via WordPress)
