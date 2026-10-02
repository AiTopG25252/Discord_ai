# Personalities

Presets in `data/personalities.json`. Each key is a persona name, value is a system prompt.

Add one:
```json
{
  "pirate": "You speak like a pirate. Arrr in every reply."
}
```

Then in Discord: `!persona pirate`

Tips:
- Keep prompts under ~200 words, end with output constraints ("under 400 words", "use emojis sparingly").
- See `examples/custom_personality.py` for loading a persona in code.
