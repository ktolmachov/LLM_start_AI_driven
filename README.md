# LLM Start AI-driven Assistant

# Домашнее задание после интенсива LLM Start

Репозиторий содержит выполнение домашнего задания после интенсива LLM Start.

**Студент:** Константин Толмачев
**Статус:** В процессе

Краткое описание: решение включает разработку Telegram-бота-ассистента на базе LLM для консультаций клиентов по услугам компании.


Telegram-бот-ассистент на базе LLM для консультаций клиентов по услугам компании. Проект разработан в рамках домашнего задания после интенсива LLM Start.

## Возможности

- 💬 Обработка текстовых сообщений через Telegram
- 🤖 Интеграция с LLM через OpenRouter API
- 📝 Сохранение контекста диалога
- ⚙️ Гибкая конфигурация через .env
- 📊 Подробное логирование работы

## Быстрый старт

1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/LLM_start_AI_driven.git
cd LLM_start_AI_driven
```

2. Создайте и активируйте виртуальное окружение:

Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
# или
uv pip install -r requirements.txt
```

4. Создайте файл `.env` с необходимыми переменными окружения:
```env
TELEGRAM_TOKEN=your_telegram_bot_token
OPENROUTER_API_KEY=your_openrouter_api_key
MODEL_NAME=your_preferred_model
SYSTEM_PROMPT=your_system_prompt
```

5. Запустите бота:
```bash
python main.py
```

## Структура проекта

```
LLM_start_AI_driven/
├── bot.py           # Telegram бот и обработка сообщений
├── config.py        # Загрузка конфигурации
├── llm_client.py    # Взаимодействие с LLM API
├── logger.py        # Настройка логирования
├── main.py          # Точка входа приложения
├── doc/            # Документация
│   ├── product_idea.md  # Описание продукта
│   ├── tasklist.md      # План разработки
│   ├── vision.md        # Техническое видение
│   └── conventions.md   # Правила разработки
└── tests/          # Тесты
    ├── test_bot.py
    ├── test_config.py
    └── test_llm.py
```

## Разработка

Проект следует принципам:
- KISS (Keep It Simple, Stupid)
- Функциональное программирование
- Минимальный код без избыточных абстракций
- Модульность с четким разграничением ответственности

Подробные правила разработки описаны в [doc/conventions.md](doc/conventions.md).

## Тестирование

Запуск тестов:
```bash
pytest
```

## Документация

- [Product Idea](doc/product_idea.md) - описание продукта
- [Vision](doc/vision.md) - техническое видение
- [Conventions](doc/conventions.md) - правила разработки
- [Tasklist](doc/tasklist.md) - план разработки

## Лицензия

MIT

## Автор

Константин Толмачев

