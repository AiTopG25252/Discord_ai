<div align="center">

# 🤖 Discord_ai

### *An AI that actually talks back.*

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![discord.py](https://img.shields.io/badge/discord.py-2.3%2B-5865F2?style=for-the-badge&logo=discord&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-10a37f?style=for-the-badge&logo=openai&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/AiTopG25252/Discord_ai?style=for-the-badge)

**Mention it. Reply to it. `!ask` it anything. It remembers context per-channel and answers like a real server member.**

[✨ Features](#-features) • [🚀 Setup](#-quick-start-3-minutes) • [💬 Commands](#-commands) • [🎭 Personalities](#-personalities) • [🐳 Docker](#-docker) • [❓ FAQ](#-faq)

</div>

---

```
  ____  _                       _      _    ___
 |  _ \(_)___  ___ ___  _ __ __| |    / \  |_ _|
 | | | | / __|/ __/ _ \| '__/ _` |   / _ \  | |
 | |_| | \__ \ (_| (_) | | | (_| |  / ___ \ | |
 |____/|_|___/\___\___/|_|  \__,_| /_/   \_\___|

        💬 chat  •  🧠 memory  •  🎭 personality
```

> `discord ai bot, uses ai to talk to users` — but polished: typing indicators, thread-aware replies, per-channel memory, personality presets, and rate-limit safety out of the box.

---

## ✨ Features

| | |
|---|---|
| 💬 **Talk naturally** | Mention `@AIBot`, reply to its message, or `!ask` — no slash setup needed |
| 🧠 **Remembers** | Last `MAX_HISTORY` messages per channel, `!reset` to wipe |
| 🎭 **Personalities** | Ship with `friendly`, `roast`, `shakespeare`, `coach` presets in `data/personalities.json` |
| ⚡ **Fast & safe** | Async OpenAI calls, per-channel lock, auto-split >2000 chars |
| 🔧 **Server controls** | `!toggle` per-guild, `ALLOWED_CHANNELS` allowlist |
| 📊 **Logs** | Structured logging in `utils/logger.py` |
| 🐳 **Deploy anywhere** | `Dockerfile` + `docker-compose.yml` included |

---

## 📸 Preview

> Drop your screenshots in `assets/` — these are placeholders wired in the README.

<p align="center">
  <img src="assets/demo-mention.png" width="700" alt="Bot replying to a mention — add your screenshot here" />
  <br><i>Mention → AI answer with context. (replace with your screenshot)</i>
</p>

<p align="center">
  <img src="assets/demo-ask.png" width="700" alt="!ask command demo" />
  <br><i>`!ask write a haiku about lag` → instant reply. (replace with your screenshot)</i>
</p>

---

## 🚀 Quick Start (3 minutes)

### 1️⃣ Get keys

- Discord bot token → https://discord.com/developers/applications → Bot → Reset Token
  - Turn ON **Privileged Gateway Intents → Message Content Intent**
- OpenAI key → https://platform.openai.com/api-keys

### 2️⃣ Install

```bash
git clone https://github.com/AiTopG25252/Discord_ai.git
cd Discord_ai
pip install -r requirements.txt
cp .env.example .env
# edit .env with your keys
python bot.py
```

### 3️⃣ Invite it

OAuth2 → URL Generator → check `bot` → permissions: `Send Messages`, `Read Message History`, `Embed Links`, `Attach Files` → open the URL.

### Minimal `.env`

```env
DISCORD_TOKEN=xxx
OPENAI_API_KEY=sk-xxx
OPENAI_MODEL=gpt-4o-mini
SYSTEM_PROMPT=You are a friendly, witty Discord assistant.
MAX_HISTORY=12
COMMAND_PREFIX=!
ALLOWED_CHANNELS=
```

---

## 💬 Commands

| Command | Example | What it does |
|---------|---------|--------------|
| `@AIBot <msg>` | `@AIBot what time is it in Tokyo?` | Chat with context |
| *reply to bot* | reply `and in London?` | Follows thread context |
| `!ask <msg>` | `!ask roast my aim` | Same as mention, prefix version |
| `!persona <name>` | `!persona roast` | Switch personality (see below) |
| `!reset` | `!reset` | Clear this channel's memory |
| `!ping` | `!ping` | `Pong! 42ms` health check |
| `!toggle` | `!toggle` | Admin-only: enable/disable server |

Long replies auto-split. Typing indicator shows while generating.

---

## 🎭 Personalities

Presets live in [`data/personalities.json`](data/personalities.json):

```json
{
  "friendly": "You are a friendly, witty Discord assistant...",
  "roast": "You are a savage but playful roaster...",
  "shakespeare": "You speak like Shakespeare..."
}
```

Switch live: `!persona roast` · `!persona friendly`
Add your own in the JSON, no restart logic needed — see [`docs/PERSONALITIES.md`](docs/PERSONALITIES.md) + [`examples/custom_personality.py`](examples/custom_personality.py).

---

## 🗂️ Project Structure

```
Discord_ai/
├── bot.py                    # entry point, mention/reply router
├── config.py                 # env loader
├── ai_client.py              # OpenAI wrapper + history
├── cogs/
│   ├── chat.py               # !ask !reset !ping !persona
│   ├── admin.py              # !toggle
│   ├── fun.py                # !joke !roll (dummy fun cmds)
│   └── events.py             # on_join welcome, logging
├── utils/
│   ├── split.py              # 2000-char chunker
│   ├── embeds.py             # pretty embed builder
│   ├── logger.py             # logging setup
│   └── rate_limit.py         # per-user cooldown
├── data/
│   └── personalities.json    # persona presets
├── docs/
│   ├── CONFIGURATION.md
│   ├── DEPLOYMENT.md
│   └── PERSONALITIES.md
├── examples/
│   ├── custom_personality.py
│   └── embed_reply.py
├── tests/
│   ├── test_split.py
│   └── test_config.py
├── assets/                   # screenshots + banner.svg
├── .github/workflows/ci.yml  # lint + tests
├── Dockerfile
├── docker-compose.yml
├── Makefile
└── requirements.txt
```

---

## ⚙️ Configuration

Full reference in [`docs/CONFIGURATION.md`](docs/CONFIGURATION.md):

| Var | Default | Meaning |
|-----|---------|---------|
| `DISCORD_TOKEN` | *required* | Discord bot token |
| `OPENAI_API_KEY` | *required* | OpenAI key |
| `OPENAI_MODEL` | `gpt-4o-mini` | Try `gpt-4o`, `gpt-3.5-turbo` |
| `SYSTEM_PROMPT` | friendly | Overridden by `!persona` |
| `MAX_HISTORY` | `12` | 0 = no memory, 30 = long memory (more tokens) |
| `COMMAND_PREFIX` | `!` | Prefix |
| `ALLOWED_CHANNELS` | empty = all | e.g. `123,456` |
| `COOLDOWN_SECONDS` | `3` | Per-user cooldown |

---

## 🐳 Docker

```bash
docker build -t discord-ai .
docker run --env-file .env discord-ai

# or compose (auto-restart):
docker compose up -d --build
docker compose logs -f
```

See [`docs/DEPLOYMENT.md`](docs/DEPLOYMENT.md) for Railway / Replit / VPS notes.

---

## 🧪 Dev

```bash
pip install -r requirements-dev.txt
pytest -q
ruff check .
python bot.py
```

CI runs `ruff + pytest` on every push — see [`.github/workflows/ci.yml`](.github/workflows/ci.yml).

---

## ❓ FAQ

<details>
<summary><b>Bot doesn't respond to mentions?</b></summary>

Enable **Message Content Intent** in the Developer Portal → Bot, then restart. Also check `ALLOWED_CHANNELS` isn't blocking the channel.
</details>

<details>
<summary><b>How do I make it funnier / meaner?</b></summary>

Edit `SYSTEM_PROMPT` in `.env` or use `!persona roast`. Full guide: `docs/PERSONALITIES.md`.
</details>

<details>
<summary><b>Does memory persist after restart?</b></summary>

No — in-memory only. Swap `ai_client.py` deque for SQLite/Redis if you need persistence (stub in `docs/DEPLOYMENT.md`).
</details>

<details>
<summary><b>401 Unauthorized?</b></summary>

Bad `DISCORD_TOKEN`. Reset it in the portal, update `.env`, restart.
</details>

---

## 🤝 Contributing

PRs welcome. `make lint && make test` before pushing. See [CONTRIBUTING.md](CONTRIBUTING.md).

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) — `v1.1.0` adds `!persona`, embeds, cooldowns.

## 📄 License

MIT — [LICENSE](LICENSE). Not affiliated with Discord or OpenAI.
