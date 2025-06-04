discord-bot/
├── 📁 core/                  # Ядро бота
│   ├── __init__.py          # Инициализация
│   ├── bot.py               # Основной класс бота
│   ├── config.py            # Настройки
│   └── logger.py            # Логирование
│
├── 📁 extensions/            # Функциональные модули
│   ├── 📁 admin/            # Админ-команды
│   │   ├── __init__.py
│   │   ├── commands.py
│   │   └── events.py
│   │
│   ├── 📁 moderation/       # Модерация
│   ├── 📁 music/            # Музыка
│   ├── 📁 economy/          # Экономика
│   └── ...                  # Другие модули
│
├── 📁 services/             # Сервисные классы
│   ├── database.py          # Работа с БД
│   ├── api_client.py        # Внешние API
│   └── cache.py             # Кеширование
│
├── 📁 models/               # Модели данных
│   ├── user.py              # Пользователи
│   ├── guild.py             # Серверы
│   └── ...                  
│
├── 📁 ui/                   # Пользовательский интерфейс
│   ├── buttons.py           # Кнопки
│   ├── modals.py            # Модальные окна
│   └── selectors.py         # Меню выбора
│
├── 📁 utils/                # Вспомогательные утилиты
│   ├── decorators.py        # Декораторы
│   ├── converters.py        # Конвертеры
│   └── helpers.py           # Хелперы
│
├── 📁 assets/               # Ресурсы
│   ├── 📁 images/           # Изображения
│   └── 📁 locales/          # Локализации
│
├── 🐍 main.py               # Точка входа
├── 📄 .env                  # Переменные окружения
└── 📄 requirements.txt      # Зависимости