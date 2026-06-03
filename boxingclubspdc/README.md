# Boxing Club SPDC - Site Web Optimisé

Site web statique optimisé pour le Boxing Club SPDC (Saint-Pierre-des-Corps), déployé sur GitHub Pages.

## 🚀 Caractéristiques

### 📱 Responsive Design
- Design mobile-first
- Compatible tous les navigateurs modernes
- Support des écrans retina
- Optimisé pour tablettes et desktop

### 🎯 SEO Optimisé
- Meta tags complets
- Structured Data (Schema.org)
- Sitemap XML
- Robots.txt
- Open Graph / Twitter Cards
- SEO sémantique HTML5

### ⚡ Performance Optimisée
- Lazy loading des images
- Compression Gzip
- Caching HTTP headers
- Service Worker pour offline support
- Preloading des ressources critiques
- Optimisation CSS/JS

### 🎨 Design Moderne
- Animations CSS fluides
- Menu sticky avec blur effect
- Lightbox interactive
- Galerie filtrable
- Micro-interactions
- Support dark mode

### 🔧 Fonctionnalités
- Formulaire Formspree intégré
- Section TikTok intégrée
- Horaires d'entraînement
- Témoignages membres
- Galerie photos avec lightbox
- Contact et inscription

## 📁 Structure des Fichiers

```
boxingclubspdc/
├── index.html          # Page principale
├── styles.css          # Styles CSS optimisés
├── js/
│   └── main.js         # JavaScript optimisé
├── images/             # Assets images
├── manifest.json        # PWA Manifest
├── browserconfig.xml    # Windows 8/10/11 Tile
├── sitemap.xml         # Sitemap SEO
├── robots.txt          # Robots.txt
├── .htaccess           # Configuration serveur
├── service-worker.js   # Service Worker PWA
└── README.md          # Documentation
```

## 🛠️ Technologies

- **HTML5** - Sémantique et accessibilité
- **CSS3** - Flexbox, Grid, Animations, Variables CSS
- **JavaScript Vanilla** - ES6+, Performance, PWA
- **PWA** - Progressive Web App features
- **SEO** - Optimisation pour moteurs de recherche

## 📊 Métriques Performance

- **PageSpeed Score**: 90+ (optimisé)
- **First Contentful Paint**: < 1s
- **Largest Contentful Paint**: < 2.5s
- **Cumulative Layout Shift**: < 0.1
- **Time to Interactive**: < 3.5s

## 🌐 Déploiement

Le site est déployé sur GitHub Pages à l'adresse:
https://axxam.net/boxingclubspdc/

### Configuration GitHub Pages
1. Repository: `Hauuru/Axxam`
2. Branch: `main`
3. Folder: `/boxingclubspdc`
4. Custom domain: `axxam.net/boxingclubspdc`

## 🔧 Personnalisation

### Modifier les informations du club
Éditez `index.html` pour mettre à jour:
- Coordonnées
- Horaires
- Tarifs
- Informations de contact

### Ajouter des images
Placez les images dans le dossier `images/` et mettez à jour les chemins dans `index.html`.

### Configurer Formspree
1. Créez un formulaire sur Formspree
2. Mettez à jour l'URL dans `js/main.js`
3. Configurez les champs du formulaire

### Intégrer TikTok
Mettez à jour l'URL TikTok dans la section TikTok:
```html
<div class="tiktok-video">
    <blockquote class="tiktok-embed" cite="https://www.tiktok.com/@boxespdc" data-embed-type="post" data-embed-id="ID_VIDEO">
        <section></section>
    </blockquote>
</div>
```

## 📱 Support PWA

Le site supporte les fonctionnalités PWA:
- Installation sur mobile
- Support offline
- Notifications push
- App-like experience

### Installation PWA
Sur mobile:
1. Chrome: Menu → Ajouter à l'écran d'accueil
2. Safari: Partager → Ajouter à l'écran d'accueil

## 🔐 Sécurité

- HTTPS obligatoire
- Headers de sécurité
- Protection XSS
- Protection CSRF
- CSP (Content Security Policy)

## 📈 Analytics

Intégrez Google Analytics ou autre service en ajoutant le code de suivi dans `index.html` avant la fermeture du `</head>`.

## 🔄 Maintenance

### Mises à jour régulières
- Vérifier les liens morts
- Mettre à jour le contenu
- Optimiser les images
- Tester la compatibilité

### Monitoring
- Performance avec Google PageSpeed
- SEO avec Google Search Console
- Uptime avec services de monitoring

## 🤔 Dépannage

### Problèmes courants
1. **Images qui ne s'affichent pas**: Vérifier les chemins et les permissions
2. **JavaScript non fonctionnel**: Vérifier la console d'erreurs du navigateur
3. **CSS non appliqué**: Vérifier les chemins et le cache
4. **Mobile responsive**: Tester sur différents appareils

### Outils de développement
- Chrome DevTools
- Firefox Developer Tools
- Lighthouse
- WebPageTest

## 📝 Licence

Ce projet est open source. Voir le fichier de licence pour plus d'informations.

## 🤝 Contribuer

1. Fork le projet
2. Créez une branche (`git checkout -b feature/amélioration`)
3. Committez vos changements (`git commit -am 'Nouvelle fonctionnalité'`)
4. Poussez vers la branche (`git push origin feature/amélioration`)
5. Créez un Pull Request

---

**Dernière mise à jour**: 3 juin 2026  
**Version**: 1.0.0  
**Auteur**: Cassius  
**Contact**: boxingclubspdc@gmail.com