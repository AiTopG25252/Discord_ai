"""Dummy fun commands to make the bot feel alive."""
import random
from discord.ext import commands

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "I would tell you a UDP joke, but you might not get it.",
    "My ping is faster than your comeback.",
]

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="joke")
    async def joke(self, ctx):
        await ctx.send(random.choice(JOKES))

    @commands.command(name="roll")
    async def roll(self, ctx, sides: int = 100):
        sides = max(2, min(sides, 1000))
        await ctx.send(f"🎲 {ctx.author.mention} rolled **{random.randint(1, sides)}** (1-{sides})")

async def setup(bot):
    await bot.add_cog(Fun(bot))
