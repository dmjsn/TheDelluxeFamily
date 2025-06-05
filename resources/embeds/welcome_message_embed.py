from discord import Embed

class WelcomeMessageEmbed(Embed):
    def __init__(self):
        super().__init__(
            title="Добро пожаловать!",
            description="Тут должно быть приветственное сообщение, но Кенси не написала его, во всем винить ее.",
            color=0x00ff00
        )
