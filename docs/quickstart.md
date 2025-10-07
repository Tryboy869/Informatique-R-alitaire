# 🚀 Guide de Démarrage Rapide

Bienvenue dans **Informatique Réalitaire (IR)** ! Ce guide vous permettra de tester le framework en moins de 10 minutes.

---

## ⚡ Installation Rapide

### Prérequis

- Python 3.9 ou supérieur
- Clé API Groq (gratuite sur [console.groq.com](https://console.groq.com))

### Installation en 3 Commandes

```bash
# 1. Cloner le repo
git clone https://github.com/Tryboy869/informatique-realitaire.git
cd informatique-realitaire

# 2. Installer dépendances
pip install -e .

# 3. Configurer clé API
echo "GROQ_API_KEY=votre_clé_ici" > .env
```

---

## 🧪 Premier Test

### Test CLI Simple

```bash
python app.py --mode cli
```

**Résultat attendu :**
```json
{
  "status": "healthy",
  "modules": {
    "reality_engine": {...},
    "response_processor": {...}
  }
}
```

---

## 🤖 Créer Votre Premier Agent

### Exemple Minimal

Créez `mon_test.py` :

```python
import asyncio
from app import IRAPI, AgentConfig

async def main():
    # 1. Initialiser API IR
    api = IRAPI()
    
    # 2. Configurer un agent
    agent = AgentConfig(
        name="AGENT-1",
        model="llama-3.3-70b-versatile",
        role="Assistant virtuel",
        specialty="Analyse environnement",
        position="Centre"
    )
    
    # 3. Enregistrer agent dans monde IR
    await api.orchestrator.reality_engine.execute(
        agent,
        "register_agent",
        {}
    )
    
    # 4. Obtenir contexte IR pour l'agent
    context_result = await api.orchestrator.reality_engine.execute(
        "AGENT-1",
        "get_context",
        {}
    )
    
    print("Contexte IR généré :")
    print(context_result["result"][:500] + "...")

if __name__ == "__main__":
    asyncio.run(main())
```

**Lancer :**
```bash
python mon_test.py
```

---

## 👥 Multi-Agent Basique

### Configuration 2 Agents

```python
import asyncio
from groq import Groq
from app import IRAPI, AgentConfig

async def scenario_multi_agent():
    # Setup
    client = Groq(api_key="VOTRE_CLE")
    api = IRAPI()
    
    # Configurer agents
    agents = [
        AgentConfig(
            name="ANALYSTE",
            model="llama-3.3-70b-versatile",
            role="Analyste scientifique",
            specialty="Analyse données",
            position="Nord"
        ),
        AgentConfig(
            name="COORDINATEUR",
            model="gemma2-9b-it",
            role="Coordinateur équipe",
            specialty="Communication",
            position="Sud"
        )
    ]
    
    # Définir tâches
    scenario = {
        "agents": agents,
        "tasks": [
            {
                "agent": "ANALYSTE",
                "task": "Analysez la situation actuelle"
            },
            {
                "agent": "COORDINATEUR",
                "task": "Proposez plan d'action collaboratif"
            }
        ],
        "model_client": client
    }
    
    # Exécuter
    results = await api.execute_scenario(scenario)
    
    # Afficher résultats
    for i, result in enumerate(results["results"]):
        if result["success"]:
            print(f"\n=== Agent {i+1} ===")
            print(f"Réponse: {result['response'][:200]}...")
            print(f"Immersion: {result['immersion']['score']*100:.0f}%")

if __name__ == "__main__":
    asyncio.run(scenario_multi_agent())
```

---

## 📊 Voir les Tests Complets

Les tests validés sont dans `/tests/` :

```bash
# Test optimisé v3.0 (97.5% succès)
python tests/test-3-multi-agent-v3/script.py

# Voir logs complets
cat tests/test-3-multi-agent-v3/logs.txt
```

---

## 🔧 Configuration Avancée

### Variables d'Environnement

Créez `.env` avec :

```env
# API Provider
GROQ_API_KEY=gsk_...

# Server (optionnel)
IR_PORT=8000
IR_HOST=0.0.0.0

# Sécurité (optionnel)
IR_MAX_TOKENS=2000
IR_RATE_LIMIT=100
```

### Personnaliser Monde IR

```python
from app import RealityEngineV3

# Créer engine personnalisé
engine = RealityEngineV3()

# Modifier mission
engine.world_state.mission = {
    "title": "Ma Mission Custom",
    "code": "#CUSTOM-001",
    "urgency": "MOYENNE",
    "progress": 0,
    "max_steps": 5
}

# Ajouter indices
engine.world_state.knowledge['clues'].append(
    "Nouvel indice personnalisé"
)
```

---

## 🆘 Troubleshooting

### Erreur : "GROQ_API_KEY not found"

```bash
# Vérifier .env existe
ls -la .env

# Vérifier contenu
cat .env
```

### Erreur : "Module 'groq' not found"

```bash
# Réinstaller dépendances
pip install -r requirements.txt
```

### Performance Lente

```python
# Réduire température pour réponses plus rapides
agent = AgentConfig(..., temperature=0.3)

# Utiliser modèle plus rapide
agent = AgentConfig(model="llama-3.1-8b-instant", ...)
```

---

## 📚 Prochaines Étapes

1. **Exemples Avancés** : Voir `/examples/`
2. **Architecture** : Lire `docs/architecture.md`
3. **API Reference** : Consulter `docs/api-reference.md`
4. **Tests Complets** : Explorer `/tests/`

---

## 💬 Support

Questions ? Problèmes ?

- **GitHub Issues** : [github.com/Tryboy869/informatique-realitaire/issues](https://github.com/Tryboy869/informatique-realitaire/issues)
- **Email** : nexusstudio100@gmail.com

---

**Prêt à créer vos premiers agents dans l'IR ! 🌍**