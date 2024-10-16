from sqlmodel import create_engine
from app.config import settings


def build_uri():
    db_name = settings.DATABASE_NAME
    password = settings.DATABASE_PASSWORD
    host = settings.DATABASE_HOST
    port = settings.DATABASE_PORT
    user = settings.DATABASE_USERNAME

    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"


uri = build_uri()
engine = create_engine(uri, echo=True)
