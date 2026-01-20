# точка входа в бд

from sqlalchemy import create_engine, text

from app.core.config import settings

engine = create_engine(
    settings.database_url,
    # пинг для проверки активности соединения
    pool_pre_ping=True,
)

# функция для проверки доступности бд
def check_db() -> None:
    with engine.connect() as conn:
        # простой запрос к бд для проверки ее работы
        conn.execute(text("SELECT 1"))