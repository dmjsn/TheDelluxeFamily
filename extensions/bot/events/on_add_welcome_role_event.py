from discord.ext import commands
from discord import Interaction
from config import constants
from services.add_welcome_role import AddWelcomeRole

class OnAddWelcomeRoleEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.service = AddWelcomeRole(self.bot)

    @commands.Cog.listener()
    async def on_interaction(self, interaction: Interaction):
        if not interaction.data.get('custom_id'):
            return

        try:
            custom_id = interaction.data['custom_id']
            guild = interaction.guild
            member = interaction.user

            if not guild or not member:
                return

            role_id = None

            if custom_id == 'guest_role':
                role_id = constants.ROLES_IDS['guest_role']

            if custom_id == 'farm_role':
                role_id = constants.ROLES_IDS['contractor_role']

            if custom_id == 'player_role':
                role_id = constants.ROLES_IDS['player_role']

            if role_id is None:
                return

            await self.service.addRole(member, role_id)

            await interaction.response.send_message('Молодец! Ты понял(а) как нажимать на кнопки', ephemeral=True)

        except Exception as e:
            print(f"Ошибка обработки взаимодействия: {e}")

async def setup(bot):
    await bot.add_cog(OnAddWelcomeRoleEvent(bot))
