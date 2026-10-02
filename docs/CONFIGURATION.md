# Configuration

All settings come from environment / `.env`. See `.env.example`.

| Var | Default | Notes |
|-----|---------|-------|
| `DISCORD_TOKEN` | required | Discord Developer Portal → Bot → Token |
| `OPENAI_API_KEY` | required | platform.openai.com/api-keys |
| `OPENAI_MODEL` | `gpt-4o-mini` | `gpt-4o`, `gpt-3.5-turbo` also work |
| `SYSTEM_PROMPT` | friendly | Startup persona, `!persona` overrides at runtime |
| `MAX_HISTORY` | `12` | Per-channel deque size. Higher = more tokens |
| `COMMAND_PREFIX` | `!` | e.g. `?` |
| `ALLOWED_CHANNELS` | empty | CSV ids, e.g. `123456789,987654321` |
| `COOLDOWN_SECONDS` | `3` | Per-user cooldown for `!ask` |

Enable **Message Content Intent** or mentions/prefix won't fire.
