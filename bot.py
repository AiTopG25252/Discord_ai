"""Discord AI bot entry point."""
import asyncio
import discord
from discord.ext import commands

import config
from ai_client import AIClient
from utils.split import chunk_message
from utils.logger import setup_logging

setup_logging()


def allowed_in_channel(channel_id: int) -> bool:
    if not config.ALLOWED_CHANNELS:
        return True
    return channel_id in config.ALLOWED_CHANNELS


def build_bot() -> commands.Bot:
    intents = discord.Intents.default()
    intents.message_content = True  # enable in portal too

    bot = commands.Bot(command_prefix=config.COMMAND_PREFIX, intents=intents)
    bot.ai = AIClient(
        api_key=config.OPENAI_API_KEY,
        model=config.OPENAI_MODEL,
        system_prompt=config.SYSTEM_PROMPT,
        max_history=config.MAX_HISTORY,
    )

    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user} ({bot.user.id})")

    @bot.event
    async def on_message(message: discord.Message):
        if message.author.bot:
            return

        # Let prefix commands run first
        await bot.process_commands(message)

        # Already handled as command?
        ctx = await bot.get_context(message)
        if ctx.valid:
            return

        if not allowed_in_channel(message.channel.id):
            return

        bot_mentioned = bot.user in message.mentions
        is_reply_to_bot = (
            message.reference is not None
            and message.reference.resolved is not None
            and getattr(message.reference.resolved, "author", None) == bot.user
        )

        if not (bot_mentioned or is_reply_to_bot):
            return

        prompt = message.content
        # strip mention markup <@12345>
        for m in message.mentions:
            prompt = prompt.replace(f"<@{m.id}>", "").replace(f"<@!{m.id}>", "")
        prompt = prompt.strip() or "Hello!"

        async with message.channel.typing():
            reply = await bot.ai.chat(
                channel_id=message.channel.id,
                user=f"{message.author.name}: {prompt}",
            )
        for chunk in chunk_message(reply):
            await message.reply(chunk, mention_author=False)

    return bot


async def main():
    if not config.DISCORD_TOKEN or not config.OPENAI_API_KEY:
        raise SystemExit("Missing DISCORD_TOKEN or OPENAI_API_KEY. Copy .env.example to .env first.")
    bot = build_bot()
    # load cogs
    await bot.load_extension("cogs.chat")
    await bot.load_extension("cogs.admin")
    await bot.load_extension("cogs.fun")
    await bot.load_extension("cogs.events")
    async with bot:
        await bot.start(config.DISCORD_TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
