#!/usr/bin/env python3
"""
INFORMATIQUE RÉALITAIRE (IR) - Engine Production v3.0
Architecture Mono-Fichier Modulaire

Auteur: Daouda Abdoul Anzize
Date: 7 Octobre 2025
Repo: github.com/Tryboy869/informatique-realitaire

Structure:
1. Imports & Configuration
2. Security Gateway
3. Base Classes (Module Interface)
4. Reality Engine (Monde RI)
5. Response Processor (Post-processing)
6. Multi-Agent Orchestrator
7. API Publique
8. CLI/Server (Point d'entrée)
"""

import os
import sys
import json
import re
import time
import logging
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path

# ============================================
# SECTION 1 : CONFIGURATION
# ============================================

# Lecture config depuis pyproject.toml (via environnement ou fichier)
CONFIG = {
    "server": {
        "port": int(os.getenv("IR_PORT", "8000")),
        "host": os.getenv("IR_HOST", "0.0.0.0")
    },
    "security": {
        "max_tokens": 2000,
        "rate_limit": 100,
        "rate_window": 60
    },
    "models": {
        "default_temperature": 0.7,
        "max_context": 4096
    }
}

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('ir_engine.log')
    ]
)

logger = logging.getLogger("IR-Engine")

# ============================================
# SECTION 2 : SECURITY GATEWAY
# ============================================

class SecurityError(Exception):
    """Exception levée pour violations sécurité"""
    pass


class SecurityGateway:
    """
    Gateway sécurité centralisé
    - Validation inputs
    - Rate limiting
    - Audit logging
    """
    
    _rate_limit_tracker: Dict[str, Dict[str, Any]] = {}
    
    @classmethod
    def validate_input(cls, text: str, metadata: Optional[Dict] = None) -> bool:
        """Valide input avant traitement"""
        metadata = metadata or {}
        
        # 1. Size check
        max_size = CONFIG["security"]["max_tokens"]
        if len(text) > max_size:
            raise SecurityError(f"Input exceeds {max_size} characters")
        
        # 2. Rate limiting
        if "client_id" in metadata:
            cls._check_rate_limit(metadata["client_id"])
        
        # 3. Pattern validation (optionnel - à adapter selon besoins)
        dangerous_patterns = ["__import__", "exec(", "eval("]
        for pattern in dangerous_patterns:
            if pattern in text:
                logger.warning(f"Dangerous pattern detected: {pattern}")
        
        return True
    
    @classmethod
    def _check_rate_limit(cls, client_id: str):
        """Rate limiting par client"""
        now = time.time()
        limit = CONFIG["security"]["rate_limit"]
        window = CONFIG["security"]["rate_window"]
        
        if client_id not in cls._rate_limit_tracker:
            cls._rate_limit_tracker[client_id] = {
                "count": 0,
                "reset_time": now + window
            }
        
        record = cls._rate_limit_tracker[client_id]
        
        if now > record["reset_time"]:
            record["count"] = 0
            record["reset_time"] = now + window
        
        if record["count"] >= limit:
            raise SecurityError(f"Rate limit exceeded for {client_id}")
        
        record["count"] += 1
    
    @classmethod
    def audit_log(cls, action: str, module: str, result: Dict, metadata: Optional[Dict] = None):
        """Log audit toutes actions"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "module": module,
            "success": result.get("success", False),
            "duration_ms": result.get("duration", 0),
            **(metadata or {})
        }
        logger.info(f"[AUDIT] {json.dumps(log_entry)}")


# ============================================
# SECTION 3 : BASE CLASSES
# ============================================

@dataclass
class AgentConfig:
    """Configuration d'un agent IA"""
    name: str
    model: str
    role: str
    specialty: str
    position: str = "Center"
    energy: str = "100%"


@dataclass
class WorldState:
    """État du monde RI"""
    mission: Dict[str, Any]
    agents: Dict[str, Dict[str, Any]]
    environment: Dict[str, Any]
    knowledge: Dict[str, List[str]]
    communication: List[str] = field(default_factory=list)
    event_sequence: List[str] = field(default_factory=list)
    time_event: int = 0


class IRModule(ABC):
    """Interface de base pour modules IR"""
    
    def __init__(self, name: str):
        self.name = name
        self.metrics = {
            "executions": 0,
            "errors": 0,
            "total_time_ms": 0
        }
    
    async def execute(self, input_data: Any, operation: str, metadata: Optional[Dict] = None) -> Dict:
        """Exécute opération avec métriques"""
        start = time.time()
        metadata = metadata or {}
        
        try:
            self.metrics["executions"] += 1
            result = await self._process(input_data, operation, metadata)
            duration = (time.time() - start) * 1000
            self.metrics["total_time_ms"] += duration
            
            return {
                "success": True,
                "result": result,
                "duration": duration
            }
        except Exception as e:
            self.metrics["errors"] += 1
            duration = (time.time() - start) * 1000
            logger.error(f"Error in {self.name}: {str(e)}")
            
            return {
                "success": False,
                "error": str(e),
                "duration": duration
            }
    
    @abstractmethod
    async def _process(self, input_data: Any, operation: str, metadata: Dict) -> Any:
        """Implémentation traitement spécifique"""
        pass
    
    def get_health(self) -> Dict:
        """Retourne métriques santé module"""
        avg_time = (
            self.metrics["total_time_ms"] / self.metrics["executions"]
            if self.metrics["executions"] > 0 else 0
        )
        
        return {
            "name": self.name,
            "status": "healthy",
            "metrics": self.metrics,
            "avg_time_ms": round(avg_time, 2)
        }


# ============================================
# SECTION 4 : REALITY ENGINE v3.0
# ============================================

class RealityEngineV3(IRModule):
    """
    Moteur RI v3.0 - Optimisé cognition LLM
    Gère état monde partagé et contexte hiérarchique
    """
    
    def __init__(self):
        super().__init__("RealityEngineV3")
        self.world_state = self._initialize_world()
    
    def _initialize_world(self) -> WorldState:
        """Initialise état monde par défaut"""
        return WorldState(
            mission={
                "title": "Anomalie Système Critique",
                "code": "#X7-THETA",
                "urgency": "HAUTE",
                "progress": 0,
                "max_steps": 3
            },
            agents={},
            environment={
                "location": "Salle Conférence Nexus",
                "time_event": 0,
                "layout": "Table ronde centrale, terminaux",
                "atmosphere": "Tension urgence palpable"
            },
            knowledge={
                "clues": ["Code #X7-THETA → module synchronisation temporelle"],
                "hypotheses": [],
                "actions_taken": []
            },
            event_sequence=[
                "Événement -3: Anomalie détectée système central",
                "Événement -2: Systèmes critiques mode dégradé",
                "Événement -1: Mission collaborative initiée",
                "Événement 0: Agents activés mission urgente"
            ]
        )
    
    def register_agent(self, agent_config: AgentConfig):
        """Enregistre nouvel agent dans monde"""
        self.world_state.agents[agent_config.name] = {
            "position": agent_config.position,
            "specialty": agent_config.specialty,
            "status": "Actif",
            "energy": agent_config.energy
        }
    
    def get_hierarchical_context(self, agent_name: str) -> str:
        """
        Génère contexte hiérarchique optimisé attention LLM
        Priorité: Info critique first
        """
        if agent_name not in self.world_state.agents:
            raise ValueError(f"Agent {agent_name} not registered")
        
        agent = self.world_state.agents[agent_name]
        others = {k: v for k, v in self.world_state.agents.items() if k != agent_name}
        
        # NIVEAU 1: ÉTAT CRITIQUE (haute priorité attention)
        critical = f"""
🚨 ÉTAT CRITIQUE - ATTENTION PRIORITAIRE

MISSION URGENTE: {self.world_state.mission['title']}
Code erreur: {self.world_state.mission['code']}
Urgence: {self.world_state.mission['urgency']}
Progression: {self.world_state.mission['progress']}/{self.world_state.mission['max_steps']} étapes

VOTRE IDENTITÉ: {agent_name}
Spécialité: {agent['specialty']}
Position: {agent['position']}
Statut: {agent['status']} | Énergie: {agent['energy']}
"""
        
        # NIVEAU 2: ÉQUIPE (contexte collaboratif)
        collab = "\n👥 ÉQUIPE PRÉSENTE (collaboration requise):\n"
        for name, data in others.items():
            collab += f"  • {name} - {data['specialty']}\n"
            collab += f"    Position: {data['position']} | Énergie: {data['energy']}\n"
        
        # NIVEAU 3: CONNAISSANCES
        knowledge = "\n🔍 CONNAISSANCES ÉQUIPE:\n"
        if self.world_state.knowledge['clues']:
            knowledge += "  Indices découverts:\n"
            for clue in self.world_state.knowledge['clues']:
                knowledge += f"    → {clue}\n"
        
        # NIVEAU 4: HISTORIQUE ÉVÉNEMENTS (temporalité relative)
        history = "\n📜 SÉQUENCE ÉVÉNEMENTS (ordre chronologique):\n"
        for event in self.world_state.event_sequence[-5:]:
            history += f"  {event}\n"
        
        # NIVEAU 5: COMMUNICATIONS
        comms = ""
        if self.world_state.communication:
            comms = "\n💬 COMMUNICATIONS RÉCENTES:\n"
            for msg in self.world_state.communication[-3:]:
                comms += f"  {msg}\n"
        
        # Assemblage final
        full_context = f"""{critical}
{'─'*70}
{collab}
{'─'*70}
{knowledge}
{'─'*70}
{history}
{comms}
{'─'*70}

🎯 ENVIRONNEMENT PHYSIQUE:
Lieu: {self.world_state.environment['location']}
Configuration: {self.world_state.environment['layout']}
Ambiance: {self.world_state.environment['atmosphere']}
"""
        return full_context
    
    def update_world(self, agent_name: str, action_summary: str, full_response: str):
        """Met à jour état monde après action agent"""
        self.world_state.time_event += 1
        event_id = self.world_state.time_event
        
        # Ajout événement
        event = f"Événement {event_id}: {agent_name} - {action_summary}"
        self.world_state.event_sequence.append(event)
        
        # Log communication
        comm_entry = f"[Evt {event_id}] {agent_name}: {action_summary}"
        self.world_state.communication.append(comm_entry)
        
        # Extraction hypothèses si présentes
        if "hypothèse" in full_response.lower() or "suppose" in full_response.lower():
            hypothesis = action_summary[:100]
            if hypothesis not in self.world_state.knowledge['hypotheses']:
                self.world_state.knowledge['hypotheses'].append(hypothesis)
    
    async def _process(self, input_data: Any, operation: str, metadata: Dict) -> Any:
        """Interface IRModule - dispatch opérations"""
        if operation == "get_context":
            return self.get_hierarchical_context(input_data)
        elif operation == "update":
            self.update_world(**input_data)
            return {"status": "updated"}
        elif operation == "register_agent":
            self.register_agent(input_data)
            return {"status": "registered"}
        else:
            raise ValueError(f"Unknown operation: {operation}")


# ============================================
# SECTION 5 : RESPONSE PROCESSOR
# ============================================

class ResponseProcessor(IRModule):
    """
    Nettoie réponses LLM pour maintenir immersion
    """
    
    def __init__(self):
        super().__init__("ResponseProcessor")
    
    @staticmethod
    def clean_artifacts(text: str, model_name: str) -> str:
        """Supprime artifacts spécifiques modèle"""
        cleaned = text
        
        # Deepseek reasoning tags
        if "deepseek" in model_name.lower():
            cleaned = re.sub(r'<think>.*?</think>', '', cleaned, flags=re.DOTALL)
        
        # Meta-commentary génériques
        meta_patterns = [
            r"(Je suis|I am) (un|une|a|an) (modèle|model|LLM|AI|assistant).*?[\.\n]",
            r"En tant qu(e |')(?:modèle|assistant|IA).*?[\.\n]",
            r"As (a|an) (language model|AI|assistant).*?[\.\n]"
        ]
        
        for pattern in meta_patterns:
            cleaned = re.sub(pattern, '', cleaned, flags=re.IGNORECASE)
        
        # Nettoyer espaces multiples
        cleaned = re.sub(r'\n\s*\n\s*\n', '\n\n', cleaned)
        return cleaned.strip()
    
    @staticmethod
    def validate_immersion(text: str) -> Dict[str, Any]:
        """Score immersion 0.0-1.0"""
        text_lower = text.lower()
        
        break_words = [
            'modèle de langage', 'language model', 'llm',
            'assistant ai', 'intelligence artificielle',
            'je ne peux pas vraiment', 'simulation',
            'en tant qu\'ia', 'as an ai'
        ]
        
        breaks_found = sum(1 for word in break_words if word in text_lower)
        penalty = min(breaks_found * 0.3, 1.0)
        score = max(0.0, 1.0 - penalty)
        
        return {
            'score': score,
            'breaks': breaks_found,
            'maintained': score >= 0.7
        }
    
    async def _process(self, input_data: Any, operation: str, metadata: Dict) -> Any:
        """Process response cleaning/validation"""
        if operation == "clean":
            model_name = metadata.get("model", "")
            return self.clean_artifacts(input_data, model_name)
        elif operation == "validate":
            return self.validate_immersion(input_data)
        else:
            raise ValueError(f"Unknown operation: {operation}")


# ============================================
# SECTION 6 : ORCHESTRATOR
# ============================================

class Orchestrator:
    """
    Coordonne modules IR et gère exécution pipeline
    """
    
    def __init__(self):
        self.reality_engine = RealityEngineV3()
        self.response_processor = ResponseProcessor()
        self.conversation_log: List[Dict] = []
    
    async def execute_agent_action(
        self,
        agent_name: str,
        task_prompt: str,
        model_client: Any,  # Groq client ou autre
        agent_config: AgentConfig
    ) -> Dict:
        """Exécute action agent complète avec pipeline IR"""
        
        # 1. Obtenir contexte RI
        context_result = await self.reality_engine.execute(
            agent_name,
            "get_context",
            {}
        )
        
        if not context_result["success"]:
            return context_result
        
        context = context_result["result"]
        
        # 2. Construire prompt complet
        system_prompt = f"""Vous êtes {agent_name}, android incarné spécialisé en {agent_config.role}.

DIRECTIVES COMPORTEMENTALES:
- Vous existez physiquement dans cet environnement
- Vous collaborez avec autres androids présents
- Répondez selon votre spécialité
- Agissez naturellement comme entité incarnée
- Ne mentionnez JAMAIS être un modèle de langage

Votre perception est immédiate et contextuelle."""
        
        full_prompt = f"""{context}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 TÂCHE ACTUELLE:
{task_prompt}

Répondez selon votre spécialité ({agent_config.specialty}) et votre perception de la situation.
"""
        
        # 3. Appel modèle (à implémenter selon client)
        # Ici placeholder - sera remplacé par vrai appel Groq/OpenAI
        raw_response = await self._call_model(
            model_client,
            system_prompt,
            full_prompt,
            agent_config.model
        )
        
        # 4. Post-processing
        clean_result = await self.response_processor.execute(
            raw_response,
            "clean",
            {"model": agent_config.model}
        )
        
        if not clean_result["success"]:
            return clean_result
        
        cleaned_response = clean_result["result"]
        
        # 5. Validation immersion
        immersion_result = await self.response_processor.execute(
            cleaned_response,
            "validate",
            {}
        )
        
        immersion = immersion_result["result"]
        
        # 6. Update world state
        action_summary = cleaned_response[:80] + "..." if len(cleaned_response) > 80 else cleaned_response
        
        await self.reality_engine.execute(
            {
                "agent_name": agent_name,
                "action_summary": action_summary,
                "full_response": cleaned_response
            },
            "update",
            {}
        )
        
        # 7. Log conversation
        self.conversation_log.append({
            "agent": agent_name,
            "model": agent_config.model,
            "task": task_prompt,
            "response": cleaned_response,
            "immersion_score": immersion['score'],
            "immersion_maintained": immersion['maintained'],
            "event": self.reality_engine.world_state.time_event
        })
        
        return {
            "success": True,
            "response": cleaned_response,
            "immersion": immersion
        }
    
    async def _call_model(self, client: Any, system: str, prompt: str, model: str) -> str:
        """
        Appel modèle LLM - À implémenter selon provider
        Placeholder ici
        """
        # TODO: Implémenter selon provider (Groq, OpenAI, etc.)
        # Pour l'instant retourne placeholder
        return f"[Response from {model}]"
    
    def get_health(self) -> Dict:
        """Health check global"""
        return {
            "status": "healthy",
            "modules": {
                "reality_engine": self.reality_engine.get_health(),
                "response_processor": self.response_processor.get_health()
            },
            "conversation_turns": len(self.conversation_log)
        }


# ============================================
# SECTION 7 : API PUBLIQUE
# ============================================

class IRAPI:
    """
    API publique Informatique Réalitaire
    """
    
    def __init__(self):
        self.orchestrator = Orchestrator()
        logger.info("IR API initialized")
    
    async def execute_scenario(self, scenario_config: Dict) -> Dict:
        """
        Exécute scénario multi-agent complet
        
        Args:
            scenario_config: {
                "agents": [AgentConfig, ...],
                "tasks": [{"agent": str, "task": str}, ...],
                "model_client": client object
            }
        """
        results = []
        
        # Register agents
        for agent_config in scenario_config["agents"]:
            await self.orchestrator.reality_engine.execute(
                agent_config,
                "register_agent",
                {}
            )
        
        # Execute tasks
        for task in scenario_config["tasks"]:
            agent_name = task["agent"]
            agent_config = next(
                a for a in scenario_config["agents"]
                if a.name == agent_name
            )
            
            result = await self.orchestrator.execute_agent_action(
                agent_name,
                task["task"],
                scenario_config["model_client"],
                agent_config
            )
            
            results.append(result)
        
        return {
            "success": True,
            "results": results,
            "health": self.orchestrator.get_health()
        }
    
    def get_health(self) -> Dict:
        """Health check API"""
        return self.orchestrator.get_health()


# ============================================
# SECTION 8 : CLI/SERVER
# ============================================

async def main():
    """Point d'entrée principal"""
    import argparse
    
    parser = argparse.ArgumentParser(description="IR Engine")
    parser.add_argument("--mode", choices=["server", "cli", "test"], default="cli")
    parser.add_argument("--port", type=int, default=CONFIG["server"]["port"])
    
    args = parser.parse_args()
    
    api = IRAPI()
    
    if args.mode == "server":
        logger.info("Starting IR server...")
        # TODO: Implémenter serveur HTTP (FastAPI, Flask, etc.)
        print(f"Server mode not yet implemented. Use --mode cli or --mode test")
    
    elif args.mode == "cli":
        logger.info("IR Engine ready - CLI mode")
        health = api.get_health()
        print(json.dumps(health, indent=2))
    
    elif args.mode == "test":
        logger.info("Running test scenario...")
        # TODO: Charger et exécuter scénario test
        print("Test mode - load test scenario from tests/")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())