# Analyse de travail — Générateur de Gobelets (`gobelet/index.html`)

> Document de travail. Objectif : partir de la logique d'utilisation, recenser les
> erreurs, proposer des modifications. La **simplification** est favorisée.
> État : analyse du 07/08/2026 — **voies B puis A appliquées** (voir §6).
> Fichier : 1601 lignes (1498 après refactor), application 3D autonome (Three.js r128 via CDN).

---

## 1. Logique d'utilisation (avant le détail technique)

### 1.1 À quoi sert l'outil
C'est un **outil de CAO-lite pour céramiste** : paramétrer un gobelet en argile et
obtenir en temps réel :
- la géométrie 3D de la pièce dans ses **3 états physiques** (cru → sec → cuit) ;
- l'**ébauche** (brut de tournage) et sa comparaison avec la pièce finie ;
- des **statistiques** (volume contenu, volume argile, poids, argile à enlever) ;
- des **exports** : fiche technique JPG A4 annotée + STL pour impression 3D.

### 1.2 Le parcours utilisateur actuel (ce qui se passe vraiment)
1. On entre les dimensions **cuits** (finales), on règle les **anneaux** (nombre,
   hauteur, largeur, saillie), les **matériaux** (densités/retraits) et les
   **marges de tournage**.
2. On bascule l'**état visualisé** (Cru/Sec/Cuit) pour voir la pièce à chaque étape,
   et le **mode** (Gobelet / Ébauche / Comparaison).
3. On valide visuellement, puis on exporte JPG et/ou STL.

### 1.3 Ce qui part "dans tous les sens" côté usage (problèmes d'expérience)

**U1 — Aucune persistance.** Tous les réglages sont perdus à chaque rechargement de
page. Pas de sauvegarde/chargement, pas de partage par URL, pas de presets.
Pour un outil d'atelier, c'est le manque le plus dommageable : on ne peut ni
retrouver un modèle, ni envoyer une config à un collègue. → **Action forte** :
persistance `localStorage` + export/import JSON (et éventuellement un hash d'URL).

**U2 — Page orpheline.** `gobelet/index.html` n'est référencée par **aucune page du
site** (ni accueil ni nav). Depuis le déplacement, seule l'URL directe y donne accès.
→ **Action** : ajouter un lien (ex. dans la page Services ou l'accueil), ou assumer
son caractère d'outil interne.

**U3 — L'état visualisé (Cru/Sec/Cuit) mélange "voir" et "calculer".** Le même
sélecteur modifie à la fois l'affichage 3D *et* les statistiques (volume, poids,
densité affichée). Un novice peut croire que le "volume contenu" change alors qu'il
ne fait que suivre l'état affiché. La capacité utile, c'est celle du **cuit**, quel
que soit l'état regardé. → **Action** : découpler « état affiché » (pure 3D) et
« chiffres de référence » (toujours calculés en cuit), ou ajouter une mention
explicite "chiffres à l'état : Cuit".

**U4 — Pas de réinitialisation.** Aucun bouton "Réinitialiser" ni retour arrière.
→ **Action** : bouton reset + (si possible) historique/undo simple.

**U5 — Des libellés trompeurs.**
- "Export JPG **(600 DPI)**" : le rendu est fait en 3508×2480, soit du **300 DPI**
  A4 paysage (4960×7016 serait du 600 DPI). Le libellé ou la résolution est faux.
- "**Échelle 1:1**" (sur l'export) : la barre d'échelle "60 mm" n'est **pas
  calibrée** — la caméra n'est jamais réglée pour que 1 pixel = 1 valeur réelle.
  La mention 1:1 est donc inexacte et peut induire en erreur (plan pris pour une
  mise à l'échelle exacte).

---

## 2. Erreurs et défauts techniques (par module)

### 2.1 Fonctionnalités mortes (options affichées mais sans effet)

| # | Élément | Endroit | Constat |
|---|---------|---------|---------|
| F1 | **Grille JPG** (5/1/10mm/Aucune) | HTML : 292-295 | Les boutons radio ne sont **jamais lus** par le JS. Aucun code ne dessine de grille. |
| F2 | **Cases annotations** "Échelle"/"Date" | HTML : 302-304, JS : 1205 | Seul `annotations.length > 0` est testé : décochant "Échelle" ou "Date", **rien ne change** (tout est toujours dessiné). |
| F3 | **Résolution STL** (Haute/Moyenne/Basse) | JS : 1302-1309 | `segments` est calculé mais **jamais utilisé** : le mesh exporté est toujours le mesh courant (64 segments). |
| F4 | Case "Afficher section" (coupe) | JS : 1043, 1056 | Ne modifie que le texte de l'indicateur. N'a **aucun effet sur le rendu**. |
| F5 | Fonction `updateCutawayPreview()` | JS : 1036 | Définie, **jamais appelée**. |
| F6 | Option STL "Comparaison" | JS : 1324-1326 | Exporte seulement l'ébauche (identique à l'option "Ébauche"). Le contenu promis (comparaison) n'existe pas. |

> Constat global : **au moins 6 options d'export affichées n'ont aucun effet**.
> Pour un outil pro, c'est le point le plus rentable à nettoyer : soit on les
> implémente, soit (recommandé) on les supprime.

### 2.2 Incohérences du modèle 3D (les plus sérieuses)

**B1 — Le mode "Comparaison" est faux : le gobelet traverse l'ébauche.**
Dans `genererProfilEbauche` (ligne 834-841) et `volumeEbauche` (ligne 1086), la
cavité de l'ébauche est construite avec `getRayonInterieurGobelet(...)`, c'est-à-dire
le rayon **intérieur du gobelet**. Or pour contenir le gobelet, la cavité de
l'ébauche doit être ≥ **rayon extérieur du gobelet + marge latérale**.
Vérifié numériquement (défauts) : rayon ext. gobelet à la base = **25 mm**,
cavité ébauche = **20 mm** → le gobelet recoupe la paroi de l'ébauche de 5 mm.
→ **Conséquence** : le mode Comparaison et le volume d'ébauche sont basés sur une
géométrie erronée. L' "argile à enlever" en découle.
→ **Actions possibles** :
  a) *Correction* : cavité = rayon extérieur gobelet + `MargeLat`.
  b) *Simplification* : retirer le mode Comparaison et l'ébauche de l'app (voir §3).

**B2 — Le fond du gobelet n'a pas d'épaisseur dans le modèle 3D.**
`genererProfilGobelet` (ligne 809-811) trace la paroi intérieure jusqu'à `h = 0` :
la cavité descend **jusqu'au bas de la pièce** (fond ouvert). En réalité le fond doit
être plein sur une épaisseur ≥ `Ep`. Vérifié : profondeur cavité 3D = **90 mm** alors
que la capacité calculée (`volumeContenu`, ligne 1115) part d'une profondeur utile
de **82 mm** (90 − Ep 5 − Rbord 3). → Le **rendu 3D et la capacité affichée se
contredisent** (la pièce affichée "fuirait").
→ **Action** : fermer le profil au fond à `h = Ep` (et aligner les deux modèles).

**B3 — Épaisseur du fond de l'ébauche incohérente.**
Le profil 3D de l'ébauche place le plancher de la cavité à `margeFond + Ep`
(ligne 845), mais le calcul de volume (`volumeEbauche`, ligne 1086) considère un
plein jusqu'à `margeFond` seulement. → Écart de `Ep` entre 3D et calcul.
→ **Action** : n'utiliser qu'une seule valeur (recommandé : `margeFond + Ep`) dans
les deux endroits.

### 2.3 Export JPG

**B4 — Cadrage non maîtrisé.** `captureJPG` (ligne 1223-1229) rend la scène en
3508×2480 en changeant seulement `camera.aspect`, sans repositionner/cadrer l'objet.
Or la composition change avec le ratio (FOV horizontal) : l'export peut être décentré,
recadré ou le gobelet trop petit sur la page. Aucun calcul de boîte englobante n'est
fait. → **Action** : calculer un cadrage automatique de l'objet à la taille cible
(fit bounding box), ou exporter en conservant l'angle de vue actuel mais en
recentrant l'objet.

**B5 — Chevauchement d'annotations.** Quand la coupe est active, le bandeau
"VUE EN COUPE" (ligne 1470) est dessiné **au même coin** que le bloc de paramètres
(ligne 1394) → chevauchement. → **Action** : décaler l'un des deux.

**B6 — Rendu 3D écrasé par le bloc blanc des annotations.** Le bloc "GOBELET
PARAMÉTRÉ" est dessiné **sur** le rendu 3D (fond blanc opaque, ligne 1394) : si le
gobelet est cadré en haut à gauche, il est masqué. → **Action** : réserver l'espace
annotations (ou décaler le cadrage), pas de recouvrement.

### 2.4 Divers / robustesse

**B7 — Duplication des valeurs par défaut.** Les valeurs initiales existent **en
double** : dans `state` (ligne 426-449) *et* dans `paramDefinitions` (ligne 531-557).
Risque réel de divergence (on change l'un, pas l'autre). → **Action** : une seule
source de vérité (générer `state` depuis `paramDefinitions`, ou l'inverse).

**B8 — Export STL fragile.** `exportSTL` (ligne 1317-1326) clone les meshes dans un
`Group` détaché de la scène. Les `matrixWorld` des enfants (surtout les anneaux)
peuvent être périmés selon les versions de l'exporteur Three.js ; le positionnement
final du STL est donc **non garanti** (décalage possible en Y). Aucune validation
n'existe. → **Action** : soit figer le comportement (tester le STL produit),
soit simplifier (exporter la géométrie "à plat" avec `applyMatrix4` explicite).

**B9 — Le volume contenu utilise la formule du tronc de cône** (ligne 1118) alors
que les parois sont incurvées (`Cv`). Approximatif dès que `Cv` est élevé.
→ **Action** : intégrer par tranches comme les autres volumes (cohérent et simple).

**B10 — "600 DPI" / taille A4** : cf. U5. Le bloc d'annotations utilise aussi
`FACTEUR_AGRANDISSEMENT = 2.5` (ligne 1381) lié à la base 3508 : tout recalibrage de
taille d'export obligera à retoucher ce facteur. À fiabiliser.

---

## 3. Propositions de simplification (à valider ensemble)

L'outil cumule ~6 fonctionnalités mortes et 2 incohérences de modèle majeures.
Deux voies :

### Voie A — "Nettoyage" (chirurgical, conserve tout le périmètre)
1. Supprimer les options mortes (F1, F2, F3, F4, F5, F6) — **suppression simple**,
   aucune perte fonctionnelle réelle.
2. Corriger les bugs de modèle (B1, B2, B3) — aligner cavité ébauche, fond du
   gobelet et fond d'ébauche entre 3D et calculs.
3. Corriger les exports (B4, B5, B6, B9) — cadrage auto, séparation des zones,
   volume par tranches.
4. Fiabiliser (B7, B8) + persistance (U1) + lien depuis le site (U2).

### Voie B — "Réduction de périmètre" (fortement simplificatrice)
L'ébauche + la comparaison + les marges de tournage forment le cœur des
incohérences (B1/B2/B3) et compliquent l'UI (2 sélecteurs d'état). On peut :
1. **Retirer l'ébauche et la Comparaison** (mode "Gobelet" uniquement) : supprime
   `genererProfilEbauche`, `getRayonExterieurEbauche`, la moitié de
   `volumeEbauche`, les marges de tournage, et les statistiques "Volume ébauche /
   Argile à enlever / Taux d'enlèvement".
2. Conserver : dimensions + anneaux + matériau + état cru/sec/cuit (3D) +
   volumes/poids + exports JPG/STL.
3. Résultat : **~40 % du code en moins**, plus de comparaison fausse, plus de
   conflit de fond d'ébauche, stats simples et cohérentes.

> **Recommandation personnelle** : Voie B pour la solidité (retirer ce qui est faux
> plutôt que le réparer), **puis** Voie A pour le reste. L'ébauche n'est utile que
> si on maîtrise la définition physique de la cavité ; dans l'état actuel elle est
> source de bugs et d'UI complexe.

---

## 4. Décisions à prendre (mini-questionnaire)

1. **Périmètre** : Voie A (nettoyage), Voie B (retrait ébauche/comparaison), ou les
   deux (recommandé) ?
2. **Persistance** : ajouter sauvegarde `localStorage` + export/import JSON + partage
   par URL ?
3. **Lien** : référencer la page depuis l'accueil/services, ou outil interne ?
4. **Exports** : conserver JPG (avec grille réellement implémentée ou supprimée) et
   STL (avec résolution réellement appliquée ou supprimée) ?
5. **Échelle 1:1** : supprimer l'annotation, ou implémenter un vrai calibrage
   (camera orthographique proportionnelle aux dimensions) ?

---

## 5. Annexes techniques (références de code)

| Sujet | Ligne(s) |
|---|---|
| État global + getters d'échelle | 426-490 |
| Défauts dupliqués (`state` / `paramDefinitions`) | 426-449 / 531-557 |
| Profil gobelet (fond non fermé, B2) | 774-814 |
| Profil ébauche (cavité = rayon intérieur, B1) | 816-849 |
| Cavité ébauche (B1) | 834-841, 1086 |
| Fond d'ébauche incohérent (B3) | 845 vs 1086 |
| Volume contenu (tronc de cône, B9) | 1111-1119 |
| Export JPG : aspect seul, pas de cadrage (B4) | 1223-1229 |
| Annotations : bloc fixe + chevauchement coupe (B5/B6) | 1394-1477 |
| Export STL : `segments` inutilisé (F3) | 1302-1309 |
| Export STL : cas "comparaison" (F6) | 1324-1326 |
| Grille JPG jamais lue (F1) | 292-295 (HTML) |
| Cases annotations ignorées (F2) | 302-304 (HTML), 1205 (JS) |
| `showCutSection` décoratif (F4) | 1043, 1056 |
| `updateCutawayPreview` jamais appelée (F5) | 1036 |

---

## 6. Modifications appliquées (07/08/2026, voies B puis A)

Décision utilisateur : **« B puis A »** — retrait de l'ébauche/comparaison/marges
(Voie B) puis nettoyage et corrections (Voie A).

**Voie B — retrait de l'ébauche, de la comparaison et des marges de tournage**
- Supprimé : `genererProfilEbauche`, `getRayonExterieurEbauche`, `volumeEbauche`,
  `getMargeAjustee`, les paramètres `MargeLat/MargeSup/MargeFond`, le mode
  `visualisation` (gobelet/ebauche/comparaison), le mesh `ebaucheMesh`.
- Supprimé de l'UI : onglet « Tournage » → remplacé par l'onglet **« États »**
  (Cru/Sec/Cuit, sans marges ni mode de visualisation) ; stats
  « Volume ébauche / Argile à enlever / Taux d'enlèvement » ; le rendu ébauche et
  le décalage `position.y` lié à la marge de fond.
- Résolu : B1 (plus de comparaison fausse), B3 (plus de conflit de fond d'ébauche).

**Voie A — nettoyage et corrections**
- B2 : le profil du gobelet se ferme désormais au fond à `h = Ep` (fond plein,
  cohérent avec la capacité).
- B9 : `volumeContenu` intégré **par tranches** (200) comme les autres volumes
  (fini le tronc de cône approximatif) ; `volumeParoi` renommé depuis
  `volumeGobeletFinal`.
- F1/F2/F3 : grille JPG, cases d'annotations individuelles et résolution STL
  supprimées (checkbox unique « Afficher les annotations », format binaire/ASCII
  seul). F5 : `updateCutawayPreview` supprimée.
- F4 : case « Afficher section » supprimée (l'indicateur de coupe ne mentionne
  plus d'option sans effet).
- B4 : `captureJPG` calcule un **cadrage automatique** (boîte englobante
  gobelet ± anneaux, `camera.position` recentrée, near/far ajustés).
- B5/B6 : le bandeau « VUE EN COUPE » est dessiné sur un bloc blanc opaque en
  haut à gauche (le bloc paramètres conserve son emplacement) ; le gobelet est
  maintenant centré par le cadrage auto → plus de recouvrement.
- U5/B10 : libellé corrigé en « A4, 300 DPI » (`CONFIG.jpg.dpi = 300`, le rendu
  3508×2480 est bien du 300 DPI A4 paysage) ; l'annotation « Échelle 1:1 » est
  remplacée par « Échelle graphique » (la barre 60 mm reste indicative).
- **Fond d'export JPG** : le renderer passe en `preserveDrawingBuffer: true`,
  couleur de fond blanche opaque pendant la capture (l'export produisait un JPEG
  à fond noir/transparent) puis restauration.
- B7 : `DEFAULTS` devient la **source unique** ; `state` est construit depuis
  `DEFAULTS` et `generateParamSection` lit les valeurs dans `state`
  (`paramDefinitions` ne porte plus que les métadonnées d'UI).
- U1 : **persistance** ajoutée — sauvegarde automatique `localStorage`
  (`gobelet-params-v1`, 300 ms après la dernière saisie), boutons
  « Réinitialiser », « Exporter JSON », « Importer JSON », valeurs rechargées à
  l'init (état visualisé inclus).
- U4 : bouton « Réinitialiser » (vide le storage puis recharge).
- U2 : lien ajouté depuis **`services.html`** (carte « Argile ») vers
  `gobelet/index.html`.

**Validation effectuée** (Playwright, Chromium headless) :
- Aucune erreur console ni pageerror sur chargement, changement d'onglet, d'état,
  d'anneaux, de paramètres, import JSON (valide et invalide), exports JPG/STL.
- Persistance vérifiée : `H=100` → rechargement → `H=100` ; reset → valeur par
  défaut et storage vidé ; import JSON → `H=110` appliqué et volumes recalculés.
- Volumes cuit (défauts) : contenu **164 ml** (≈ tronc de cône 163 ml + courbure),
  paroi **78 cm³**, poids **195 g** (× 2,5 g/cm³).
- Le rendu de pixels WebGL n'a pas pu être vérifié dans cet environnement
  (contexte WebGL perdu par le driver headless, constat identique sur la version
  d'origine) ; les corrections de rendu sont validées par construction.

> Réponses au questionnaire §4 : 1. Voies B **puis** A. 2. Oui (persistance
> localStorage + JSON, pas de partage par URL). 3. Lien ajouté (Services).
> 4. Exports conservés, options mortes supprimées. 5. Annotation « 1:1 » supprimée
> (pas de calibrage orthographique, jugé hors périmètre).

