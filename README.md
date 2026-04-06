# 🌱 Le Potager - Workspace Agent Gestionnaire

## ✅ Configuration terminée !

Le workspace "le potager" est maintenant opérationnel pour l'Agent Gestionnaire.

## 📁 Structure

```
le-potager/
├── site/              # Dossier vide - Prêt pour l'import du site
│   └── (à remplir)
├── documentation/     # Documentation et analyses
│   ├── analyse-etape-2.md
│   ├── analyse-etape-3.md
│   ├── PLAN-OPTIMISATION.md
│   ├── README.md
│   ├── RESUME-GLOBAL.md
│   ├── optimize-images.sh
│   └── vesemt-full/
├── .git/              # Dépôt git local
└── README.md          # Ce fichier
```

## 🔐 Sécurité

L'Agent Gestionnaire est **limité à cet espace** :

- ✅ Peut modifier les fichiers dans `site/`
- ✅ Peut consulter la documentation dans `documentation/`
- ✅ Peut faire des git push vers Hauuru/Axxam
- ✅ Peut envoyer des notifications Discord
- ❌ **Ne peut pas** accéder aux fichiers en dehors de `le-potager/`

## 🚀 Utilisation

### Via l'Agent Principal (moi)

Dites-moi simplement ce que vous voulez faire :
- "Importe le site"
- "Modifie la page d'accueil"
- "Ajoute un article"
- "Push sur git"
- "Envoie sur Discord"

### Directement (scripts)

```bash
# Vérifier le statut
./agents/gestionnaire/handler.sh status

# Lire un fichier
./agents/gestionnaire/handler.sh read /home/hauuru/.openclaw/workspace-marco/le-potager/documentation/README.md

# Écrire un fichier
./agents/gestionnaire/handler.sh write /home/hauuru/.openclaw/workspace-marco/le-potager/site/test.html "<h1>Test</h1>"

# Git push
./agents/gestionnaire/handler.sh git_push /home/hauuru/.openclaw/workspace-marco/le-potager/site/test.html "<h1>Test</h1>" "Test commit"
```

## 📦 Configuration

- **Dépôt Git** : Hauuru/Axxam
- **Bot Discord** : Marco
- **Serveur** : Le Jardin du Chateau
- **Workspace** : `/home/hauuru/.openclaw/workspace-marco/le-potager`
- **Agent** : Marco (workspace principal)

## 🎯 Actions disponibles

| Action | Description | Exemple |
|--------|-------------|---------|
| `status` | Afficher le statut du workspace | `handler.sh status` |
| `read` | Lire un fichier | `handler.sh read <fichier>` |
| `write` | Écrire dans un fichier | `handler.sh write <fichier> <contenu>` |
| `edit` | Éditer un fichier | `handler.sh edit <fichier> <ancien> <nouveau>` |
| `git_push` | Git push | `handler.sh git_push <fichier> <contenu> <message>` |
| `discord_notify` | Notification Discord | `handler.sh discord_notify <message> <channel_id>` |

## 📝 Prochaine étape

Le dossier `site/` est vide et prêt à recevoir l'import du site web.

---
*Créé le 5 avril 2026*
