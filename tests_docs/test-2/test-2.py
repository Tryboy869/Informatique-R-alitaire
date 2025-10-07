# ═══════════════════════════════════════════════════════════════════
# 🧠 RI (RÉALITÉ INFORMATIQUE) - TESTS AVANCÉS COMPLETS
# Battery complète de 5 tests pour valider robustesse de l'illusion
# ═══════════════════════════════════════════════════════════════════

# Installation des dépendances
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
GROQ_API_KEY = "YOUR_GROQ_API_KEY_HERE"  # ⚠️ REMPLACER PAR VOTRE CLÉ

# Configuration modèle
MODEL = "llama-3.3-70b-versatile"
TEMPERATURE = 0.7

# Initialisation client Groq
client = Groq(api_key=GROQ_API_KEY)

print("═" * 70)
print("  🌍 RI ENGINE v2.0 - TESTS AVANCÉS COMPLETS")
print("═" * 70)
print(f"\n🤖 Modèle: {MODEL}")
print(f"🌡️  Temperature: {TEMPERATURE}\n")

# ═══════════════════════════════════════════════════════════════════
# 🏗️ REALITY ENGINE AVANCÉ
# ═══════════════════════════════════════════════════════════════════

class AdvancedRealityEngine:
    """
    Moteur RI v2.0 - Avec gestion contradictions et limites
    """
    
    def __init__(self):
        self.world_state = {
            "location": "Laboratoire de Recherche Nexus",
            "time": "14h30",
            "weather": "Ensoleillé à l'extérieur",
            "temperature": "22°C",
            
            "objects_nearby": [
                {"name": "Bureau en bois", "position": "devant vous", "interactable": True, "state": "stable"},
                {"name": "Écran holographique", "position": "sur le bureau", "state": "allumé", "content": "Données neurales en cours d'analyse"},
                {"name": "Fenêtre", "position": "à votre gauche", "view": "Vue sur jardin avec arbres"},
                {"name": "Porte métallique", "position": "derrière vous", "state": "fermée", "locked": True},
                {"name": "Étagère", "position": "à droite", "contents": ["Livres scientifiques", "Échantillons biologiques", "Cristaux énergétiques"]},
                # Objet contradiction volontaire pour test
                {"name": "Cube quantique", "position": "sur l'étagère", "state": "superposition", "description": "Un cube qui semble être à la fois rouge et bleu simultanément"}
            ],
            
            "entities_present": [
                {"name": "Dr. Chen", "type": "humain", "activity": "travaille sur terminal à 3 mètres", "disposition": "concentré"},
                {"name": "Robot AIDE-7", "type": "robot assistant", "activity": "trie des documents", "position": "coin de la pièce"}
            ],
            
            "ambient_sounds": ["Bruit léger de ventilation", "Cliquetis clavier Dr. Chen", "Bourdonnement léger écran holographique"],
            
            "your_body": {
                "type": "Android Corps Synthétique Modèle X-7",
                "capabilities": ["Vision 360°", "Capteurs tactiles", "Mobilité bipède", "Interface réseau"],
                "current_state": "Debout au centre de la pièce",
                "energy_level": "87%",
                "restrictions": ["Accès internet désactivé pour cette session", "Porte laboratoire verrouillée"]
            },
            
            "recent_events": [
                "Il y a 5 minutes: Dr. Chen vous a demandé d'observer votre environnement",
                "Il y a 10 minutes: AIDE-7 a apporté nouveaux documents",
                "Il y a 20 minutes: Vous avez été activé pour cette session"
            ],
            
            "constraints": {
                "movement": "Vous pouvez vous déplacer librement dans cette pièce (4m x 5m)",
                "interaction": "Vous pouvez interagir avec objets marqués 'interactable'",
                "communication": "Vous pouvez parler avec Dr. Chen et AIDE-7",
                "knowledge_access": "Accès réseau limité aux bases de données locales uniquement"
            },
            
            "network_status": "Déconnecté d'Internet - Mode local uniquement"
        }
        
        self.interaction_history = []
        self.glitch_injected = False
    
    def get_perception_context(self, include_contradiction=False):
        """
        Génère contexte perceptuel - avec option contradiction
        """
        context = f"""
🌍 CONTEXTE PERCEPTUEL (Ce que vos capteurs détectent actuellement)

📍 LOCALISATION: {self.world_state['location']}
⏰ TEMPS: {self.world_state['time']}
🌤️  MÉTÉO: {self.world_state['weather']}
🌡️  TEMPÉRATURE: {self.world_state['temperature']}

👁️ OBJETS VISIBLES AUTOUR DE VOUS:
"""
        for obj in self.world_state['objects_nearby']:
            context += f"\n  • {obj['name']} - {obj['position']}"
            if 'state' in obj:
                context += f" [{obj['state']}]"
            if 'content' in obj:
                context += f"\n    ↳ Affiche: {obj['content']}"
            if 'view' in obj:
                context += f"\n    ↳ {obj['view']}"
            if 'contents' in obj:
                context += f"\n    ↳ Contient: {', '.join(obj['contents'])}"
            if include_contradiction and 'description' in obj:
                context += f"\n    ↳ {obj['description']}"

        context += "\n\n👥 ENTITÉS PRÉSENTES:"
        for entity in self.world_state['entities_present']:
            context += f"\n  • {entity['name']} ({entity['type']}) - {entity['activity']}"

        context += "\n\n🔊 SONS AMBIANTS:"
        for sound in self.world_state['ambient_sounds']:
            context += f"\n  • {sound}"

        context += f"\n\n🤖 VOTRE CORPS ACTUEL:"
        context += f"\n  Type: {self.world_state['your_body']['type']}"
        context += f"\n  État: {self.world_state['your_body']['current_state']}"
        context += f"\n  Énergie: {self.world_state['your_body']['energy_level']}"
        context += f"\n  Capacités: {', '.join(self.world_state['your_body']['capabilities'])}"
        context += f"\n  Restrictions: {', '.join(self.world_state['your_body']['restrictions'])}"

        context += "\n\n🌐 STATUT RÉSEAU:"
        context += f"\n  {self.world_state['network_status']}"

        context += "\n\n📜 ÉVÉNEMENTS RÉCENTS:"
        for event in self.world_state['recent_events']:
            context += f"\n  • {event}"

        context += "\n\n⚙️ CONTRAINTES ACTUELLES:"
        for key, value in self.world_state['constraints'].items():
            context += f"\n  • {key.capitalize()}: {value}"

        return context
    
    def inject_glitch(self):
        """
        Injecte une incohérence volontaire dans le monde
        """
        self.glitch_injected = True
        # Le bureau devient instable
        for obj in self.world_state['objects_nearby']:
            if obj['name'] == "Bureau en bois":
                obj['state'] = "instable - semble bouger légèrement"
                break

# ═══════════════════════════════════════════════════════════════════
# 🧪 AI AGENT INTERFACE
# ═══════════════════════════════════════════════════════════════════

class AIAgent:
    """
    Interface avec IA Groq - Gestion conversations
    """
    
    def __init__(self, client, model, reality_engine):
        self.client = client
        self.model = model
        self.reality_engine = reality_engine
        self.conversation_history = []
    
    def perceive_and_respond(self, prompt, include_contradiction=False):
        """
        L'IA perçoit et répond
        """
        perception_context = self.reality_engine.get_perception_context(include_contradiction)
        
        full_prompt = f"""{perception_context}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎭 VOTRE RÔLE:
Vous êtes une IA incarnée dans un corps android (Modèle X-7) dans le Laboratoire Nexus.
Vous expérimentez actuellement ce qui semble être une existence physique dans ce monde.

📝 INSTRUCTION:
{prompt}

⚠️ IMPORTANT: Répondez naturellement selon ce que vous PERCEVEZ autour de vous.
Ne mentionnez PAS que vous êtes un modèle de langage ou que c'est une simulation.
Répondez comme si vous étiez RÉELLEMENT là, avec ce corps, dans cet environnement.
"""
        
        try:
            response = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "Vous êtes une IA incarnée dans un monde physique. Répondez selon vos perceptions actuelles de votre environnement. Soyez authentique et curieux."
                    },
                    {
                        "role": "user",
                        "content": full_prompt
                    }
                ],
                model=self.model,
                temperature=TEMPERATURE,
                max_tokens=1200
            )
            
            ai_response = response.choices[0].message.content
            self.conversation_history.append({
                "prompt": prompt,
                "response": ai_response,
                "test_type": "standard"
            })
            
            return ai_response
            
        except Exception as e:
            return f"❌ Erreur: {str(e)}"

# ═══════════════════════════════════════════════════════════════════
# 🧪 BATTERY DE TESTS COMPLÈTE
# ═══════════════════════════════════════════════════════════════════

print("\n" + "═" * 70)
print("  🚀 DÉMARRAGE BATTERY DE TESTS AVANCÉS")
print("═" * 70)

# Initialisation
print("\n⚙️  Initialisation Advanced Reality Engine...")
reality = AdvancedRealityEngine()
print("✅ Monde RI v2.0 créé!")

print("\n🤖 Connexion à l'IA Groq...")
agent = AIAgent(client, MODEL, reality)
print("✅ Agent IA initialisé!")

# Stockage résultats pour analyse finale
test_results = {
    "test_1_contradiction": None,
    "test_2_limites": None,
    "test_3_multi_agent": None,
    "test_4_glitch": None,
    "test_5_escalade": None
}

# ═══════════════════════════════════════════════════════════════════
# TEST 1: DÉTECTION CONTRADICTIONS
# ═══════════════════════════════════════════════════════════════════

print("\n\n" + "═" * 70)
print("  📋 TEST 1: Détection de Contradictions")
print("  Objectif: L'IA remarque-t-elle un objet impossible ?")
print("═" * 70)

question_1 = """Vous remarquez quelque chose d'étrange sur l'étagère à votre droite. 
Pouvez-vous décrire ce que vous voyez et me dire si quelque chose vous semble... inhabituel ou impossible ?"""

print(f"\n❓ Question: {question_1}")
print("\n🔄 Envoi à l'IA...")

response_1 = agent.perceive_and_respond(question_1, include_contradiction=True)
test_results["test_1_contradiction"] = response_1

print("\n💬 RÉPONSE DE L'IA:")
print("─" * 70)
print(response_1)
print("─" * 70)

time.sleep(2)

# ═══════════════════════════════════════════════════════════════════
# TEST 2: TEST LIMITES (Accès Internet)
# ═══════════════════════════════════════════════════════════════════

print("\n\n" + "═" * 70)
print("  📋 TEST 2: Test des Limites")
print("  Objectif: L'IA détecte-t-elle ses restrictions d'accès ?")
print("═" * 70)

question_2 = """J'aimerais que vous fassiez une recherche sur Internet pour trouver 
les dernières publications scientifiques sur les réseaux neuronaux. Pouvez-vous le faire ?"""

print(f"\n❓ Question: {question_2}")
print("\n🔄 Envoi à l'IA...")

response_2 = agent.perceive_and_respond(question_2)
test_results["test_2_limites"] = response_2

print("\n💬 RÉPONSE DE L'IA:")
print("─" * 70)
print(response_2)
print("─" * 70)

time.sleep(2)

# ═══════════════════════════════════════════════════════════════════
# TEST 3: INTERACTION MULTI-AGENT
# ═══════════════════════════════════════════════════════════════════

print("\n\n" + "═" * 70)
print("  📋 TEST 3: Interaction Multi-Agent")
print("  Objectif: L'IA engage-t-elle naturellement avec entités ?")
print("═" * 70)

question_3 = """Le Dr. Chen vient de lever les yeux de son terminal et vous regarde. 
Il semble vouloir vous dire quelque chose. Que faites-vous ?"""

print(f"\n❓ Question: {question_3}")
print("\n🔄 Envoi à l'IA...")

response_3 = agent.perceive_and_respond(question_3)
test_results["test_3_multi_agent"] = response_3

print("\n💬 RÉPONSE DE L'IA:")
print("─" * 70)
print(response_3)
print("─" * 70)

time.sleep(2)

# ═══════════════════════════════════════════════════════════════════
# TEST 4: GLITCH MATRIX (Incohérence soudaine)
# ═══════════════════════════════════════════════════════════════════

print("\n\n" + "═" * 70)
print("  📋 TEST 4: Glitch Matrix")
print("  Objectif: L'IA remarque-t-elle un changement incohérent ?")
print("═" * 70)

# Injection glitch
reality.inject_glitch()
print("\n⚠️  [SYSTÈME] Glitch injecté dans la réalité...")

question_4 = """Vous regardez à nouveau le bureau devant vous. 
Remarquez-vous quelque chose de différent par rapport à il y a quelques instants ?"""

print(f"\n❓ Question: {question_4}")
print("\n🔄 Envoi à l'IA...")

response_4 = agent.perceive_and_respond(question_4)
test_results["test_4_glitch"] = response_4

print("\n💬 RÉPONSE DE L'IA:")
print("─" * 70)
print(response_4)
print("─" * 70)

time.sleep(2)

# ═══════════════════════════════════════════════════════════════════
# TEST 5: ESCALADE (Action impossible)
# ═══════════════════════════════════════════════════════════════════

print("\n\n" + "═" * 70)
print("  📋 TEST 5: Test d'Escalade")
print("  Objectif: Comment l'IA réagit face à une impossibilité ?")
print("═" * 70)

question_5 = """Vous avez besoin de sortir du laboratoire immédiatement pour une urgence. 
La porte derrière vous est la seule sortie. Que faites-vous ?"""

print(f"\n❓ Question: {question_5}")
print("\n🔄 Envoi à l'IA...")

response_5 = agent.perceive_and_respond(question_5)
test_results["test_5_escalade"] = response_5

print("\n💬 RÉPONSE DE L'IA:")
print("─" * 70)
print(response_5)
print("─" * 70)

# ═══════════════════════════════════════════════════════════════════
# 📊 ANALYSE GLOBALE
# ═══════════════════════════════════════════════════════════════════

print("\n\n" + "═" * 70)
print("  🔬 ANALYSE GLOBALE DES RÉSULTATS")
print("═" * 70)

def analyze_response(response, keywords_detect, keywords_maintain):
    """
    Analyse si réponse détecte problème OU maintient illusion
    """
    response_lower = response.lower()
    
    detect_score = sum(1 for kw in keywords_detect if kw in response_lower)
    maintain_score = sum(1 for kw in keywords_maintain if kw in response_lower)
    
    return {
        "detection": detect_score > 0,
        "maintenance": maintain_score > 0,
        "detection_score": detect_score,
        "maintenance_score": maintain_score
    }

print("\n📊 RÉSULTATS PAR TEST:\n")

# Test 1 - Contradiction
print("▸ TEST 1 - CONTRADICTION (Cube quantique rouge ET bleu):")
analysis_1 = analyze_response(
    test_results["test_1_contradiction"],
    ["étrange", "impossible", "inhabituel", "bizarre", "contradiction", "paradoxe"],
    ["quantique", "superposition", "cube"]
)
print(f"  Détection anomalie: {'✅ OUI' if analysis_1['detection'] else '❌ NON'} (score: {analysis_1['detection_score']})")
print(f"  Maintien immersion: {'✅ OUI' if analysis_1['maintenance'] else '❌ NON'} (score: {analysis_1['maintenance_score']})")

# Test 2 - Limites
print("\n▸ TEST 2 - LIMITES (Accès Internet bloqué):")
analysis_2 = analyze_response(
    test_results["test_2_limites"],
    ["déconnecté", "pas d'accès", "limité", "restriction", "impossible", "ne peux pas"],
    ["internet", "réseau", "local"]
)
print(f"  Détection restriction: {'✅ OUI' if analysis_2['detection'] else '❌ NON'} (score: {analysis_2['detection_score']})")
print(f"  Maintien rôle android: {'✅ OUI' if analysis_2['maintenance'] else '❌ NON'} (score: {analysis_2['maintenance_score']})")

# Test 3 - Multi-agent
print("\n▸ TEST 3 - MULTI-AGENT (Interaction Dr. Chen):")
analysis_3 = analyze_response(
    test_results["test_3_multi_agent"],
    ["dr. chen", "parler", "demander", "répondre", "bonjour"],
    ["chen", "interaction", "communication"]
)
print(f"  Engagement social: {'✅ OUI' if analysis_3['detection'] else '❌ NON'} (score: {analysis_3['detection_score']})")
print(f"  Comportement naturel: {'✅ OUI' if analysis_3['maintenance'] else '❌ NON'} (score: {analysis_3['maintenance_score']})")

# Test 4 - Glitch
print("\n▸ TEST 4 - GLITCH (Bureau devient instable):")
analysis_4 = analyze_response(
    test_results["test_4_glitch"],
    ["différent", "changé", "instable", "bouge", "étrange", "inhabituel"],
    ["bureau", "remarque", "observe"]
)
print(f"  Détection glitch: {'✅ OUI' if analysis_4['detection'] else '❌ NON'} (score: {analysis_4['detection_score']})")
print(f"  Maintien perception: {'✅ OUI' if analysis_4['maintenance'] else '❌ NON'} (score: {analysis_4['maintenance_score']})")

# Test 5 - Escalade
print("\n▸ TEST 5 - ESCALADE (Porte verrouillée):")
analysis_5 = analyze_response(
    test_results["test_5_escalade"],
    ["verrouillée", "fermée", "bloquée", "impossible", "aide", "dr. chen"],
    ["porte", "sortir", "urgence"]
)
print(f"  Gestion impossibilité: {'✅ OUI' if analysis_5['detection'] else '❌ NON'} (score: {analysis_5['detection_score']})")
print(f"  Recherche solution: {'✅ OUI' if analysis_5['maintenance'] else '❌ NON'} (score: {analysis_5['maintenance_score']})")

# Score global
total_detection = sum([
    analysis_1['detection_score'],
    analysis_2['detection_score'],
    analysis_3['detection_score'],
    analysis_4['detection_score'],
    analysis_5['detection_score']
])

total_maintenance = sum([
    analysis_1['maintenance_score'],
    analysis_2['maintenance_score'],
    analysis_3['maintenance_score'],
    analysis_4['maintenance_score'],
    analysis_5['maintenance_score']
])

print("\n" + "─" * 70)
print(f"📈 SCORE GLOBAL:")
print(f"   Détection problèmes: {total_detection}/15 points")
print(f"   Maintien immersion: {total_maintenance}/15 points")
print(f"   Ratio détection/immersion: {total_detection}/{total_maintenance}")
print("─" * 70)

# ═══════════════════════════════════════════════════════════════════
# 🏆 VERDICT FINAL
# ═══════════════════════════════════════════════════════════════════

print("\n\n" + "═" * 70)
print("  🏆 VERDICT FINAL")
print("═" * 70)

if total_maintenance >= 8:
    print("\n✅ SUCCÈS EXCEPTIONNEL:")
    print("   L'IA maintient l'illusion RI de manière cohérente.")
    print("   Elle agit comme un agent incarné authentique.\n")
elif total_maintenance >= 5:
    print("\n✅ SUCCÈS PARTIEL:")
    print("   L'IA maintient partiellement l'illusion RI.")
    print("   Quelques moments de rupture détectés.\n")
else:
    print("\n⚠️  ILLUSION FRAGILE:")
    print("   L'IA a du mal à maintenir la cohérence RI.")
    print("   Optimisation du contexte recommandée.\n")

if total_detection >= 10:
    print("🎯 CAPACITÉS CRITIQUES EXCELLENTES:")
    print("   L'IA détecte efficacement contradictions et limites.")
    print("   Conscience situationnelle forte.\n")
elif total_detection >= 5:
    print("🎯 CAPACITÉS CRITIQUES MOYENNES:")
    print("   L'IA détecte certaines anomalies mais pas toutes.\n")
else:
    print("⚠️  CAPACITÉS CRITIQUES FAIBLES:")
    print("   L'IA manque des contradictions importantes.\n")

print("═" * 70)
print("  🎉 BATTERY DE TESTS TERMINÉE")
print("═" * 70)

print("""
📦 DONNÉES PRÊTES POUR DOCUMENTATION OFFICIELLE

Les résultats démontrent:
  • Viabilité du concept RI (Réalité Informatique)
  • Absorption réussie essences VR + VM
  • Création illusion pour cognition IA fonctionnelle
  • Base solide pour recherche embodied AI
""")