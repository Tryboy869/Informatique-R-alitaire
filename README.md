# Immersive Context Engine for Multi-Agent LLM Scenarios

A lightweight framework for creating embodied multi-agent scenarios without expensive compute or physics simulation.

## What is this?

Instead of using game engines or physics simulators to test multi-agent AI behavior, this framework structures narrative context hierarchically to help LLMs maintain consistent embodied perspectives in shared simulated environments.

**Core idea:** Hierarchical context structure + state injection + artifact cleaning = better role-play coherence and multi-agent interaction.

### How it differs from normal prompting

**Normal approach:**
```
"You are ALPHA-7, a scientific android. You are in a lab with BETA-3 and GAMMA-5. 
There's a desk, a screen, and a window. You see Dr. Chen working at a terminal."
```

**Our approach:**
```
[CRITICAL INFO - HIGHEST PRIORITY]
Mission: Anomaly #X7-THETA
Your role: ALPHA-7 (scientific analysis)
Team: BETA-3 (coordination), GAMMA-5 (problem-solving)

[ENVIRONMENT]
Location: Nexus Conference Room
Objects: desk, screen, window
Agents: Dr. Chen, AIDE-7

[EVENT SEQUENCE - RELATIVE TIME]
Event 0: Anomaly detected
Event +1: Mission initiated
```

Hierarchical structure helps LLMs allocate attention better. Event sequences avoid temporal confusion. Complete state injection compensates for LLM statelessness.

## Technical approach

### 5 Core Modules

1. **RealityEngineV3** - Manages world state and hierarchical context
2. **ResponseProcessor** - Removes model artifacts, validates immersion
3. **Orchestrator** - Coordinates execution pipeline
4. **SecurityGateway** - Input validation, rate limiting, audit logging
5. **IRAPI** - Public API interface

### How it works

```python
orchestrator = Orchestrator()

agent = AgentConfig(
    name="ALPHA-7",
    model="llama-3.3-70b-versatile",
    specialty="Scientific analysis"
)

orchestrator.reality_engine.register_agent(agent)

result = await orchestrator.execute_agent_action(
    agent_name="ALPHA-7",
    task_prompt="Analyze error #X7-THETA",
    model_client=groq_client,
    agent_config=agent
)

print(result["response"])
print(f"Immersion: {result['immersion']['score']*100:.0f}%")
```

## Testing Results

We tested 3 LLM models (Llama-3.3-70b, Gemma2-9b-it, Deepseek-r1-distill) on multi-agent crisis scenarios.

**Observation:** Hierarchical context improved agent coherence vs. flat prompting. Agents maintained consistent character and showed better inter-agent coordination.

**Results:**
- v2.0 (initial): 68.3% average
- v3.0 (with post-processing): ~95-97% average

**Important caveat:** Immersion scoring is subjective aggregation based on keyword detection, not rigorous metrics.

## Installation

```bash
git clone https://github.com/Tryboy869/informatique-realitaire.git
cd informatique-realitaire

pip install -r requirements.txt

export GROQ_API_KEY=your_key_here

python app.py --mode cli
```

### Requirements

- Python 3.9+
- Groq API key (or other LLM provider)
- ~50MB disk space

## Public API

### Live API Access

Base URL: `https://ri-api-plt9.onrender.com`

Health check: `https://ri-api-plt9.onrender.com/health`

### Quick Start

Create your first IR world:

```bash
curl -X POST https://ri-api-plt9.onrender.com/api/v1/world/create \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Research Laboratory",
    "objects": [
      {"id": "desk", "type": "furniture", "state": "stable"},
      {"id": "screen", "type": "display", "state": "active"}
    ],
    "metadata": {
      "description": "A modern research lab environment"
    }
  }'
```

Response:
```json
{
  "world_id": "w_abc123...",
  "created_at": "2025-10-11T18:00:00Z"
}
```

### Get World Context

```bash
curl https://ri-api-plt9.onrender.com/api/v1/world/{world_id}/context
```

Response includes formatted context ready for your AI.

### Use with Your AI

```python
import requests
from openai import OpenAI  # or Anthropic, Groq, etc.

# Get IR world context
world_context = requests.get(
    "https://ri-api-plt9.onrender.com/api/v1/world/w_abc123.../context"
).json()["formatted_context"]

# Send to your AI
client = OpenAI(api_key="YOUR_KEY")
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": world_context},
        {"role": "user", "content": "Describe what you perceive."}
    ]
)

print(response.choices[0].message.content)
```

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | API health check |
| POST | `/api/v1/world/create` | Create new world |
| GET | `/api/v1/world/{id}/context` | Get formatted context |
| POST | `/api/v1/world/{id}/update` | Update world state |
| GET | `/api/v1/world/{id}/metrics` | Get world metrics |
| GET | `/api/v1/worlds` | List all worlds |
| DELETE | `/api/v1/world/{id}` | Delete world |

### API Limits (Free Tier)

- Rate limit: 100 req/min
- Max objects per world: 100
- Max worlds: 1000
- Retention: 24h for inactive worlds

For enterprise limits, contact us.

### API Examples

**Multi-agent simulation:**

```bash
# Create shared world
WORLD_ID=$(curl -s -X POST https://ri-api-plt9.onrender.com/api/v1/world/create \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Collaborative Office",
    "objects": [
      {"id": "whiteboard", "type": "tool"},
      {"id": "meeting_table", "type": "furniture"}
    ]
  }' | jq -r '.world_id')

# Get context for Agent 1
CONTEXT=$(curl -s "https://ri-api-plt9.onrender.com/api/v1/world/$WORLD_ID/context" | jq -r '.formatted_context')

# Update world based on Agent 1's action
curl -X POST "https://ri-api-plt9.onrender.com/api/v1/world/$WORLD_ID/update" \
  -H "Content-Type: application/json" \
  -d '{"changes": {"whiteboard.content": "Agent 1 wrote ideas"}}'

# Agent 2 gets updated context
curl "https://ri-api-plt9.onrender.com/api/v1/world/$WORLD_ID/context"
```

**Dynamic environment:**

```bash
curl -X POST "https://ri-api-plt9.onrender.com/api/v1/world/$WORLD_ID/update" \
  -d '{
    "changes": {
      "objects[0].state": "filled",
      "objects[0].temperature": "increasing",
      "metadata.description": "Chemical reaction in progress"
    }
  }'
```

## Architecture

```
informatique-realitaire/
├── app.py                    # Main engine (5 modules)
├── requirements.txt
├── tests/
│   ├── test_1_single_agent/
│   │   ├── script.py
│   │   └── logs.txt
│   ├── test_2_multi_agent_v2/
│   │   ├── script.py
│   │   └── logs.txt
│   └── test_3_multi_agent_v3/
│       ├── script.py
│       └── logs.txt
├── examples/
│   └── basic_usage.py
├── docs/
│   ├── architecture.md
│   └── api.md
└── README.md
```

## Limitations

- **Not a physics engine** - No real physics, just narrative context
- **Not a game engine** - Not optimized for real-time rendering
- **Subjective immersion scoring** - Based on keyword detection, not rigorous measurement
- **Small test sample** - N~8-10 interactions per model
- **No peer review** - Exploratory work, not peer-reviewed research
- **Post-processing bias** - Artifact removal removes data, introduces selection bias
- **Works best for narrative scenarios** - Multi-agent role-play, not general LLM tasks

## What this is NOT

- A breakthrough in AI (it's prompt engineering)
- A solution to alignment or safety
- A replacement for physics simulation
- A way to make LLMs "truly embodied"

It's a tool for better prompt engineering in specific scenarios.

## Use Cases

- Multi-agent role-play testing
- Safety research with embodied contexts
- LLM coordination studies
- Interactive narrative with AI agents
- Educational simulations

## License

MIT License - See LICENSE file

## Citation

If you use this in research:

```bibtex
@misc{anzize2025context_engine,
  title={Immersive Context Engine for Multi-Agent LLM Scenarios},
  author={Anzize, Daouda Abdoul},
  year={2025},
  howpublished={\url{https://github.com/Tryboy869/informatique-realitaire}}
}
```

## Contact

Daouda Abdoul Anzize
- GitHub: @Tryboy869
- Email: nexusstudio100@gmail.com

## Contributing

Contributions welcome. Please see CONTRIBUTING.md

---

Questions? Open an issue or contact us.