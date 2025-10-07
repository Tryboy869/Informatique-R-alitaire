# Guide de Contribution

Merci de votre intérêt pour contribuer à Informatique Réalitaire (IR) !

## ⚠️ Note Importante sur la Licence

Ce projet est sous **Licence Propriétaire**. En contribuant, vous acceptez que :
- Vos contributions soient sous la même licence propriétaire
- La méthodologie sous-jacente reste confidentielle
- L'usage commercial nécessite une licence séparée

## 🎯 Comment Contribuer

### Rapporter des Bugs

1. Vérifiez que le bug n'a pas déjà été rapporté dans [Issues](https://github.com/Tryboy869/informatique-realitaire/issues)
2. Ouvrez une nouvelle issue avec:
   - Description claire du problème
   - Étapes pour reproduire
   - Comportement attendu vs observé
   - Version Python et dépendances
   - Logs pertinents

### Proposer des Fonctionnalités

1. Ouvrez une issue "Feature Request"
2. Décrivez:
   - Cas d'usage
   - Bénéfice attendu
   - Implémentation proposée (optionnel)

### Soumettre des Pull Requests

1. Fork le repo
2. Créez une branche: `git checkout -b feature/ma-feature`
3. Committez: `git commit -m "feat: ajout ma feature"`
4. Push: `git push origin feature/ma-feature`
5. Ouvrez une Pull Request

## 📝 Standards de Code

### Style Python

- Suivre PEP 8
- Utiliser Black pour formatting: `black app.py`
- Utiliser Ruff pour linting: `ruff check app.py`
- Type hints recommandés

### Commits

Format: `type(scope): description`

Types:
- `feat`: Nouvelle fonctionnalité
- `fix`: Correction bug
- `docs`: Documentation
- `test`: Tests
- `refactor`: Refactoring
- `perf`: Performance

Exemple: `feat(orchestrator): add multi-agent scaling`

### Tests

- Tous nouveaux features doivent avoir tests
- Run tests: `pytest tests/`

## 🔒 Restrictions

**Ne PAS inclure dans contributions :**
- Détails sur la méthodologie propriétaire
- Tentatives de reverse engineering
- Contenu sous copyright tiers

## 🔬 Domaines de Contribution Acceptés

### Prioritaires

1. **Support LLM Providers**
   - OpenAI, Anthropic, Mistral, etc.
   - Standardisation interface

2. **Optimisations Performance**
   - Scaling agents
   - Réduction latence

3. **Documentation**
   - Exemples d'utilisation
   - Guides utilisateurs

### Refusés

- Modifications méthodologie propriétaire
- Extraction/documentation techniques confidentielles
- Usage commercial non-licencié

## 📞 Contact

Questions? Contactez:
- Email: nexusstudio100@gmail.com
- GitHub Issues: [@Tryboy869](https://github.com/Tryboy869)

## 📄 Licence

En contribuant, vous acceptez que votre code soit sous Licence Propriétaire.