import logging
import os

LOG_PATH = os.path.join("logs", "bot.log")

logger = logging.getLogger("bot")
logger.setLevel(logging.INFO)

# Создаем директорию logs, если не существует
os.makedirs("logs", exist_ok=True)

file_handler = logging.FileHandler(LOG_PATH, encoding="utf-8")
console_handler = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s %(levelname)s [%(user_id)s][%(role)s]: %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


def log_message(user_id, role, text):
    logger.info(text, extra={"user_id": user_id, "role": role}) 