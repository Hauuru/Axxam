# Boxing Club SPDC - Site Web

Site web statique du Boxing Club SPDC (Saint-Pierre-des-Corps), déployé sur GitHub Pages.

## Accès

https://axxam.net/boxingclubspdc/

## Structure

```
boxingclubspdc/
├── index.html          # Page principale (one-page)
├── styles.css          # Styles (thème noir / rouge)
├── js/
│   └── main.js         # Nav mobile, galerie, lightbox, formulaire
├── images/             # Photos, galerie, icônes
├── manifest.json       # PWA Manifest
├── sitemap.xml         # Sitemap SEO
├── robots.txt          # Robots.txt
└── service-worker.js   # Service Worker PWA
```

## Contenu

- **Disciplines** : boxe anglaise, fitness, jeunes, coaching
- **Offres** : Jeunes (8-15 ans) 45 €/mois, Adultes (16+) 55 €/mois
- **Horaires** : saison 2026-2027, Gymnase de la Morinerie
- **Contact** : boxingclubspdc@gmail.com

## Formulaire

Le formulaire d'inscription ouvre la messagerie avec un email pré-rempli à
l'adresse du club. Pour utiliser Formspree à la place, remplacer la fonction
`buildMailto` dans `js/main.js` par un fetch vers son endpoint.

## Maintenance

Mettre à jour les informations (horaires, événements, tarifs) dans `index.html`,
les images dans `images/`, puis pousser sur la branche `main`.
