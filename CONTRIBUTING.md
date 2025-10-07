# Guide de Contribution

Merci de votre intérêt pour contribuer à Informatique Réalitaire (IR) !

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
- Type hints obligatoires: `mypy app.py`

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
- Coverage minimum: 80%

## 🔬 Domaines de Contribution

### Prioritaires

1. **Support LLM Providers**
   - OpenAI, Anthropic, Mistral, etc.
   - Standardisation interface

2. **Server HTTP**
   - FastAPI implementation
   - WebSocket support temps-réel

3. **Monitoring & Analytics**
   - Dashboard visualisation
   - Métriques temps-réel

### Recherche

1. **Nouveaux Environnements RI**
   - Templates monde personnalisables
   - Générateurs procéduraux

2. **Benchmarks**
   - Suite tests standardisés
   - Comparaison providers LLM

3. **Extensions DECAP NEXUS**
   - Application autres paradigmes
   - Documentation méthodologie

## 📞 Contact

Questions? Contactez:
- Email: nexusstudio100@gmail.com
- GitHub Issues: [@Tryboy869](https://github.com/Tryboy869)

## 📄 Licence

En contribuant, vous acceptez que votre code soit sous licence MIT.