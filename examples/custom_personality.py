"""Load a custom persona without touching .env."""
import json

with open("data/personalities.json") as f:
    PERSONAS = json.load(f)

# pick one and pass as system_prompt to AIClient
print(PERSONAS["roast"])
