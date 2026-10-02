"""Join/leave logging + welcome."""
from discord.ext import commands
import logging

log = logging.getLogger("bot.events")

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        log.info(f"Joined guild: {guild.name} ({guild.id})")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"Slow down! Try again in {error.retry_after:.1f}s.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You need Manage Server to do that.")

async def setup(bot):
    await bot.add_cog(Events(bot))
