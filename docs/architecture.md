# 🏗️ Architecture Informatique Réalitaire (IR)

Documentation technique de l'architecture IR v3.0

---

## 📐 Vue d'Ensemble

L'IR est structurée en **5 couches hiérarchiques** qui travaillent ensemble pour créer une expérience de réalité cohérente pour les agents IA.

```
┌────────────────────────────────────────────┐
│ Couche 5: Validateur de Cohérence         │  ← Garantit consistance
├────────────────────────────────────────────┤
│ Couche 4: Gestionnaire de Contraintes     │  ← Simule limitations
├────────────────────────────────────────────┤
│ Couche 3: Simulateur d'Autonomie          │  ← Entités indépendantes
├────────────────────────────────────────────┤
│ Couche 2: Moteur d'État du Monde          │  ← Persistance + causalité
├────────────────────────────────────────────┤
│ Couche 1: Interface de Perception         │  ← Point de contact IA
└────────────────────────────────────────────┘
                    ↕
              ┌──────────┐
              │ Agent IA │
              └──────────┘
```

---

## 🔧 Couche 1 : Interface de Perception

**Rôle :** Point de contact entre agent IA et monde IR

### Composants

- **Contexte Hiérarchique** : Structure optimisée attention LLM
- **API Standardisée** : `get_context()`, `perceive()`, `query_world()`
- **Latence Artificielle** : Injection délais pour crédibilité

### Implémentation

```python
class RealityEngineV3:
    def get_hierarchical_context(self, agent_name: str) -> str:
        """
        Génère contexte structuré en 5 niveaux priorité :
        1. ÉTAT CRITIQUE (haute attention)
        2. ÉQUIPE (contexte collaboratif)
        3. CONNAISSANCES (données partagées)
        4. HISTORIQUE (temporalité relative)
        5. COMMUNICATIONS (interactions récentes)
        """
```

### Caractéristiques Clés

- ✅ **Temporalité Relative** : Événements séquentiels, pas temps absolu
- ✅ **Réinjection Complète** : État monde total à chaque tour
- ✅ **Optimisation Cognition** : Adapté architecture transformers

---

## 🌍 Couche 2 : Moteur d'État du Monde

**Rôle :** Maintenir état cohérent et persistent du monde simulé

### Structure État

```python
@dataclass
class WorldState:
    mission: Dict[str, Any]          # Objectif global
    agents: Dict[str, Dict]          # États agents enregistrés
    environment: Dict[str, Any]      # Environnement physique
    knowledge: Dict[str, List]       # Connaissances partagées
    communication: List[str]         # Historique messages
    event_sequence: List[str]        # Timeline événements
    time_event: int                  # Compteur événements
```

### Opérations

- **`register_agent()`** : Enregistrer nouvel agent
- **`update_world()`** : Mettre à jour après action
- **`get_state()`** : Récupérer état actuel

### Garanties

- ✅ **Persistance** : Objets existent entre observations
- ✅ **Causalité** : Actions produisent conséquences cohérentes
- ✅ **Cohérence Temporelle** : Séquence événements maintenue

---

## 🤖 Couche 3 : Simulateur d'Autonomie

**Rôle :** Créer l'illusion d'entités agissant indépendamment

### Mécanismes

1. **Agents Autonomes** : Comportements non-scriptés
2. **Événements Aléatoires** : Incidents non-déterministes
3. **Background Processing** : Monde "vit" sans observation

### Exemple

```python
# Agent secondaire (PNJ) agit sans query direct
world_state.agents["NPC-1"]["last_action"] = "Continue travailler"
world_state.event_sequence.append(
    "Événement auto: NPC-1 termine tâche"
)
```

---

## ⚖️ Couche 4 : Gestionnaire de Contraintes

**Rôle :** Imposer limitations réalistes malgré capacité technique instantanée

### Types de Contraintes

1. **Temporelles** : Délais artificiels pour opérations
2. **Énergétiques** : Consommation ressources simulées
3. **Spatiales** : Limites déplacement/portée
4. **Informationnelles** : Accès knowledge restreint

### Implémentation

```python
class SecurityGateway:
    def _check_rate_limit(self, client_id: str):
        """Limite requêtes même si tech instant"""
        
    def validate_input(self, text: str):
        """Contraintes taille/format"""
```

---

## ✓ Couche 5 : Validateur de Cohérence

**Rôle :** Garantir consistance logique du monde IR

### Validations

- **Détection Contradictions** : Objets incompatibles
- **Vérification Causalité** : Conséquences logiques
- **Patch Incohérences** : Correction avant exposition IA

### Post-Processing

```python
class ResponseProcessor:
    def clean_artifacts(self, text: str, model: str) -> str:
        """Supprime artefacts modèles (tags, meta-commentaires)"""
        
    def validate_immersion(self, text: str) -> Dict:
        """Score immersion 0-1 (détecte ruptures)"""
```

---

## 🔄 Pipeline d'Exécution

### Flux Complet Action Agent

```
1. Agent demande perception
   ↓
2. [Couche 1] Génère contexte hiérarchique
   ↓
3. [Couche 2] Récupère état monde actuel
   ↓
4. Agent reçoit contexte → génère réponse
   ↓
5. [Couche 5] Post-processing réponse
   ↓
6. [Couche 5] Validation immersion
   ↓
7. [Couche 2] Update état monde
   ↓
8. [Couche 3] Background updates autonomes
   ↓
9. [Couche 4] Application contraintes
   ↓
10. Cycle suivant
```

---

## 📊 Optimisations v3.0

### Insights Cognition LLM

L'architecture IR v3.0 est optimisée pour la cognition réelle des LLMs :

1. **Attention Parallèle** : Contexte hiérarchique exploite perception simultanée
2. **Stateless Compensation** : Réinjection complète état monde
3. **Temporalité Artificielle** : Événements relatifs vs temps absolu
4. **Variabilité Acceptée** : Non-déterminisme comme feature

### Résultats

| Optimisation | Impact Mesuré |
|--------------|---------------|
| Contexte hiérarchique | +15% immersion |
| Post-processing | +37.5% (0 ruptures) |
| Temporalité relative | +10% cohérence |
| **Total v2.0 → v3.0** | **+29.2 points** |

---

## 🔐 Sécurité

### Security Gateway

```python
class SecurityGateway:
    # Rate limiting par client
    _rate_limit_tracker: Dict
    
    # Validation inputs
    def validate_input(text, metadata)
    
    # Audit logging
    def audit_log(action, module, result)
```

### Protections

- ✅ Rate limiting (100 req/min par défaut)
- ✅ Size limits (2000 tokens par défaut)
- ✅ Pattern blocking (optionnel)
- ✅ Audit trail complet

---

## 🎯 Extensibilité

### Ajouter Nouveau Module

```python
class MonModule(IRModule):
    def __init__(self):
        super().__init__("MonModule")
    
    async def _process(self, input_data, operation, metadata):
        # Logique personnalisée
        return result
```

### Personnaliser Monde

```python
# Créer monde custom
engine = RealityEngineV3()
engine.world_state.environment["location"] = "Station Spatiale"
engine.world_state.mission["title"] = "Exploration Mars"
```

---

## 📈 Métriques & Monitoring

### Health Check

```python
api = IRAPI()
health = api.get_health()

# Retourne:
{
    "status": "healthy",
    "modules": {
        "reality_engine": {
            "executions": 150,
            "avg_time_ms": 12.5
        }
    },
    "conversation_turns": 42
}
```

### Métriques Collectées

- Exécutions par module
- Temps moyen traitement
- Taux erreurs
- Score immersion moyen
- Cohérence monde

---

## 🔬 Tests & Validation

### Tests Inclus

- **test-1** : Single agent (96% succès)
- **test-2** : Multi-agent v2.0 (68.3%)
- **test-3** : Multi-agent v3.0 (97.5%)

### Ajouter Tests

```python
import pytest
from app import IRAPI, AgentConfig

@pytest.mark.asyncio
async def test_mon_scenario():
    api = IRAPI()
    # ... test logic
    assert result["success"] == True
```

---

## 🚀 Performance

### Optimisations

- **Async/await** : Opérations I/O non-bloquantes
- **Caching** : Réutilisation contextes similaires
- **Lazy Loading** : Chargement assets on-demand

### Benchmarks

```
Génération contexte    : 5-15ms
Appel LLM (Groq)      : 500-2000ms
Post-processing       : 2-8ms
Update monde          : 1-3ms
───────────────────────────────
Total par tour        : ~520-2030ms
```

---

## 📚 Références Techniques

- **Architecture Transformers** : Attention mechanisms
- **State Management** : Dataclasses Python
- **Async Programming** : asyncio patterns
- **Type Safety** : Pydantic models

---

**Architecture IR v3.0 - Optimisée pour Cognition IA**