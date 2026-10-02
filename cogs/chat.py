"""User-facing chat commands."""
import json
from discord.ext import commands
from utils.split import chunk_message
import config


def load_personas() -> dict:
    try:
        with open("data/personalities.json") as f:
            return json.load(f)
    except Exception:
        return {}


class Chat(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ask")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def ask(self, ctx: commands.Context, *, prompt: str):
        """Ask the AI something: !ask tell me a joke"""
        if config.ALLOWED_CHANNELS and ctx.channel.id not in config.ALLOWED_CHANNELS:
            return
        async with ctx.typing():
            reply = await self.bot.ai.chat(ctx.channel.id, f"{ctx.author.name}: {prompt}")
        for chunk in chunk_message(reply):
            await ctx.reply(chunk, mention_author=False)

    @commands.command(name="reset")
    async def reset(self, ctx: commands.Context):
        """Clear memory for this channel."""
        self.bot.ai.reset(ctx.channel.id)
        await ctx.send("Memory cleared for this channel. 🧹")

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.command(name="persona")
    async def persona(self, ctx: commands.Context, name: str = ""):
        """Switch personality: !persona roast"""
        personas = load_personas()
        if not name:
            await ctx.send(f"Available: {', '.join(personas.keys()) or 'none'}")
            return
        if name not in personas:
            await ctx.send(f"Unknown persona `{name}`. Try: {', '.join(personas.keys())}")
            return
        self.bot.ai.system_prompt = personas[name]
        self.bot.ai.reset(ctx.channel.id)
        await ctx.send(f"Persona → **{name}** 🎭")


async def setup(bot: commands.Bot):
    await bot.add_cog(Chat(bot))
