from discord import Embed

class WelcomeMessageEmbed(Embed):
    def __init__(self):
        super().__init__(
            title="Добро пожаловать!",
            description="Мы рады видеть вас на сервере",
            color=0x00ff00
        )
        self.set_thumbnail(url="https://i.imgur.com/example.png")
        self.add_field(name="Правила", value="Прочитайте #правила")
