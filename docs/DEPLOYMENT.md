# Deployment

## Local
```bash
pip install -r requirements.txt
cp .env.example .env
python bot.py
```

## Docker
```bash
docker build -t discord-ai .
docker run --env-file .env --restart unless-stopped discord-ai
```

## Compose
```bash
docker compose up -d --build
docker compose logs -f
```

## Railway / VPS
- Set env vars in dashboard (same names as `.env`).
- Start command: `python bot.py`
- Need persistent memory? Replace `ai_client.py` deque with SQLite — history dict is isolated per channel so it's a 20-line swap.

## Troubleshooting
- `401 Unauthorized` → bad DISCORD_TOKEN
- `Privileged intent` error → enable Message Content Intent
- `RateLimitError` from OpenAI → lower MAX_HISTORY / add cooldown
