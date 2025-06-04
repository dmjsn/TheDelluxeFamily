from typing import List, Dict

class Settings:
    PREFIXES: List[str] = ["!"]

    EXTENSIONS: List[str] = [
        # 'admin.Commands',
        # 'admin.Events'
        'admin.commends.create_welcome_message',
        'bot.events.on_add_welcome_role_event'
    ]

    INTENTS: Dict[str, bool] = {
        'messages': True,
        'guilds': True,
        'members': True,
        'voice_states': True,
        'message_content': True,
    }
