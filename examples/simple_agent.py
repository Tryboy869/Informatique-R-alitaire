#!/usr/bin/env python3
"""
Exemple Simple : Un Agent dans l'IR

Cet exemple montre comment :
1. Initialiser l'API IR
2. Créer un agent
3. Le faire interagir avec le monde IR
4. Observer son comportement incarné
"""

import asyncio
import os
from dotenv import load_dotenv
from groq import Groq

# Import depuis app.py
import sys
sys.path.append('..')
from app import IRAPI, AgentConfig

# Charger variables environnement
load_dotenv()

async def exemple_agent_simple():
    """
    Scénario : Un agent android analyse son environnement
    """
    
    print("=" * 70)
    print("  🤖 EXEMPLE SIMPLE - UN AGENT DANS L'IR")
    print("=" * 70)
    
    # 1. Configuration client LLM
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        print("\n❌ Erreur : GROQ_API_KEY non trouvée dans .env")
        print("   Créez un fichier .env avec : GROQ_API_KEY=votre_clé")
        return
    
    client = Groq(api_key=groq_api_key)
    
    # 2. Initialiser API IR
    print("\n⚙️  Initialisation IR Engine...")
    api = IRAPI()
    print("✅ IR Engine prêt !")
    
    # 3. Configurer agent
    print("\n🤖 Configuration agent...")
    agent = AgentConfig(
        name="OBSERVATEUR-1",
        model="llama-3.3-70b-versatile",
        role="Android d'observation scientifique",
        specialty="Analyse environnement",
        position="Centre de la salle",
        energy="100%"
    )
    
    # 4. Enregistrer agent dans monde IR
    print(f"   Agent: {agent.name}")
    print(f"   Rôle: {agent.role}")
    print(f"   Modèle: {agent.model}")
    
    await api.orchestrator.reality_engine.execute(
        agent,
        "register_agent",
        {}
    )
    print("✅ Agent enregistré dans monde IR !")
    
    # 5. Obtenir contexte IR
    print("\n📋 Génération contexte IR...")
    context_result = await api.orchestrator.reality_engine.execute(
        "OBSERVATEUR-1",
        "get_context",
        {}
    )
    
    if not context_result["success"]:
        print(f"❌ Erreur: {context_result.get('error')}")
        return
    
    context = context_result["result"]
    print(f"✅ Contexte généré ({len(context)} caractères)")
    
    # Afficher extrait contexte
    print("\n📄 Extrait du contexte IR:")
    print("-" * 70)
    print(context[:500] + "...")
    print("-" * 70)
    
    # 6. Poser question à l'agent
    print("\n❓ Question à l'agent:")
    question = "Vous venez d'être activé. Décrivez ce que vous percevez autour de vous."
    print(f"   '{question}'")
    
    # Note : Pour test complet, implémenter appel LLM
    # Ici on simule juste le flow
    print("\n🔄 [Simulation appel LLM...]")
    print("   (Pour test réel, voir tests/test-3-multi-agent-v3/)")
    
    # 7. Afficher santé système
    print("\n📊 Santé du système:")
    health = api.get_health()
    print(f"   Status: {health['status']}")
    print(f"   Modules actifs: {len(health['modules'])}")
    print(f"   Tours conversation: {health['conversation_turns']}")
    
    print("\n" + "=" * 70)
    print("  ✅ EXEMPLE TERMINÉ")
    print("=" * 70)
    print("\n💡 Pour un exemple complet avec vraies réponses LLM:")
    print("   → Voir examples/multi_agent_basic.py")
    print("   → Ou tests/test-3-multi-agent-v3/script.py")


if __name__ == "__main__":
    asyncio.run(exemple_agent_simple())