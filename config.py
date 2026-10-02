"""Central config loaded from environment / .env."""
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN: str = os.getenv("DISCORD_TOKEN", "")
OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
SYSTEM_PROMPT: str = os.getenv(
    "SYSTEM_PROMPT",
    "You are a friendly, witty Discord assistant. Keep replies under 400 words unless asked for more.",
)
MAX_HISTORY: int = int(os.getenv("MAX_HISTORY", "12"))
COMMAND_PREFIX: str = os.getenv("COMMAND_PREFIX", "!")
COOLDOWN_SECONDS: float = float(os.getenv("COOLDOWN_SECONDS", "3"))

_raw_allowed = os.getenv("ALLOWED_CHANNELS", "").strip()
if _raw_allowed:
    ALLOWED_CHANNELS = {int(x.strip()) for x in _raw_allowed.split(",") if x.strip().isdigit()}
else:
    ALLOWED_CHANNELS = set()
