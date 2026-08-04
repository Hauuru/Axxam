# PROPOSITION DE MÉTHODE — Conversion WordPress → site statique VESEMT

**Statut : VALIDÉ le 04/08/2026**
**Décisions §3.3 actées par l'utilisateur**
**Date : 04/08/2026**

---

## 1. Objectif

Le site statique (https://axxam.net/vesemt.org) va grossir : Le Plombier publie régulièrement.
Cette proposition définit :

1. une **présentation simplifiée** du site (fini les catégories, accueil = bandeau + liste de tous les articles) ;
2. une **méthode de conversion reproductible** WordPress → article statique, à la demande ;
3. un **plan d'application** au backlog (~26 articles en attente).

## 2. Constats (vérifiés le 04/08/2026)

- **Source disponible** : le flux `https://vesemt.org/?feed=rss2` répond (30 articles visibles via `paged=1..3`). Chaque article `https://vesemt.org/?p=ID` fournit : titre, date (`datetime` ISO), auteur (Le Plombier), image à la une (`colormag-featured-image`), contenu complet (paragraphes, titres, listes, blockquotes, liens).
- **Backlog estimé** : après dédoublonnage avec les articles déjà convertis (p=592, 603, 611, 622), **~26 articles** (juin → août 2026) sont à convertir.
- **Gabarit article existant** : `articles/bilan-mandat-2020-2026.html` sert de référence (head/OG/Twitter, header+nav, `article-full`, partage, footer, FB SDK).

## 3. Présentation cible (simplifiée)

### 3.1 Nouvelle structure
```
vesemt.org/
├── index.html                  # Accueil : bandeau + liste de TOUS les articles (résumé très bref)
├── articles/<slug>.html        # Un fichier par article (gabarit standard)
├── pages fixes conservées :
│   ├── qui-sommes-nous.html
│   ├── contacter-reseaux.html
│   ├── politique-confidentialite.html
│   └── elections-municipales-2026.html   # page info (à trancher, voir §3.3)
├── images/  vesemt-css/  sitemap.xml  robots.txt
```

### 3.2 Accueil (index.html)
- **Bandeau** : héros existant conservé (identité visuelle), allégé.
- **Liste de tous les articles** : tri du plus récent au plus ancien, **un seul bloc d'entrée par article** :
  - date (format court), titre cliquable, **résumé très bref** (≈1 ligne, les ~150 premiers caractères du contenu nettoyé) ;
  - clic → article.
- **Aucune catégorie** : ni cartes à thèmes, ni pages catégories, ni liens catégorie dans les articles.

### 3.3 Décisions actées
| Point | Décision |
|---|---|
| Nav principale | Simplifiée à : **Accueil · Qui sommes-nous ? · Élections 2026 · Contacter-réseaux · Politique de confidentialité** |
| Pages catégorie (`saint-pierre-des-corps.html`, `le-quotidien-le-vrai.html`, `dossiers-metropolitains.html`, `vesemt-localement.html`) | **Supprimées** |
| Bandeau héros | **Image actuelle conservée** |
| Lien « catégorie » dans le header d'article | **Supprimé** (cohérent avec la fin des catégories) |
| Tags dans le footer d'article | **Conservés, non cliquables** |

## 4. Méthode de conversion (pipeline)

Flux par article, reproductible et partiellement automatisable. Un **point de relecture** reste prévu (embeds Facebook, entités HTML, liens `?p=N` : rien ne doit arriver cassé en production).

1. **Découverte** — lecture RSS → liste `?p=ID` → dédoublonnage (par `?p=` ou titre) contre `articles/` → backlog.
2. **Récupération** — téléchargement de `https://vesemt.org/?p=ID`.
3. **Extraction** — titre, date ISO, auteur, image à la une, corps nettoyé (classes WP supprimées, entités `&rsquo;`… résolues, shortcodes retirés).
4. **Transformation** — slug (accent-nettoyé, kebab-case), génération du HTML à partir du gabarit, **liens internes `?p=N` réécrits vers `articles/<slug>.html`** (dédoublonnés au moment du batch).
5. **Médias** — image à la une → `images/<slug>-800x445.jpg` (Pillow, JPEG q85, largeur ≤ 800).
6. **Intégration** — entrée ajoutée dans la liste d'accueil (§3.2), `sitemap.xml` régénéré, chaînage prev/next des voisins mis à jour.
7. **Validation** — 0 lien interne cassé, 0 image cassée, Playwright desktop+mobile (0 erreur JS, pas d'overflow), relecture du contenu.
8. **Publication** — commit → push → attendre Pages « built » → vérification 200 en ligne.

### Conventions
- Slug : titre accent-nettoyé → kebab-case (ex. `DE RUGY DÉCOUVRE LA CHALEUR…` → `de-rugy-decouvre-la-chaleur-saint-pierre-des-corps.html`).
- Image : largeur ≤ 800, JPEG q85, nom `<slug>-800x445.jpg` ; à défaut d'image à la une, fallback `Logo.jpg`.
- Date : ISO dans `<time datetime>`, affichée format français.
- Résumé bref : ~150 caractères extraits du contenu, complété de « … ».

## 5. Plan d'exécution (phases)

### Phase 0 — Conventions & validation du présent document
- Valider §3.3 (structure cible), figer les conventions §4.
- Créer `articles/etat-conversion.md` : registre ID WP ↔ fichier statique ↔ statut.

### Phase 1 — Outillage
- `tools/fetch_backlog.py` : découverte RSS + dédoublonnage + export du backlog.
- `tools/convert_article.py` : extraction → article HTML (gabarit) + image.
- `tools/wire.py` : intégration accueil + sitemap + prev/next.
- `tools/check_site.py` : liens + images + Playwright (réutilisation des tests existants).

### Phase 2 — Pilote (2 articles réels)
- 1 article simple + 1 article riche (embeds, liens, citation).
- Conversion, relecture, validation complète, ajustements de l'outil.
- Rebase du backlog si nécessaire (titres différents → nouveaux ?p= à ajouter).

### Phase 3 — Restructuration accueil (§3.2/§3.3)
- Réécriture d'`index.html` : bandeau + liste de tous les articles (résumés brefs).
- Simplification de la nav sur toutes les pages, suppression des pages catégories validées.
- Mise à jour des articles existants (retrait du lien catégorie, liens internes).

### Phase 4 — Lot 1 : 10 articles les plus récents (juil–août 2026)
- Conversion par article (pipeline §4), relecture, publication par sous-lots de 2-3.

### Phase 5 — Lot 2 : reste du backlog (~16 articles)
- Même processus.

### Phase 6 — Documentation & base de données
- `documentation/CONVERSION-METHODE.md` (playbook humain/IA, exemple pas-à-pas).
- README + base `anyclaw.db` (`vesemt_*`) mis à jour.

### Phase 7 — Récurrence (routine « nouvel article »)
- À chaque publication du Plombier : relancer `fetch_backlog.py` → convertir les seuls nouveaux → valider → publier.
- Check de santé du site inclus à chaque publication.

## 6. Critères de validation (définition de « fait »)
- [ ] 0 lien interne cassé, 0 image cassée, 0 erreur JS (desktop + mobile)
- [ ] Chaque article du backlog a un fichier statique et une entrée d'accueil
- [ ] Accueil liste **tous** les articles, résumé très bref, tri antéchronologique
- [ ] Aucun lien `?p=` interne ne mène vers une page absente
- [ ] Sitemap = nombre exact de pages/article
- [ ] Pages « built » et vérification 200 sur les URL clés

## 7. Points de vigilance
- **Contenu politique vivant** : chaque article doit être relu avant publication.
- **Embeds** (Facebook, vidéos) : à remplacer par un lien texte propre.
- **Liens croisés** entre articles WP : à résoudre en fin de batch (le mapping complet `?p=`→slug est connu).
- Ne pas toucher à la racine du dépôt (CNAME, sitemap racine, google…html).
