"""Pretty embeds for AI replies."""
import discord

def ai_embed(title: str, description: str) -> discord.Embed:
    e = discord.Embed(title=title, description=description[:4000], color=0x5865F2)
    e.set_footer(text="Discord_ai • gpt")
    return e
