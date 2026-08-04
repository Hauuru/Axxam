# Méthode de conversion WordPress → VESEMT statique

> Ce document décrit le pipeline reproductible pour ajouter un article WordPress
> (https://vesemt.org) au site statique (https://axxam.net/vesemt.org).
> Il complète et met en œuvre la proposition validée dans
> [`PROPOSITION-METHODE.md`](PROPOSITION-METHODE.md) (validée le 04/08/2026).

## Quand l'utiliser

Dès qu'un nouvel article est publié sur le WordPress, ou qu'un article du backlog
encore non converti doit être intégré.

## 1. Découverte des nouveaux articles

Le flux RSS donne la liste des derniers articles (le WordPress n'expose pas
`wp-json` ni `/feed/`, seul `?feed=rss2` fonctionne) :

```bash
python3 tools/backlog.py          # rafraîchit tools/backlog.json (known / pending)
```

`backlog.py` compare le RSS (paged 1..6, ~55 articles) aux articles déjà
convertis (via `tools/registry.json`, construit par `build_registry.py`), avec
une déduplication par similarité de titres (Jaccard ≥ 0,5).

## 2. Conversion d'un article

```bash
python3 tools/convert.py <pID> [--slug mon-slug]
```

Le convertisseur (DOM parser maison, standard library) :

1. récupère `https://vesemt.org/?p=<pID>` ;
2. extrait le titre, la date ISO, l'image à la une, et le corps
   (`<div class="cm-entry-summary">` jusqu'à son `</div>` — la sidebar/wp-widgets
   sont exclus) ;
3. transforme le HTML WP en HTML propre :
   - suppression du tracking Facebook (l.facebook.com, fbclid, __cft__, __tn__),
     des embeds emoji (→ texte alt), des scripts/styles ;
   - `<h1>` de contenu promu en `<h2>` (le titre de page reste un `<h1>`) ;
   - en-têtes markdown `## ` supprimés, paragraphes recomposés ;
   - liens internes WP → placeholders `[[p:N]]` (résolus en fin de batch) ;
4. télécharge les images (`images/<slug>-<nom>.jpg`, redimensionnées ≤ 800 px,
   JPEG q85) ;
5. génère un article au gabarit `articles/bilan-mandat-2020-2026.html`
   (head + OG, nav 5 liens, article-full, tags, partage, commentaires FB) ;
6. met à jour `tools/slugmap.json` (`p:N → slug`) ;
7. imprime la REVUE du contenu : **toujours relire avant intégration**.

### Cas particuliers

- Pas d'image à la une → `Logo.jpg` ; si l'article contient une image, elle est
  utilisée pour `og:image`.
- Caractères unicode dans les URLs (`×`) → encodés et sanitizés dans le nom de fichier.
- Article ne contenant qu'un PDF → lien conservé vers le WordPress d'origine.

## 3. Intégration dans le site

```bash
python3 tools/wire.py
```

`wire.py` :

1. construit la liste maîtresse des articles (`articles/*.html`) ;
2. résout les placeholders `[[p:N]]` → `../articles/<slug>.html` (via slugmap.json) ;
3. réécrit la navigation (5 liens) sur toutes les pages ;
4. chaîne la navigation précédent/suivant de chaque article ;
5. régénère `index.html` : bandeau conservé + liste de **tous** les articles
   (date, titre cliquable, résumé bref) ;
6. régénère `sitemap.xml`.

Si des placeholders restent non résolus (`[[p:N]]`), c'est que le post n'est pas
encore converti : ajouter la correspondance dans `tools/slugmap.json` (comme pour
les anciens posts déjà statiques, ex. `542 → communique-clarification-...`).

## 4. Validation

```bash
# 1. liens internes
python3 /tmp/opencode/checklinks_vesemt.py

# 2. rendu (Playwright, desktop + mobile) sur le serveur local 8099
node /tmp/opencode/crawl_all2.js     # desktop : img + overflow
node /tmp/opencode/mobile_all.js     # mobile  : overflow
```

Critères : 0 fichier cassé, 0 image manquante, 0 overflow (desktop + mobile).

## 5. Publication

```bash
git add -A
git -c user.name="Calcifere-hauuru" -c user.email="leopal147258369@gmail.com" commit -m "vesemt.org: <résumé>"
git push origin main
# vérifier sur GitHub Pages que la page a rebuild, puis :
#   - URL de chaque nouvel article → 200
#   - sitemap.xml contient le bon nombre d'URLs
```

## Récapitulatif des outils (tools/)

| Fichier | Rôle |
|---|---|
| `build_registry.py` | inventaire des articles statiques → `registry.json` |
| `backlog.py` | RSS → `backlog.json` (known / pending, dédupliqué) |
| `convert.py` | `?p=ID` → article HTML + images + `slugmap.json` |
| `wire.py` | index, nav, prev/next, placeholders, sitemap |
| `slugmap.json` | correspondance `p:N → slug` (y compris anciens posts) |

## État du site (après conversion du backlog, 04/08/2026)

- **58 articles** statiques (22 existants + 36 convertis depuis le WordPress),
  du 01/03/2026 au 04/08/2026.
- **5 pages** racine : index, qui-sommes-nous, elections-municipales-2026,
  contacter-reseaux, politique-confidentialite.
- Les pages de catégories (saint-pierre-des-corps, le-quotidien-le-vrai,
  dossiers-metropolitains, vesemt-localement) et la page auteur
  (author-le-plombier) ont été supprimées (présentation simplifiée sans catégories).
- Accueil : bandeau + liste de tous les articles (résumé bref).
