from fastapi import FastAPI
from fastapi_k8s.config import settings
from fastapi_k8s.api.book import router as book_router

app = FastAPI(title=settings.APP_NAME)

app.include_router(book_router, prefix="/books")
