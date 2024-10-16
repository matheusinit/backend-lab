from fastapi import FastAPI
from app.config import settings
from app.api.book import router as book_router

app = FastAPI(title=settings.APP_NAME)

app.include_router(book_router, prefix="/books")
