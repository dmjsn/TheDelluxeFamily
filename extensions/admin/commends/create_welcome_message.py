from discord.ext import commands
from core import bot
from config import constants
from resources.embeds import welcomeMessageEmbed
from resources.views import welcomeMessageView

class CreateWelcomeMessage(commands.Cog):
    def __init__(self, bot: bot):
        self.bot = bot

    @commands.command(name="create-welcome-message")
    async def createWelcomeMessage(self, ctx: commands.Context):
        """Отправить сообщение с выбором роли в welcome-канал"""

        welcomeChannel = self.bot.get_channel(constants.CHANNEL_IDS['welcome_channel_id'])
        infoChannel = self.bot.get_channel(constants.INFO_CHANNEL_ID)

        if not welcomeChannel:
            return await infoChannel.send("❌ Канал не найден!")

        await welcomeChannel.send(embed=welcomeMessageEmbed, view=welcomeMessageView)
        await infoChannel.send("✅ Сообщение отправлено!")


async def setup(bot):
    await bot.add_cog(CreateWelcomeMessage(bot))
