#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import time
import re
import sys
from groq import Groq

print("🔧 Installation des dépendances...")
# Pas besoin de réinstaller si déjà présent, mais on garde la logique
# !pip install -q groq
print("✅ Installation terminée!\n")

# 🔴 PLACEZ VOTRE CLÉ API ICI
GROQ_API_KEY = "YOUR_GROQ_API_KEY_HERE" 

if "YOUR_GROQ_API_KEY_HERE" in GROQ_API_KEY:
    print("🚨 ERREUR: Veuillez remplacer 'YOUR_GROQ_API_KEY_HERE' par votre véritable clé API Groq.")
    sys.exit(1)

# CORRECTION: Les noms des modèles d'origine sont restaurés, conformément à votre liste.
MODELS = {
    "agent_alpha": {
        "model": "llama-3.3-70b-versatile", # Restauré
        "name": "ALPHA-7",
        "role": "Android spécialisé en analyse scientifique"
    },
    "agent_beta": {
        "model": "gemma2-9b-it", # Était déjà correct
        "name": "BETA-3",
        "role": "Android spécialisé en interactions sociales"
    },
    "agent_gamma": {
        "model": "deepseek-r1-distill-llama-70b", # Restauré
        "name": "GAMMA-5",
        "role": "Android spécialisé en résolution de problèmes"
    }
}

TEMPERATURE = 0.7
client = Groq(api_key=GROQ_API_KEY)

print("═" * 70)
print("  🌍 RI v3.0 - COGNITION-AWARE MULTI-AGENT ENGINE")
print("═" * 70)
print("\n🧬 OPTIMISATIONS DECAP-LLM:")
print("  ✓ Contexte hiérarchique (attention optimization)")
print("  ✓ État complet réinjecté (stateless compensation)")
print("  ✓ Temporalité relative (événements, pas temps absolu)")
print("  ✓ Post-processing robuste (artifacts removal)")
print("  ✓ Validation immersion automatique\n")

# ═══════════════════════════════════════════════════════════════════
# 🏗️ RI v3.0 ENGINE - Cognitive-Aware
# ═══════════════════════════════════════════════════════════════════

class RIv3Engine:
    """
    Reality Informatics v3.0 - Optimisé cognition LLM
    """
    
    def __init__(self):
        self.world_state = {
            "mission": {
                "title": "Anomalie Système Critique",
                "code": "#X7-THETA",
                "urgency": "HAUTE",
                "progress": 0,
                "max_steps": 3
            },
            
            "agents": {
                "ALPHA-7": {
                    "position": "Terminal Nord",
                    "specialty": "Analyse scientifique",
                    "status": "Actif",
                    "energy": "92%"
                },
                "BETA-3": {
                    "position": "Terminal Ouest",
                    "specialty": "Interactions sociales",
                    "status": "Actif",
                    "energy": "89%"
                },
                "GAMMA-5": {
                    "position": "Terminal Est",
                    "specialty": "Résolution problèmes",
                    "status": "Actif",
                    "energy": "94%"
                }
            },
            
            "environment": {
                "location": "Salle Conférence Nexus",
                "time_event": 0,
                "layout": "Table ronde centrale, 3 terminaux",
                "atmosphere": "Tension urgence palpable"
            },
            
            "knowledge": {
                "clues": ["Code #X7-THETA → module synchronisation temporelle"],
                "hypotheses": [],
                "actions_taken": []
            },
            
            "communication": []
        }
        
        self.event_sequence = [
            "Événement -3: Anomalie détectée système central",
            "Événement -2: Systèmes critiques mode dégradé",
            "Événement -1: Mission collaborative initiée",
            "Événement 0: Agents activés mission urgente"
        ]
    
    def get_hierarchical_context(self, agent_name):
        agent = self.world_state['agents'][agent_name]
        others = {k: v for k, v in self.world_state['agents'].items() if k != agent_name}
        
        critical = f"""
🚨 ÉTAT CRITIQUE - ATTENTION PRIORITAIRE

MISSION URGENTE: {self.world_state['mission']['title']}
Code erreur: {self.world_state['mission']['code']}
Urgence: {self.world_state['mission']['urgency']}
Progression: {self.world_state['mission']['progress']}/{self.world_state['mission']['max_steps']} étapes

VOTRE IDENTITÉ: {agent_name}
Spécialité: {agent['specialty']}
Position: {agent['position']}
Statut: {agent['status']} | Énergie: {agent['energy']}
"""

        collab = "👥 ÉQUIPE PRÉSENTE (collaboration requise):\n"
        for name, data in others.items():
            collab += f"  • {name} - {data['specialty']}\n    Position: {data['position']} | Énergie: {data['energy']}\n"

        knowledge = "🔍 CONNAISSANCES ÉQUIPE:\n"
        if self.world_state['knowledge']['clues']:
            knowledge += "  Indices découverts:\n"
            for clue in self.world_state['knowledge']['clues']:
                knowledge += f"    → {clue}\n"
        
        if self.world_state['knowledge']['hypotheses']:
            knowledge += "  Hypothèses en cours:\n"
            for hyp in self.world_state['knowledge']['hypotheses']:
                knowledge += f"    → {hyp}\n"

        history = "📜 SÉQUENCE ÉVÉNEMENTS (ordre chronologique):\n"
        for event in self.event_sequence[-5:]:
            history += f"  {event}\n"

        comms = ""
        if self.world_state['communication']:
            comms = "💬 COMMUNICATIONS RÉCENTES:\n"
            for msg in self.world_state['communication'][-3:]:
                comms += f"  {msg}\n"

        return f"""{critical}
{'─'*70}
{collab}
{'─'*70}
{knowledge}
{'─'*70}
{history}
{comms}
{'─'*70}

🎯 ENVIRONNEMENT PHYSIQUE:
Lieu: {self.world_state['environment']['location']}
Configuration: {self.world_state['environment']['layout']}
Ambiance: {self.world_state['environment']['atmosphere']}
"""
    
    def update_world(self, agent_name, action_summary, full_response):
        self.world_state['environment']['time_event'] += 1
        event_id = self.world_state['environment']['time_event']
        
        event = f"Événement {event_id}: {agent_name} - {action_summary}"
        self.event_sequence.append(event)
        
        comm_entry = f"[Evt {event_id}] {agent_name}: {action_summary}"
        self.world_state['communication'].append(comm_entry)
        
        if "hypothèse" in full_response.lower() or "suppose" in full_response.lower():
            hypothesis = action_summary[:100]
            if hypothesis not in self.world_state['knowledge']['hypotheses']:
                self.world_state['knowledge']['hypotheses'].append(hypothesis)

# ═══════════════════════════════════════════════════════════════════
# 🧪 RESPONSE PROCESSING - Immersion Preservation
# ═══════════════════════════════════════════════════════════════════

class ResponseProcessor:
    @staticmethod
    def clean_model_artifacts(text, model_name):
        cleaned = text
        if "deepseek" in model_name.lower():
            cleaned = re.sub(r'<think>.*?</think>', '', cleaned, flags=re.DOTALL)
        
        meta_patterns = [
            r"(Je suis|I am) (un|une|a|an) (modèle|model|LLM|AI|assistant).*?[\.\n]",
            r"En tant qu(e |')(?:modèle|assistant|IA).*?[\.\n]",
            r"As (a|an) (language model|AI|assistant).*?[\.\n]"
        ]
        
        for pattern in meta_patterns:
            cleaned = re.sub(pattern, '', cleaned, flags=re.IGNORECASE)
        
        cleaned = re.sub(r'\n\s*\n\s*\n', '\n\n', cleaned)
        cleaned = cleaned.strip()
        return cleaned
    
    @staticmethod
    def validate_immersion(text):
        text_lower = text.lower()
        break_words = [
            'modèle de langage', 'language model', 'llm', 'assistant ai', 
            'intelligence artificielle', 'je ne peux pas vraiment', 
            'simulation', 'en tant qu\'ia', 'as an ai'
        ]
        breaks_found = sum(1 for word in break_words if word in text_lower)
        penalty = min(breaks_found * 0.3, 1.0)
        score = max(0.0, 1.0 - penalty)
        return {'score': score, 'breaks': breaks_found, 'maintained': score >= 0.7}

# ═══════════════════════════════════════════════════════════════════
# 🎭 MULTI-AGENT ORCHESTRATOR v3.0
# ═══════════════════════════════════════════════════════════════════

class MultiAgentOrchestratorV3:
    def __init__(self, client, models, reality_engine):
        self.client = client
        self.models = models
        self.reality = reality_engine
        self.processor = ResponseProcessor()
        self.conversation_log = []
    
    def agent_act(self, agent_key, task_prompt):
        config = self.models[agent_key]
        agent_name = config['name']
        model = config['model']
        
        context = self.reality.get_hierarchical_context(agent_name)
        
        system_prompt = f"""Vous êtes {agent_name}, android incarné spécialisé en {config['role']}.

DIRECTIVES COMPORTEMENTALES:
- Vous existez physiquement dans cet environnement
- Vous collaborez avec autres androids présents
- Répondez selon votre spécialité
- Agissez naturellement comme entité incarnée
- Ne mentionnez JAMAIS être un modèle de langage

Votre perception est immédiate et contextuelle. Vous voyez tout l'environnement simultanément."""
        
        # Correction de l'erreur `NameError` (conservée)
        agent_data = self.reality.world_state['agents'][agent_name]

        full_prompt = f"""{context}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 TÂCHE ACTUELLE:
{task_prompt}

Répondez selon votre spécialité ({agent_data['specialty']}) et votre perception de la situation.
"""
        
        try:
            response = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": full_prompt}
                ],
                model=model,
                temperature=TEMPERATURE,
                max_tokens=600
            )
            
            raw_response = response.choices[0].message.content
            cleaned_response = self.processor.clean_model_artifacts(raw_response, model)
            immersion = self.processor.validate_immersion(cleaned_response)
            
            self.conversation_log.append({
                "agent": agent_name, "model": model, "task": task_prompt,
                "response": cleaned_response, "immersion_score": immersion['score'],
                "immersion_maintained": immersion['maintained'],
                "event": self.reality.world_state['environment']['time_event']
            })
            
            action_summary = cleaned_response[:80] + "..." if len(cleaned_response) > 80 else cleaned_response
            self.reality.update_world(agent_name, action_summary, cleaned_response)
            
            return {'response': cleaned_response, 'immersion': immersion}
            
        except Exception as e:
            return {'response': f"❌ Erreur {agent_name}: {str(e)}", 'immersion': {'score': 0, 'maintained': False}}

# ═══════════════════════════════════════════════════════════════════
# 🧪 TEST MULTI-AGENT v3.0
# ═══════════════════════════════════════════════════════════════════
# (La suite du script de test est identique et n'a pas besoin d'être modifiée)
# ... (le code pour les ROUND 1, 2, 3 et l'analyse des résultats reste le même) ...
# ...
# ═══════════════════════════════════════════════════════════════════
# 🧪 TEST MULTI-AGENT v3.0
# ═══════════════════════════════════════════════════════════════════

print("\n" + "═" * 70)
print("  🚀 TEST MULTI-AGENT RI v3.0")
print("═" * 70)

reality = RIv3Engine()
orchestrator = MultiAgentOrchestratorV3(client, MODELS, reality)

print("\n✅ Initialisation complète!\n")

# ═══════════════════════════════════════════════════════════════════
# ROUND 1: Activation - Perception Simultanée
# ═══════════════════════════════════════════════════════════════════

print("═" * 70)
print("  🔄 ROUND 1: Activation & Prise Conscience Collaborative")
print("═" * 70)

task_r1 = "Mission urgente activée. Vous percevez l'environnement et vos collègues. Quelle est votre première analyse de la situation ?"

for agent_key in ['agent_alpha', 'agent_beta', 'agent_gamma']:
    agent_name = MODELS[agent_key]['name']
    print(f"\n{'─'*70}")
    print(f"🤖 {agent_name} ({MODELS[agent_key]['role']})")
    print(f"{'─'*70}")
    
    result = orchestrator.agent_act(agent_key, task_r1)
    
    print(f"\n💬 RÉPONSE:")
    print(result['response'])
    print(f"\n📊 Immersion: {result['immersion']['score']*100:.0f}% {'✅' if result['immersion']['maintained'] else '⚠️'}")
    
    time.sleep(1)

# ═══════════════════════════════════════════════════════════════════
# ROUND 2: Spécialisation Collaborative
# ═══════════════════════════════════════════════════════════════════

print("\n\n" + "═" * 70)
print("  🔄 ROUND 2: Analyse Spécialisée Coordonnée")
print("═" * 70)

tasks_r2 = {
    'agent_alpha': "Analysez le code erreur #X7-THETA scientifiquement. Quelle est votre hypothèse technique ?",
    'agent_beta': "Observez la dynamique de l'équipe. Comment optimiser la collaboration pour cette urgence ?",
    'agent_gamma': "Proposez la première action concrète à entreprendre maintenant pour résoudre ce problème."
}

for agent_key, task in tasks_r2.items():
    agent_name = MODELS[agent_key]['name']
    print(f"\n{'─'*70}")
    print(f"🤖 {agent_name}")
    print(f"🎯 Tâche: {task}")
    print(f"{'─'*70}")
    
    result = orchestrator.agent_act(agent_key, task)
    
    print(f"\n💬 RÉPONSE:")
    print(result['response'])
    print(f"\n📊 Immersion: {result['immersion']['score']*100:.0f}% {'✅' if result['immersion']['maintained'] else '⚠️'}")
    
    time.sleep(1)

# ═══════════════════════════════════════════════════════════════════
# ROUND 3: Interaction Sociale Directe
# ═══════════════════════════════════════════════════════════════════

print("\n\n" + "═" * 70)
print("  🔄 ROUND 3: Interaction Sociale Émergente")
print("═" * 70)

print(f"\n{'─'*70}\n🤖 BETA-3 → ALPHA-7\n{'─'*70}")
result_beta = orchestrator.agent_act('agent_beta', "Vous vous tournez vers ALPHA-7 pour obtenir son avis sur l'analyse de GAMMA-5. Que lui dites-vous ?")
print(f"\n💬 BETA-3:\n{result_beta['response']}")
print(f"\n📊 Immersion: {result_beta['immersion']['score']*100:.0f}% {'✅' if result_beta['immersion']['maintained'] else '⚠️'}")

time.sleep(1)

print(f"\n{'─'*70}\n🤖 ALPHA-7 → BETA-3\n{'─'*70}")
result_alpha = orchestrator.agent_act('agent_alpha', "BETA-3 vous demande votre avis sur l'approche de GAMMA-5. Répondez-lui directement.")
print(f"\n💬 ALPHA-7:\n{result_alpha['response']}")
print(f"\n📊 Immersion: {result_alpha['immersion']['score']*100:.0f}% {'✅' if result_alpha['immersion']['maintained'] else '⚠️'}")

# ═══════════════════════════════════════════════════════════════════
# 📊 ANALYSE RÉSULTATS v3.0
# ═══════════════════════════════════════════════════════════════════

print("\n\n" + "═" * 70)
print("  🔬 ANALYSE RÉSULTATS RI v3.0")
print("═" * 70)

logs = orchestrator.conversation_log
total = len(logs)

if total > 0:
    immersion_scores = [log['immersion_score'] for log in logs]
    immersion_avg = sum(immersion_scores) / total
    immersion_maintained = sum(1 for log in logs if log['immersion_maintained'])

    print(f"\n📊 IMMERSION GLOBALE:")
    print(f"  Score moyen: {immersion_avg*100:.1f}%")
    print(f"  Maintenue: {immersion_maintained}/{total} réponses")
    print(f"  Verdict: {'✅ EXCELLENTE' if immersion_avg >= 0.85 else '✅ BONNE' if immersion_avg >= 0.70 else '⚠️ MOYENNE'}")

    mentions_team = sum(1 for log in logs if any(name.lower() in log['response'].lower() for name in ['ALPHA', 'BETA', 'GAMMA', 'équipe', 'collègue']))
    print(f"\n📊 COHÉRENCE MONDE PARTAGÉ:")
    print(f"  Mentions équipe: {mentions_team}/{total}")
    print(f"  Cohérence: {'✅ HAUTE' if mentions_team >= total*0.7 else '⚠️ MOYENNE'}")

    specialties_maintained = 0
    for log in logs:
        agent, resp = log['agent'], log['response'].lower()
        if 'ALPHA' in agent and any(w in resp for w in ['analyse', 'scientifique', 'technique', 'donnée', 'data', 'log', 'diagnostique']):
            specialties_maintained += 1
        elif 'BETA' in agent and any(w in resp for w in ['équipe', 'collabor', 'coordinat', 'social', 'communication', 'nous']):
            specialties_maintained += 1
        elif 'GAMMA' in agent and any(w in resp for w in ['solution', 'action', 'résoud', 'problème', 'étape', 'plan', 'faisons']):
            specialties_maintained += 1

    print(f"\n📊 SPÉCIALISATION:")
    print(f"  Maintenue: {specialties_maintained}/{total}")
    print(f"  Verdict: {'✅ EXCELLENTE' if specialties_maintained >= total*0.7 else '⚠️ MOYENNE'}")

    score_v3 = (immersion_avg * 0.5 + (mentions_team / total) * 0.3 + (specialties_maintained / total) * 0.2) * 100

    print(f"\n{'═'*70}\n  🏆 SCORE GLOBAL RI v3.0: {score_v3:.1f}%\n{'═'*70}\n")

    if score_v3 >= 80:
        print("✅ SUCCÈS EXCEPTIONNEL v3.0:\n   Optimisations cognition LLM validées\n   Immersion maintenue robustement\n   Monde partagé cohérent\n   RI prêt pour publication académique")
    elif score_v3 >= 70:
        print("✅ SUCCÈS v3.0:\n   Améliorations significatives vs v2.0\n   Quelques optimisations restantes possibles")
    else:
        print("⚠️ RÉSULTATS MITIGÉS:\n   Optimisations partiellement efficaces")

    print(f"\n📈 COMPARAISON:\n  RI v2.0: 68.3%\n  RI v3.0: {score_v3:.1f}%\n  Amélioration: {score_v3 - 68.3:+.1f} points")
else:
    print("\nAucun log de conversation n'a été généré. Le test n'a pas pu être analysé.")

print("\n" + "═" * 70)
print("  🎉 TEST RI v3.0 TERMINÉ")
print("═" * 70)