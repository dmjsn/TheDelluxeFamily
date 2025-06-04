import discord
from discord.ui import View, Button

class WelcomeMessageView(View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(Button(
            style=discord.ButtonStyle.primary,
            label='🎮 Пришел погостить',
            custom_id='guest_role'
        ))

        self.add_item(Button(
            style=discord.ButtonStyle.primary,
            label='🎮 Пришел сделать контракты',
            custom_id='farm_role'
        ))

        self.add_item(Button(
            style=discord.ButtonStyle.secondary,
            label='🎮 Пришел поиграть в другие игры',
            custom_id='player_role'
        ))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        return True
