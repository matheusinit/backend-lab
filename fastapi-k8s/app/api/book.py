import uuid

from fastapi.routing import APIRouter
from fastapi import HTTPException
from sqlmodel import Session

from sqlmodel import select

from app.dtos import BookCreate, BookResponse, BookUpdate, Message
from app.models import Book
from app.database import engine


router = APIRouter()


@router.get("/", response_model=list[BookResponse])
def get_books():
    """
    Get all books in the database
    """

    session = Session(engine)

    statement = select(Book)

    books = session.exec(statement).all()

    session.close()

    return books


@router.post("/", response_model=BookResponse)
def create_book(book_in: BookCreate):
    """
    Create a new book in the database
    """

    book = Book(
        name=book_in.name,
        description=book_in.description,
    )

    session = Session(engine)

    session.add(book)
    session.commit()
    session.refresh(book)
    return book


@router.get("/{id}", response_model=BookResponse)
def get_book_by_id(id: uuid.UUID):
    """
    Get a book by id
    """

    session = Session(engine)

    statement = select(Book).where(Book.id == id)

    book = session.exec(statement).first()

    session.close()

    return book


@router.put('/{id}', response_model=BookResponse)
def update_book_by_id(id: uuid.UUID, book_in: BookUpdate):
    """
    Update a book by id
    """

    session = Session(engine)

    statement = select(Book).where(Book.id == id)

    book = session.exec(statement).first()

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    if book_in.name is not None:
        book.name = book_in.name
    if book_in.description is not None:
        book.description = book_in.description

    session.add(book)
    session.commit()

    session.refresh(book)

    session.close()

    return book


@router.delete('/{id}', response_model=Message)
def delete_book_by_id(id: uuid.UUID):
    """
    Delete a book by id
    """

    session = Session(engine)

    statement = select(Book).where(Book.id == id)

    book = session.exec(statement).first()

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    session.delete(book)

    session.commit()

    return Message(message="Book deleted successfully")
