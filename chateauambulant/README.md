# Château Ambulant – Foyer de Calcifère

Site grimoire du **Foyer de Calcifère** : documentation littéraire d'un système multi-agents présentée sous la forme d'un grimoire médiéval (parchemin, dorure, serments).

## 🚀 Présentation

Le Château Ambulant documente l'architecture, la sécurité et la mémoire du système multi-agents du Foyer, à travers un thème magique :
- **Architecture** : diagrammes Mermaid et tableaux des agents & ports
- **Sécurité** : grimoire des protections (SSRF, cercles d'influence, serments)
- **Poésie technique** : poèmes des gardiens du Château
- **Mémoire** : timeline, décisions architecturales, leçons et erreurs

## 🏰 Architecture documentée

| Composant | Port | Rôle | Modèle/Protocole |
|---|---|---|---|
| Sen | 8766 (WS) | Gardienne conversationnelle | `mistral-medium-2508` |
| Calcifère | 8901 | Orchestrateur | `nvidia-nemotron-ultra` |
| Sophie | 8902 | Stratège | `llama-3.3-70b` |
| Marco | 8903 | Créatif | `glm-4.7-flash` |
| Hinn | 8904 | Système | `gpt-oss-120b` |
| MCP Fédération | 5000 | Gateway outils système | TCP/JSON-RPC |
| LiteLLM | 4000 | Proxy modèles | API compatible |

Flux : `Utilisateur → Sen (8766) → Calcifère (8901) → [Sophie | Marco | Hinn] → MCP (5000)`

## 📁 Structure des Fichiers

```
chateauambulant/
├── index.html               # Accueil et navigation
├── architecture.html        # Architecture multi-agents + tableau des ports
├── securite.html            # Grimoire de sécurité (SSRF, audits, serments)
├── poesie.html              # Poésie technique des gardiens
├── memoire.html             # Mémoire du Foyer (timeline, décisions, leçons)
├── script.js                # Navigation partagée
├── styles.css               # Thème grimoire (parchemin/or)
└── README.md                # Documentation
```

## 🛠️ Technologies

- **HTML5** – Pages sémantiques
- **CSS3** – Thème grimoire (fontes UnifrakturMaguntia + Cinzel, palette parchemin/or)
- **JavaScript Vanilla** – Mode nuit persistant (localStorage), date dynamique
- **Mermaid.js** – Diagrammes flowchart interactifs (CDN jsdelivr)

## 🌐 Déploiement

Site déployé sur GitHub Pages à l'adresse : `https://axxam.net/chateauambulant/`

### Configuration GitHub Pages
1. Repository : `Hauuru/Axxam`
2. Branch : `main`
3. Folder : `/chateauambulant`
4. Custom domain : `axxam.net/chateauambulant`

## 🔧 Personnalisation

- **Thème** : modifiez `styles.css` (variables `--couleur-parchemin`, `--couleur-or`, etc.)
- **Mode nuit** : bouton 🌙 dans le header, préférence stockée dans `localStorage`
- **Diagrammes** : éditez les blocs `mermaid` dans `architecture.html` et `securite.html`
- **Contenu** : chaque page est un fichier HTML autonome relié via `index.html`

## 🔐 Sécurité (documentée)

Le grimoire de sécurité (`securite.html`) détaille :
- **SSRF whitelist** : ports autorisés `127.0.0.1:8901-8904` et `localhost:4000` (config.json)
- **Runes de permission** : accès différenciés par agent (Sen : workspace, Hinn : logs en lecture, Sophie : isolation réseau)
- **Logs d'audit** : `~/logs/mcp_audit.log` et `~/logs/hinn.log`
- **Rotation lunaire** : renouvellement des clés tous les 28 jours (`litellm update_key`, chiffrement gpg)

## 🤝 Contribuer

1. Fork le projet
2. Créez une branche (`git checkout -b feature/amélioration`)
3. Committez vos changements
4. Poussez vers la branche
5. Créez un Pull Request

---

**Dernière mise à jour** : 4 août 2026
**Auteur** : Hauuru (Foyer de Calcifère)
