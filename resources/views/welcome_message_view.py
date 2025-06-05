import discord
from discord.ui import View, Button

class WelcomeMessageView(View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(Button(
            style=discord.ButtonStyle.primary,
            label='ㅤㅤ☕ Пришел погоститьㅤㅤ',
            custom_id='guest_role',
            row=0,
        ))

        self.add_item(Button(
            style=discord.ButtonStyle.primary,
            label='📝 Пришел сделать контракты',
            custom_id='farm_role',
            row=0
        ))

        self.add_item(Button(
            style=discord.ButtonStyle.secondary,
            label='ㅤㅤㅤㅤㅤㅤㅤ🎮 Пришел поиграть в другие игрыㅤㅤㅤㅤㅤㅤㅤㅤ',
            custom_id='player_role',
            row=1
        ))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        return True
