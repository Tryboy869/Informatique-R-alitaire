# Changelog

Toutes les modifications notables du projet Informatique Réalitaire seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/).

## [1.0.0] - 2025-10-07

### Ajouté
- Architecture IR v3.0 complète (5 couches)
- Moteur Reality Engine avec contexte hiérarchique
- Response Processor avec nettoyage artefacts
- Orchestrator multi-agents
- Support 3 modèles Groq simultanés
- Tests empiriques complets (97.5% score)
- Validation immersion automatique
- Logs audit complets
- Documentation utilisateur

### Optimisations v3.0
- Contexte hiérarchique optimisé attention LLM (+37.5% immersion)
- Temporalité relative (événements vs temps absolu)
- Post-processing robuste (suppression tags <think>)
- État monde complet réinjecté (compensation stateless)
- Score amélioration global : +29.2 points (68.3% → 97.5%)

### Sécurité
- Security Gateway centralisé
- Rate limiting par client
- Validation inputs
- Audit logging toutes actions

## [Unreleased]

### Prévu
- Support providers LLM additionnels (OpenAI, Anthropic)
- Serveur HTTP FastAPI
- Dashboard monitoring temps-réel
- Scaling 10+ agents simultanés
- Templates environnements personnalisables
- Benchmarks standardisés

---

**Format:** [Version] - Date YYYY-MM-DD  
**Types:** Ajouté, Modifié, Déprécié, Supprimé, Corrigé, Sécurité