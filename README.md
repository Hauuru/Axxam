# Axxam – Dépôt Multi-Sites

Bienvenue dans le dépôt **Axxam**, qui contient deux projets web distincts :

1. **`/`** – Site **axxam.net** : site professionnel d'entrepreneur
2. **`/vesemt.org/`** – Site **vesemt.org** : conversion HTML+CSS du site WordPress politique

---

## 📦 Structure du dépôt

```
Axxam/
├── index.html              ← Page d'accueil axxam.net
├── a-propos.html           ← À propos (axxam.net)
├── contact.html            ← Contact (axxam.net)
├── services.html           ← Services (axxam.net)
├── gobelet.html            ← Page Gobelet (axxam.net)
├── style.css               ← Feuille de style principale (axxam.net)
├── favicon.png, logo.jpg   ← Ressources (axxam.net)
├── CNAME, robots.txt, sitemap.xml  ← Configuration
│
└── vesemt.org/             ← Site HTML+CSS de vesemt.org
    ├── index.html
    ├── articles/
    ├── images/
    ├── vesemt-css/style.css
    ├── README.md           ← Documentation détaillée du site vesemt.org
    ├── RAPPORT_ANALYSE.md
    └── ... (20 pages HTML)
```

---

## 🌐 Sites hébergés

### axxam.net (racine)
- Site vitrine d'entrepreneur
- HTML+CSS simple et léger
- Déployé via GitHub Pages sur `https://hauuru.github.io/Axxam/`
- Domaine personnalisé : `https://axxam.net` (via fichier CNAME)

### vesemt.org (sous-dossier)
- Conversion statique du site WordPress politique **VESEMT** (Vivre Surtout Ensemble et Si Possible Solidaires en Métropole Tourangelle)
- 20 pages HTML + 20 images + 1 feuille CSS
- Contenu fidèle au site WordPress original
- Responsive design
- Documentation complète dans `/vesemt.org/README.md`

---

## 🔄 Workflow de synchronisation

Le fichier `/vesemt.org/` est une **copie HTML+CSS** du site WordPress `vesemt.org`. Lorsque le site WordPress évolue (nouveaux articles, modifications de design), les changements sont **manuellement reflétés** dans cette version statique :

1. Vérifier les modifications sur le WordPress original
2. Appliquer les changements dans les fichiers HTML/CSS du dossier `vesemt.org/`
3. Tester en local
4. Commiter et pousser sur GitHub
5. GitHub Pages déploie automatiquement

---

## 🛠️ Technologies utilisées

### axxam.net
- HTML5
- CSS3
- Aucun framework
- Responsive design (media queries)

### vesemt.org
- HTML5 sémantique
- CSS3 (dossier `vesemt-css/`)
- Responsive design intégré
- Aucun JavaScript (site purement statique)

---

## 🚀 Déploiement

Les deux sites sont déployés via **GitHub Pages** :

1. **axxam.net** : Racine du dépôt → `https://hauuru.github.io/Axxam/`
2. **vesemt.org** : Sous-dossier → `https://hauuru.github.io/Axxam/vesemt.org/`

### Activation GitHub Pages
- Aller dans **Settings → Pages** du dépôt
- Branche source : `main`
- Dossier : `/ (root)`
- Sauvegarder

Attendre 1-2 minutes, puis les sites sont accessibles.

---

## 📝 Modification des sites

### Pour **axxam.net** (racine)
- Éditer `index.html`, `services.html`, etc.
- Modifier `style.css` pour le style global
- Commit & push

### Pour **vesemt.org**
- Éditer les fichiers HTML dans `/vesemt.org/`
- Modifier `/vesemt.org/vesemt-css/style.css`
- Voir le `/vesemt.org/README.md` pour la documentation complète

---

## 📚 Documentation

- **`/vesemt.org/README.md`** – Documentation du site vesemt.org (installation, structure, déploiement)
- **`/vesemt.org/RAPPORT_ANALYSE.md`** – Rapport d'analyse détaillé et recommandations
- **`/vesemt.org/JOURNAL-MODIFICATIONS.md`** – Historique des modifications du site vesemt.org

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

---

## 📞 Contact

Pour toute question sur le dépôt ou les sites :
- Contacter **hauuru** (propriétaire du dépôt)
- Pour le site vesemt.org : voir la page `vesemt.org/contacter-reseaux.html`

---

**Dernière mise à jour** : 2 mai 2026
**Statut** : ✅ Opérationnel, déployé via GitHub Pages
