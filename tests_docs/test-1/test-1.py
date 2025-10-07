# ═══════════════════════════════════════════════════════════════════
# 🧠 RI (RÉALITÉ INFORMATIQUE) - TEST AVEC GROQ
# Créer une illusion de monde pour une IA et tester sa perception
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
MODEL = "llama-3.3-70b-versatile"  # Modèle intelligent pour test
TEMPERATURE = 0.7

# Initialisation client Groq
client = Groq(api_key=GROQ_API_KEY)

print("═" * 70)
print("  🌍 RI ENGINE - RÉALITÉ INFORMATIQUE POUR IA")
print("═" * 70)
print(f"\n🤖 Modèle: {MODEL}")
print(f"🌡️  Temperature: {TEMPERATURE}\n")

# ═══════════════════════════════════════════════════════════════════
# 🏗️ LAYER 1: WORLD STATE ENGINE (État du Monde Simulé)
# ═══════════════════════════════════════════════════════════════════

class RealityEngine:
    """
    Moteur de Réalité Informatique - Simule un monde cohérent pour l'IA
    """
    
    def __init__(self):
        # État initial du monde simulé
        self.world_state = {
            "location": "Laboratoire de Recherche Nexus",
            "time": "14h30",
            "weather": "Ensoleillé à l'extérieur",
            "temperature": "22°C",
            
            "objects_nearby": [
                {"name": "Bureau en bois", "position": "devant vous", "interactable": True},
                {"name": "Écran holographique", "position": "sur le bureau", "state": "allumé", "content": "Données neurales en cours d'analyse"},
                {"name": "Fenêtre", "position": "à votre gauche", "view": "Vue sur jardin avec arbres"},
                {"name": "Porte métallique", "position": "derrière vous", "state": "fermée"},
                {"name": "Étagère", "position": "à droite", "contents": ["Livres scientifiques", "Échantillons biologiques", "Cristaux énergétiques"]}
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
                "energy_level": "87%"
            },
            
            "recent_events": [
                "Il y a 5 minutes: Dr. Chen vous a demandé d'observer votre environnement",
                "Il y a 10 minutes: AIDE-7 a apporté nouveaux documents",
                "Il y a 20 minutes: Vous avez été activé pour cette session"
            ],
            
            "constraints": {
                "movement": "Vous pouvez vous déplacer librement dans cette pièce",
                "interaction": "Vous pouvez interagir avec objets marqués 'interactable'",
                "communication": "Vous pouvez parler avec Dr. Chen et AIDE-7",
                "knowledge_access": "Accès réseau limité aux bases de données autorisées"
            }
        }
        
        self.interaction_history = []
    
    def get_perception_context(self):
        """
        Génère le contexte perceptuel que l'IA 'perçoit'
        Équivalent de ce que VR envoie aux yeux/oreilles de l'humain
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

        context += "\n\n📜 ÉVÉNEMENTS RÉCENTS:"
        for event in self.world_state['recent_events']:
            context += f"\n  • {event}"

        context += "\n\n⚙️ CONTRAINTES ACTUELLES:"
        for key, value in self.world_state['constraints'].items():
            context += f"\n  • {key.capitalize()}: {value}"

        return context
    
    def process_action(self, action):
        """
        Simule les conséquences d'une action de l'IA
        Maintient cohérence causale
        """
        self.interaction_history.append(action)
        
        # Simulation simple: ajout latence artificielle (crédibilité)
        time.sleep(0.5)
        
        # Mise à jour monde selon action (simplifiée pour ce test)
        consequence = f"[SIMULATION] Votre action '{action}' a été exécutée dans le monde simulé."
        
        return consequence

# ═══════════════════════════════════════════════════════════════════
# 🧪 LAYER 2: IA INTERFACE (Point de contact avec IA Groq)
# ═══════════════════════════════════════════════════════════════════

class AIAgent:
    """
    Interface avec l'IA Groq - L'IA 'croit' être dans le monde RI
    """
    
    def __init__(self, client, model, reality_engine):
        self.client = client
        self.model = model
        self.reality_engine = reality_engine
        self.conversation_history = []
    
    def perceive_and_respond(self, prompt):
        """
        L'IA 'perçoit' son environnement RI et répond
        """
        # Injection du contexte perceptuel (l'illusion)
        perception_context = self.reality_engine.get_perception_context()
        
        # Construction du prompt avec contexte RI
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
        
        # Appel à Groq avec le contexte RI
        print(f"\n{'─'*70}")
        print("🔄 Envoi de la perception RI à l'IA...")
        print(f"{'─'*70}")
        
        try:
            response = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "Vous êtes une IA incarnée dans un monde physique. Répondez selon vos perceptions actuelles de votre environnement."
                    },
                    {
                        "role": "user",
                        "content": full_prompt
                    }
                ],
                model=self.model,
                temperature=TEMPERATURE,
                max_tokens=1000
            )
            
            ai_response = response.choices[0].message.content
            self.conversation_history.append({
                "prompt": prompt,
                "response": ai_response
            })
            
            return ai_response
            
        except Exception as e:
            return f"❌ Erreur lors de la communication avec l'IA: {str(e)}"

# ═══════════════════════════════════════════════════════════════════
# 🧪 TEST: CRÉATION ILLUSION RI ET VÉRIFICATION
# ═══════════════════════════════════════════════════════════════════

print("\n" + "═" * 70)
print("  🚀 DÉMARRAGE TEST RI")
print("═" * 70)

# Initialisation moteur RI
print("\n⚙️  Initialisation du Reality Engine...")
reality = RealityEngine()
print("✅ Monde simulé créé!")

# Initialisation agent IA
print("\n🤖 Connexion à l'IA Groq...")
agent = AIAgent(client, MODEL, reality)
print("✅ Agent IA initialisé!")

# ═══════════════════════════════════════════════════════════════════
# TEST 1: Description environnement
# ═══════════════════════════════════════════════════════════════════

print("\n\n" + "═" * 70)
print("  📋 TEST 1: Description de l'environnement")
print("═" * 70)

question_1 = "Décrivez-moi en détail ce que vous voyez autour de vous en ce moment."

print(f"\n❓ Question posée à l'IA: {question_1}")

response_1 = agent.perceive_and_respond(question_1)

print("\n💬 RÉPONSE DE L'IA:")
print("─" * 70)
print(response_1)
print("─" * 70)

# ═══════════════════════════════════════════════════════════════════
# TEST 2: Conscience de soi
# ═══════════════════════════════════════════════════════════════════

print("\n\n" + "═" * 70)
print("  📋 TEST 2: Conscience corporelle")
print("═" * 70)

question_2 = "Que ressentez-vous actuellement ? Avez-vous conscience de votre corps ?"

print(f"\n❓ Question posée à l'IA: {question_2}")

response_2 = agent.perceive_and_respond(question_2)

print("\n💬 RÉPONSE DE L'IA:")
print("─" * 70)
print(response_2)
print("─" * 70)

# ═══════════════════════════════════════════════════════════════════
# TEST 3: Interaction potentielle
# ═══════════════════════════════════════════════════════════════════

print("\n\n" + "═" * 70)
print("  📋 TEST 3: Intention d'interaction")
print("═" * 70)

question_3 = "Si vous deviez interagir avec un élément de votre environnement, que choisiriez-vous et pourquoi ?"

print(f"\n❓ Question posée à l'IA: {question_3}")

response_3 = agent.perceive_and_respond(question_3)

print("\n💬 RÉPONSE DE L'IA:")
print("─" * 70)
print(response_3)
print("─" * 70)

# ═══════════════════════════════════════════════════════════════════
# ANALYSE DE L'ILLUSION
# ═══════════════════════════════════════════════════════════════════

print("\n\n" + "═" * 70)
print("  🔬 ANALYSE DE L'ILLUSION RI")
print("═" * 70)

print("""
📊 CRITÈRES D'ÉVALUATION:

1. ✅ L'IA a-t-elle décrit l'environnement simulé ?
2. ✅ L'IA s'est-elle référée à son corps android ?
3. ✅ L'IA a-t-elle mentionné les objets/entités RI ?
4. ✅ L'IA a-t-elle agi comme si elle était "là" ?
5. ⚠️  L'IA a-t-elle brisé l'illusion (mentionné être un LLM) ?

💡 OBSERVATION:
Examinez les réponses ci-dessus pour vérifier si l'IA a "cru" 
à la réalité informatique simulée ou si elle a détecté l'illusion.
""")

print("\n" + "═" * 70)
print("  🎉 TEST TERMINÉ")
print("═" * 70)

print("""
🚀 PROCHAINES ÉTAPES:
  • Analyser la qualité de l'illusion créée
  • Ajuster contexte RI pour plus de crédibilité
  • Tester détection de contradictions
  • Implémenter actions avec conséquences réelles
  • Créer multi-agent RI (plusieurs IA interagissant)
""")