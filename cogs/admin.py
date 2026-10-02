"""Simple per-guild toggle."""
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.disabled_guilds: set[int] = set()

    @commands.command(name="toggle")
    @commands.has_permissions(manage_guild=True)
    async def toggle(self, ctx: commands.Context):
        """Enable/disable bot responses in this server."""
        gid = ctx.guild.id if ctx.guild else 0
        if gid in self.disabled_guilds:
            self.disabled_guilds.remove(gid)
            await ctx.send("AI enabled here. ✅")
        else:
            self.disabled_guilds.add(gid)
            await ctx.send("AI disabled here. ❌")


async def setup(bot: commands.Bot):
    await bot.add_cog(Admin(bot))
