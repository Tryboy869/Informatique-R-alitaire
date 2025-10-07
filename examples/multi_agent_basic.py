#!/usr/bin/env python3
"""
Exemple Multi-Agent : Collaboration de 2 Agents

Cet exemple montre :
1. Configuration de 2 agents avec spécialités différentes
2. Tâches collaboratives
3. Interactions dans monde IR partagé
4. Analyse résultats immersion
"""

import asyncio
import os
from dotenv import load_dotenv
from groq import Groq

import sys
sys.path.append('..')
from app import IRAPI, AgentConfig

load_dotenv()


async def exemple_multi_agent():
    """
    Scénario : 2 agents collaborent sur mission urgente
    """
    
    print("=" * 70)
    print("  🤖🤖 EXEMPLE MULTI-AGENT - COLLABORATION")
    print("=" * 70)
    
    # 1. Setup
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        print("\n❌ Erreur : GROQ_API_KEY manquante")
        return
    
    client = Groq(api_key=groq_api_key)
    api = IRAPI()
    
    print("\n✅ IR Engine initialisé")
    
    # 2. Configurer 2 agents complémentaires
    print("\n🤖 Configuration agents...")
    
    agents = [
        AgentConfig(
            name="ANALYSTE-ALPHA",
            model="llama-3.3-70b-versatile",
            role="Android analyste scientifique",
            specialty="Analyse technique et diagnostics",
            position="Terminal Nord"
        ),
        AgentConfig(
            name="COORDINATEUR-BETA",
            model="gemma2-9b-it",
            role="Android coordinateur d'équipe",
            specialty="Communication et stratégie",
            position="Terminal Sud"
        )
    ]
    
    for agent in agents:
        print(f"\n   Agent: {agent.name}")
        print(f"   Spécialité: {agent.specialty}")
        print(f"   Position: {agent.position}")
        
        await api.orchestrator.reality_engine.execute(
            agent,
            "register_agent",
            {}
        )
    
    print("\n✅ 2 agents enregistrés dans monde IR partagé")
    
    # 3. Définir tâches collaboratives
    print("\n📋 Définition tâches collaboratives...")
    
    tasks = [
        {
            "agent": "ANALYSTE-ALPHA",
            "task": "Analysez le code erreur #X7-THETA. Quelle est votre hypothèse technique ?"
        },
        {
            "agent": "COORDINATEUR-BETA",
            "task": "Observez votre collègue ANALYSTE-ALPHA. Comment coordonner efficacement cette mission urgente ?"
        }
    ]
    
    for i, task in enumerate(tasks, 1):
        print(f"\n   Tâche {i}: {task['agent']}")
        print(f"   → {task['task'][:60]}...")
    
    # 4. Vérifier état monde avant exécution
    print("\n🌍 État du monde IR:")
    world_state = api.orchestrator.reality_engine.world_state
    
    print(f"   Mission: {world_state.mission['title']}")
    print(f"   Code: {world_state.mission['code']}")
    print(f"   Agents actifs: {len(world_state.agents)}")
    print(f"   Événements: {len(world_state.event_sequence)}")
    
    # 5. Afficher exemple contexte pour un agent
    print("\n📄 Exemple contexte pour ANALYSTE-ALPHA:")
    print("-" * 70)
    
    context_result = await api.orchestrator.reality_engine.execute(
        "ANALYSTE-ALPHA",
        "get_context",
        {}
    )
    
    if context_result["success"]:
        context = context_result["result"]
        # Afficher première section (critique)
        lines = context.split('\n')
        for line in lines[:15]:
            print(line)
        print("   [...]")
    
    print("-" * 70)
    
    # 6. Note sur exécution complète
    print("\n💡 EXÉCUTION COMPLÈTE:")
    print("   Pour voir vraies interactions LLM, utilisez:")
    print("   → python tests/test-3-multi-agent-v3/script.py")
    print("\n   Ce script montre :")
    print("   ✓ Setup architecture IR")
    print("   ✓ Configuration multi-agents")
    print("   ✓ Génération contextes")
    print("   ✓ [Appels LLM nécessaires pour suite]")
    
    # 7. Santé système
    print("\n📊 Santé système:")
    health = api.get_health()
    
    for module_name, module_health in health['modules'].items():
        print(f"\n   {module_name}:")
        print(f"   - Exécutions: {module_health['metrics']['executions']}")
        print(f"   - Temps moyen: {module_health['avg_time_ms']:.2f}ms")
    
    print("\n" + "=" * 70)
    print("  ✅ EXEMPLE MULTI-AGENT TERMINÉ")
    print("=" * 70)
    
    print("\n🎯 PROCHAINES ÉTAPES:")
    print("   1. Implémenter appels LLM complets")
    print("   2. Observer interactions spontanées agents")
    print("   3. Mesurer scores immersion")
    print("   4. Analyser comportements émergents")
    
    print("\n📚 RESSOURCES:")
    print("   - Documentation: docs/architecture.md")
    print("   - Tests complets: tests/")
    print("   - API Reference: docs/api-reference.md")


if __name__ == "__main__":
    asyncio.run(exemple_multi_agent())