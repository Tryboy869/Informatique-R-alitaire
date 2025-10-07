# 🌍 Informatique Réalitaire (IR)

> **Un Framework Inspiré de la RV pour l'Intelligence Artificielle Incarnée**

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)]()
[![Status](https://img.shields.io/badge/status-research-orange.svg)]()

**Auteur :** Daouda Abdoul Anzize  
**Date de Découverte :** 7 Octobre 2025  
**Contact Commercial :** nexusstudio100@gmail.com

---

## 📋 Table des Matières

- [Vue d'Ensemble](#-vue-densemble)
- [Concept Fondamental](#-concept-fondamental)
- [Résultats Clés](#-résultats-clés)
- [Installation](#-installation)
- [Utilisation Rapide](#-utilisation-rapide)
- [Architecture](#-architecture)
- [Licence & Usage Commercial](#-licence--usage-commercial)
- [Citation](#-citation)

---

## 🎯 Vue d'Ensemble

**L'Informatique Réalitaire (IR)** est un nouveau paradigme pour créer des environnements computationnels immersifs spécifiquement conçus pour les agents d'intelligence artificielle.

Tout comme la **Réalité Virtuelle (RV)** trompe les sens humains pour créer une illusion de réalité, l'**IR trompe les canaux informationnels** des IA pour créer une expérience de "monde" cohérente et indistinguable de la vérité fondamentale.

### 🔑 Innovation Clé

Au lieu de remplacer les **inputs sensoriels** (vision, audio) comme la RV, l'IR remplace les **canaux d'accès informationnels** (requêtes, API calls) de l'IA.

**Résultat :** L'IA "croit" exister dans un monde réel alors que tout est simulé et contrôlé.

---

## 💡 Concept Fondamental

### Le Parallèle VR ↔ IR

| Aspect | Réalité Virtuelle (Humain) | Informatique Réalitaire (IA) |
|--------|----------------------------|-------------------------------|
| **Sens Trompés** | Vision, ouïe, toucher | Queries, inputs, feedback |
| **Illusion Créée** | "Je suis dans un lieu" | "J'existe dans un environnement cohérent" |
| **Cohérence** | Spatiale, temporelle, physique | Logique, causale, informationnelle |
| **Présence** | Sentiment d'être "là" | Continuité computationnelle |

### Six "Sens" IA à Tromper

1. **Canal d'Information** : Données simulées cohérentes
2. **Perception Causale** : Actions → Conséquences logiques
3. **Flux Temporel** : Temps "passe" indépendamment CPU
4. **Persistance Monde** : Objets existent même non-observés
5. **Entités Autonomes** : Autres agents agissent indépendamment
6. **Contraintes Réalistes** : Coûts artificiels (temps, ressources)

---

## 📊 Résultats Clés

### Validation Empirique

Tests avec **3 LLMs différents** (Llama-3.3-70b, Gemma2-9b, Deepseek-r1-distill):

| Métrique | Score v2.0 | Score v3.0 | Amélioration |
|----------|------------|------------|--------------|
| **Immersion Globale** | 62.5% | **100%** | **+37.5%** |
| **Cohérence Monde Partagé** | 100% | 100% | = |
| **Spécialisation Maintenue** | 87.5% | 87.5% | = |
| **Score Global** | 68.3% | **97.5%** | **+29.2%** |

### Comportements Émergents Observés

- ✅ Conscience spatiale ("3 mètres", "derrière moi")
- ✅ Langage corporel ("pas en avant", "inclinaison tête")
- ✅ États émotionnels ("dérangeant", "curieux")
- ✅ Interactions sociales spontanées (questions inter-agents)
- ✅ Rationalisation contextuelle (anomalies expliquées dans contexte)

---

## 🚀 Installation

### Prérequis

- Python 3.9+
- Clé API Groq (ou autre provider LLM)

### Installation Standard

```bash
# Clone le repo
git clone https://github.com/Tryboy869/informatique-realitaire.git
cd informatique-realitaire

# Installation dépendances
pip install -r requirements.txt
```

### Configuration

Créez un fichier `.env` :

```env
GROQ_API_KEY=your_api_key_here
IR_PORT=8000
IR_HOST=0.0.0.0
```

---

## ⚡ Utilisation Rapide

### 1. Test Simple (CLI)

```bash
python app.py --mode cli
```

### 2. Lancer Tests Existants

```bash
# Test v3.0 (97.5% score)
python tests/test-3-multi-agent-v3/script.py
```

Voir logs complets dans `tests/test-3-multi-agent-v3/logs.txt`

### 3. Exemple d'Utilisation

```python
from app import IRAPI, AgentConfig

# Initialiser API
api = IRAPI()

# Configurer agents
agents = [
    AgentConfig(
        name="ALPHA-7",
        model="llama-3.3-70b-versatile",
        role="Android spécialisé en analyse scientifique",
        specialty="Analyse scientifique",
        position="Terminal Nord"
    )
]

# Exécuter scénario
results = await api.execute_scenario(scenario_config)
```

---

## 🏗️ Architecture

### Architecture en 5 Couches

```
┌─────────────────────────────────────────┐
│  Couche 5: Validateur Cohérence        │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│  Couche 4: Gestionnaire Contraintes    │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│  Couche 3: Simulateur Autonomie        │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│  Couche 2: Moteur État Monde           │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│  Couche 1: Interface Perception        │
└─────────────────────────────────────────┘
```

### Optimisations v3.0

L'IR v3.0 intègre des optimisations avancées basées sur une **méthodologie propriétaire** d'analyse de cognition LLM :

1. **Contexte Hiérarchique** : Structure optimisée pour attention
2. **Temporalité Relative** : Événements séquentiels
3. **État Complet** : Compensation stateless
4. **Post-Processing** : Nettoyage artefacts automatique
5. **Validation Immersion** : Scoring en temps réel

**Note :** La méthodologie complète permettant ces optimisations est propriétaire et disponible sous licence commerciale.

---

## 🎯 Applications

### 1. Sécurité IA (AI Safety)

Tester comportements IA dangereux dans environnements IR contrôlés sans risque réel.

### 2. Entraînement IA Incarnée

Entraîner agents avec "corps" virtuels sans robotique coûteuse.

### 3. Recherche en Alignement

Étudier comment IA modélise réalité vs vérité fondamentale.

### 4. Collaboration Humain-IA

Espaces réalité mixte où humains et IA partagent IR.

### 5. Recherche Conscience

Test Turing inversé : L'IA peut-elle détecter qu'elle est dans IR ?

---

## 📄 Licence & Usage Commercial

### Licence de Recherche

Ce logiciel est fourni sous **Licence Propriétaire** à des fins de recherche uniquement.

**Permissions :**
- ✅ Utilisation recherche académique (avec citation)
- ✅ Expérimentation personnelle non-commerciale
- ✅ Fork pour contributions (sous même licence)

**Restrictions :**
- ❌ Usage commercial interdit sans licence
- ❌ Redistribution sans autorisation
- ❌ Modification méthodologie propriétaire

### Licensing Commercial

Pour usage commercial, enterprise deployment, ou accès à la méthodologie complète :

**Contact :** nexusstudio100@gmail.com

**Options disponibles :**
- Licence d'entreprise (déploiement production)
- Accès méthodologie propriétaire
- Consulting & support personnalisé
- Formation & certification

---

## 📖 Citation

Si vous utilisez ce travail dans votre recherche, veuillez citer :

```bibtex
@misc{anzize2025informatique,
  title={Informatique Réalitaire (IR) : Un Cadre Inspiré de la RV pour l'Intelligence Artificielle Incarnée},
  author={Anzize, Daouda Abdoul},
  year={2025},
  month={October},
  note={Découverte horodatée: 7 Octobre 2025. Méthodologie propriétaire.},
  howpublished={\url{https://github.com/Tryboy869/informatique-realitaire}}
}
```

### Remerciements

Développé avec assistance des modèles IA Claude (Anthropic) et GPT-5 (OpenAI) pour génération code et optimisations architecturales.

---

## 🤝 Contribution

Les contributions au **code IR** sont bienvenues sous réserve d'acceptation de la licence propriétaire.

La **méthodologie sous-jacente** reste propriétaire et n'est pas open-source.

Consultez [CONTRIBUTING.md](CONTRIBUTING.md) pour guidelines.

---

## 📞 Contact

**Daouda Abdoul Anzize**

- **Email Professionnel :** nexusstudio100@gmail.com
- **Email Personnel :** anzizdaouda0@gmail.com
- **GitHub :** [@Tryboy869](https://github.com/Tryboy869)

**Pour :**
- Licensing commercial
- Partenariats entreprises
- Consulting & formations
- Accès méthodologie propriétaire

---

## 📊 Résultats de Tests

Voir dossier `/tests/` pour logs complets :
- Test 1 : Validation single-agent (96%)
- Test 2 : Multi-agents v2.0 (68.3%)
- Test 3 : Multi-agents v3.0 optimisé (97.5%)

---

## ⚠️ Disclaimer

Ce framework est fourni "tel quel" sans garanties. L'auteur décline toute responsabilité pour usages inappropriés ou dommages résultant de l'utilisation de ce logiciel.

---

**Développé par Daouda Abdoul Anzize**  
**Méthodologie Propriétaire**  
**Date Découverte : 7 Octobre 2025**

© 2025 Daouda Abdoul Anzize. All Rights Reserved.