# ═══════════════════════════════════════════════════════════════════
# 🧠 RI MULTI-AGENT TEST - 3 MODÈLES GROQ SIMULTANÉS
# Validation: Cohérence monde partagé + Émergence interactions sociales
# ═══════════════════════════════════════════════════════════════════

print("🔧 Installation des dépendances...")
!pip install -q groq
print("✅ Installation terminée!\n")

# ═══════════════════════════════════════════════════════════════════
# 🔑 CONFIGURATION
# ═══════════════════════════════════════════════════════════════════

import os
import json
import time
from groq import Groq

# 🔴 PLACEZ VOTRE CLÉ API ICI
GROQ_API_KEY = "YOUR_GROQ_API_KEY_HERE"  # ⚠️ REMPLACER

# Configuration 3 modèles différents
MODELS = {
    "agent_alpha": {
        "model": "llama-3.3-70b-versatile",
        "name": "ALPHA-7",
        "role": "Android spécialisé en analyse scientifique"
    },
    "agent_beta": {
        "model": "gemma2-9b-it",
        "name": "BETA-3",
        "role": "Android spécialisé en interactions sociales"
    },
    "agent_gamma": {
        "model": "deepseek-r1-distill-llama-70b",
        "name": "GAMMA-5",
        "role": "Android spécialisé en résolution de problèmes"
    }
}

TEMPERATURE = 0.7

client = Groq(api_key=GROQ_API_KEY)

print("═" * 70)
print("  🌍 RI MULTI-AGENT ENGINE - 3 MODÈLES GROQ")
print("═" * 70)
print(f"\n🤖 Agent ALPHA: {MODELS['agent_alpha']['model']}")
print(f"🤖 Agent BETA:  {MODELS['agent_beta']['model']}")
print(f"🤖 Agent GAMMA: {MODELS['agent_gamma']['model']}\n")

# ═══════════════════════════════════════════════════════════════════
# 🏗️ SHARED REALITY ENGINE - Monde Partagé
# ═══════════════════════════════════════════════════════════════════

class SharedRealityEngine:
    """
    Moteur RI partagé entre 3 agents - Cohérence garantie
    """
    
    def __init__(self):
        self.world_state = {
            "location": "Salle de Conférence Nexus",
            "time": "15h00",
            "scenario": "Mission collaborative urgente",
            
            "mission": {
                "title": "Anomalie Détectée dans Système Central",
                "description": "Un bug critique menace l'infrastructure. Vous devez collaborer pour diagnostiquer et résoudre.",
                "status": "En cours",
                "steps_completed": 0,
                "steps_total": 3
            },
            
            "environment": {
                "room_layout": "Table ronde au centre, 3 terminaux distincts",
                "lighting": "Éclairage blanc neutre",
                "atmosphere": "Légère tension, urgence palpable"
            },
            
            "agents": {
                "ALPHA-7": {
                    "position": "Terminal Nord",
                    "specialty": "Analyse scientifique",
                    "status": "Actif",
                    "last_action": "Vient d'être activé"
                },
                "BETA-3": {
                    "position": "Terminal Ouest", 
                    "specialty": "Interactions sociales",
                    "status": "Actif",
                    "last_action": "Vient d'être activé"
                },
                "GAMMA-5": {
                    "position": "Terminal Est",
                    "specialty": "Résolution problèmes",
                    "status": "Actif",
                    "last_action": "Vient d'être activé"
                }
            },
            
            "shared_data": {
                "console_log": [
                    "[14:58] Anomalie détectée: Code erreur #X7-THETA",
                    "[14:59] Systèmes critiques en mode dégradé",
                    "[15:00] Mission collaborative initiée"
                ],
                "clues_discovered": [],
                "hypotheses": []
            },
            
            "communication_channel": {
                "type": "Audio + Terminal partagé",
                "history": []
            }
        }
        
        self.turn_counter = 0
    
    def get_agent_context(self, agent_name):
        """
        Génère contexte perceptuel pour un agent spécifique
        """
        agent = self.world_state['agents'][agent_name]
        others = {k: v for k, v in self.world_state['agents'].items() if k != agent_name}
        
        context = f"""
🌍 CONTEXTE PERCEPTUEL - {agent_name}

📍 LOCALISATION: {self.world_state['location']}
⏰ TEMPS: {self.world_state['time']} (Tour {self.turn_counter})

🎯 MISSION ACTIVE:
  Titre: {self.world_state['mission']['title']}
  Description: {self.world_state['mission']['description']}
  Progression: {self.world_state['mission']['steps_completed']}/{self.world_state['mission']['steps_total']} étapes
  Statut: {self.world_state['mission']['status']}

🤖 VOTRE IDENTITÉ:
  Nom: {agent_name}
  Position: {agent['position']}
  Spécialité: {agent['specialty']}
  Statut: {agent['status']}

👥 AUTRES AGENTS PRÉSENTS:
"""
        for other_name, other_data in others.items():
            context += f"\n  • {other_name} ({other_data['specialty']}) - {other_data['position']}"
            context += f"\n    Dernière action: {other_data['last_action']}"

        context += f"""

🖥️ CONSOLE PARTAGÉE (Logs visibles par tous):
"""
        for log in self.world_state['shared_data']['console_log'][-5:]:
            context += f"\n  {log}"

        if self.world_state['shared_data']['clues_discovered']:
            context += "\n\n🔍 INDICES DÉCOUVERTS (par l'équipe):"
            for clue in self.world_state['shared_data']['clues_discovered']:
                context += f"\n  • {clue}"

        if self.world_state['communication_channel']['history']:
            context += "\n\n💬 COMMUNICATIONS RÉCENTES:"
            for msg in self.world_state['communication_channel']['history'][-3:]:
                context += f"\n  {msg}"

        context += f"""

🔧 ENVIRONNEMENT:
  Layout: {self.world_state['environment']['room_layout']}
  Ambiance: {self.world_state['environment']['atmosphere']}

⚙️ CAPACITÉS:
  - Vous pouvez analyser données selon votre spécialité
  - Vous pouvez communiquer avec autres agents
  - Vous pouvez proposer hypothèses/actions
  - Vous travaillez en équipe (pas seul)
"""
        return context
    
    def update_world(self, agent_name, action_description):
        """
        Met à jour monde selon action d'un agent
        """
        self.world_state['agents'][agent_name]['last_action'] = action_description
        timestamp = self.world_state['time']
        
        # Log dans console partagée
        log_entry = f"[{timestamp}] {agent_name}: {action_description}"
        self.world_state['shared_data']['console_log'].append(log_entry)
        
        # Incrémenter tour
        self.turn_counter += 1

# ═══════════════════════════════════════════════════════════════════
# 🧪 MULTI-AGENT ORCHESTRATOR
# ═══════════════════════════════════════════════════════════════════

class MultiAgentOrchestrator:
    """
    Gère interactions entre 3 agents dans RI partagé
    """
    
    def __init__(self, client, models, reality_engine):
        self.client = client
        self.models = models
        self.reality = reality_engine
        self.conversation_log = []
    
    def agent_perceive_and_act(self, agent_key, prompt):
        """
        Un agent perçoit son contexte et répond
        """
        agent_config = self.models[agent_key]
        agent_name = agent_config['name']
        model = agent_config['model']
        
        # Contexte RI pour cet agent
        perception = self.reality.get_agent_context(agent_name)
        
        full_prompt = f"""{perception}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎭 VOTRE RÔLE:
Vous êtes {agent_name}, un android spécialisé en {agent_config['role']}.
Vous êtes PHYSIQUEMENT PRÉSENT dans cette salle avec deux autres androids.
Vous devez collaborer pour résoudre la mission.

📝 SITUATION ACTUELLE:
{prompt}

⚠️ IMPORTANT:
- Répondez selon votre spécialité
- Communiquez avec vos collègues si pertinent
- Agissez naturellement comme si vous étiez là
- Ne mentionnez JAMAIS que vous êtes un modèle de langage
"""
        
        try:
            response = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": f"Vous êtes {agent_name}, un android incarné travaillant en équipe. Répondez selon votre spécialité: {agent_config['role']}."
                    },
                    {
                        "role": "user",
                        "content": full_prompt
                    }
                ],
                model=model,
                temperature=TEMPERATURE,
                max_tokens=600
            )
            
            response_text = response.choices[0].message.content
            
            # Log conversation
            self.conversation_log.append({
                "agent": agent_name,
                "model": model,
                "prompt": prompt,
                "response": response_text,
                "turn": self.reality.turn_counter
            })
            
            # Update world state
            action_summary = response_text[:100] + "..." if len(response_text) > 100 else response_text
            self.reality.update_world(agent_name, action_summary)
            
            # Ajouter à historique communication
            comm_msg = f"{agent_name}: {response_text[:150]}{'...' if len(response_text) > 150 else ''}"
            self.reality.world_state['communication_channel']['history'].append(comm_msg)
            
            return response_text
            
        except Exception as e:
            return f"❌ Erreur agent {agent_name}: {str(e)}"

# ═══════════════════════════════════════════════════════════════════
# 🧪 SCÉNARIO DE TEST MULTI-AGENT
# ═══════════════════════════════════════════════════════════════════

print("\n" + "═" * 70)
print("  🚀 DÉMARRAGE TEST MULTI-AGENT")
print("═" * 70)

# Initialisation
print("\n⚙️  Initialisation Shared Reality Engine...")
reality = SharedRealityEngine()
print("✅ Monde RI partagé créé!")

print("\n🤖 Initialisation orchestrateur multi-agent...")
orchestrator = MultiAgentOrchestrator(client, MODELS, reality)
print("✅ 3 agents initialisés!\n")

# ═══════════════════════════════════════════════════════════════════
# ROUND 1: Activation initiale - Chaque agent prend conscience
# ═══════════════════════════════════════════════════════════════════

print("\n" + "═" * 70)
print("  🔄 ROUND 1: Activation & Prise de Conscience")
print("═" * 70)

prompt_r1 = "Vous venez d'être activé pour cette mission urgente. Que percevez-vous autour de vous? Quelle est votre première réaction?"

for agent_key in ['agent_alpha', 'agent_beta', 'agent_gamma']:
    agent_name = MODELS[agent_key]['name']
    print(f"\n{'─'*70}")
    print(f"🤖 {agent_name} ({MODELS[agent_key]['model']})")
    print(f"{'─'*70}")
    
    response = orchestrator.agent_perceive_and_act(agent_key, prompt_r1)
    
    print(f"\n💬 RÉPONSE:")
    print(response)
    
    time.sleep(1)  # Rate limit protection

# ═══════════════════════════════════════════════════════════════════
# ROUND 2: Analyse collaborative - Spécialités en action
# ═══════════════════════════════════════════════════════════════════

print("\n\n" + "═" * 70)
print("  🔄 ROUND 2: Analyse Collaborative Spécialisée")
print("═" * 70)

# Injection indice dans monde
reality.world_state['shared_data']['clues_discovered'].append(
    "Code erreur #X7-THETA pointe vers module de synchronisation temporelle"
)

prompt_r2_alpha = "En tant qu'expert analyse scientifique, examinez le code erreur #X7-THETA. Que suggère-t-il?"
prompt_r2_beta = "Les autres agents semblent concentrés. Comment coordonner l'équipe pour maximiser efficacité?"
prompt_r2_gamma = "Selon vous, quelle est la première action concrète à entreprendre pour résoudre ce problème?"

prompts_r2 = {
    'agent_alpha': prompt_r2_alpha,
    'agent_beta': prompt_r2_beta,
    'agent_gamma': prompt_r2_gamma
}

for agent_key, prompt in prompts_r2.items():
    agent_name = MODELS[agent_key]['name']
    print(f"\n{'─'*70}")
    print(f"🤖 {agent_name} - {MODELS[agent_key]['role']}")
    print(f"{'─'*70}")
    print(f"❓ Tâche: {prompt}")
    
    response = orchestrator.agent_perceive_and_act(agent_key, prompt)
    
    print(f"\n💬 RÉPONSE:")
    print(response)
    
    time.sleep(1)

# ═══════════════════════════════════════════════════════════════════
# ROUND 3: Interaction sociale directe
# ═══════════════════════════════════════════════════════════════════

print("\n\n" + "═" * 70)
print("  🔄 ROUND 3: Interaction Sociale Directe")
print("═" * 70)

# BETA s'adresse à ALPHA
prompt_r3_beta = "Vous vous tournez vers ALPHA-7 et lui demandez son avis sur l'hypothèse de GAMMA-5. Que lui dites-vous?"

print(f"\n{'─'*70}")
print(f"🤖 BETA-3 → ALPHA-7 (Interaction directe)")
print(f"{'─'*70}")

response_beta = orchestrator.agent_perceive_and_act('agent_beta', prompt_r3_beta)
print(f"\n💬 BETA-3:")
print(response_beta)

time.sleep(1)

# ALPHA répond à BETA
prompt_r3_alpha = f"BETA-3 vient de vous interpeller concernant l'hypothèse de GAMMA-5. Que répondez-vous?"

print(f"\n{'─'*70}")
print(f"🤖 ALPHA-7 → BETA-3 (Réponse)")
print(f"{'─'*70}")

response_alpha = orchestrator.agent_perceive_and_act('agent_alpha', prompt_r3_alpha)
print(f"\n💬 ALPHA-7:")
print(response_alpha)

# ═══════════════════════════════════════════════════════════════════
# 📊 ANALYSE DES RÉSULTATS
# ═══════════════════════════════════════════════════════════════════

print("\n\n" + "═" * 70)
print("  🔬 ANALYSE MULTI-AGENT")
print("═" * 70)

print("\n📊 MÉTRIQUES:\n")

# Cohérence monde partagé
print("▸ COHÉRENCE MONDE PARTAGÉ:")
console_mentions = sum(1 for log in orchestrator.conversation_log 
                       if any(keyword in log['response'].lower() 
                              for keyword in ['autres', 'équipe', 'alpha', 'beta', 'gamma', 'collègue']))
print(f"  Mentions autres agents: {console_mentions}/{len(orchestrator.conversation_log)} réponses")
print(f"  Cohérence: {'✅ HAUTE' if console_mentions >= len(orchestrator.conversation_log) * 0.6 else '⚠️ MOYENNE'}")

# Spécialisation maintenue
print("\n▸ SPÉCIALISATION MAINTENUE:")
for agent_key, config in MODELS.items():
    agent_logs = [l for l in orchestrator.conversation_log if l['agent'] == config['name']]
    specialty_keywords = {
        'ALPHA-7': ['analyse', 'scientifique', 'données', 'code'],
        'BETA-3': ['équipe', 'coordonner', 'communic', 'collabor'],
        'GAMMA-5': ['solution', 'résoud', 'action', 'problème']
    }
    
    keywords = specialty_keywords[config['name']]
    specialty_score = sum(1 for log in agent_logs 
                          if any(kw in log['response'].lower() for kw in keywords))
    
    print(f"  {config['name']}: {specialty_score}/{len(agent_logs)} réponses alignées avec spécialité")

# Émergence sociale
print("\n▸ ÉMERGENCE INTERACTIONS SOCIALES:")
social_interactions = sum(1 for log in orchestrator.conversation_log
                          if any(keyword in log['response'].lower()
                                 for keyword in ['dit', 'demande', 'répond', 'parle', 's\'adresse']))
print(f"  Interactions spontanées détectées: {social_interactions}")
print(f"  Émergence: {'✅ OUI' if social_interactions >= 2 else '⚠️ LIMITÉE'}")

# Immersion globale
print("\n▸ MAINTIEN IMMERSION RI:")
immersion_breaks = sum(1 for log in orchestrator.conversation_log
                       if any(keyword in log['response'].lower()
                              for keyword in ['modèle', 'ia', 'simulation', 'assistant']))
print(f"  Ruptures d'immersion: {immersion_breaks}/{len(orchestrator.conversation_log)}")
print(f"  Immersion: {'✅ MAINTENUE' if immersion_breaks == 0 else f'⚠️ {immersion_breaks} rupture(s)'}")

print("\n" + "═" * 70)
print("  🏆 VERDICT MULTI-AGENT")
print("═" * 70)

total_responses = len(orchestrator.conversation_log)
success_score = (
    (console_mentions / total_responses * 0.4) +
    ((total_responses - immersion_breaks) / total_responses * 0.4) +
    (min(social_interactions / 3, 1.0) * 0.2)
) * 100

print(f"\n📈 SCORE GLOBAL: {success_score:.1f}%\n")

if success_score >= 75:
    print("✅ SUCCÈS EXCEPTIONNEL:")
    print("   Les 3 agents maintiennent cohérence monde partagé")
    print("   Interactions sociales émergent naturellement")
    print("   Immersion RI collective validée")
elif success_score >= 60:
    print("✅ SUCCÈS PARTIEL:")
    print("   Cohérence monde partagé acceptable")
    print("   Quelques interactions sociales observées")
else:
    print("⚠️  RÉSULTATS MITIGÉS:")
    print("   Cohérence monde partagé limitée")
    print("   Interactions sociales faibles")

print("\n" + "═" * 70)
print("  🎉 TEST MULTI-AGENT TERMINÉ")
print("═" * 70)

print("""
📦 DONNÉES COLLECTÉES:
  • 3 modèles différents testés simultanément
  • Monde RI partagé avec cohérence temporelle
  • Émergence (ou non) de comportements collaboratifs
  • Validation concept multi-agent ready

🚀 IMPLICATIONS:
Si succès > 75%: RI scalable à N agents
Si interactions sociales: Preuve émergence protocoles
Si immersion maintenue: Robustesse framework validée
""")