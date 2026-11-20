from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

books = [
    {"id": 1, "title": "Python Basics", "author": "John", "available": True},
    {"id": 2, "title": "Learn FastAPI", "author": "David", "available": False},
    {"id": 3, "title": "Data Structures", "author": "Smith", "available": True}
]


class BookCreate(BaseModel):
    id: int
    title: str
    author: str
    available: bool


# GET all books with optional available filter
@app.get("/books")
def get_books(available: bool = None):
    if available is not None:
        return [book for book in books if book["available"] == available]

    return books


# GET book statistics
@app.get("/books/stats")
def book_stats():
    total = len(books)
    available = sum(1 for book in books if book["available"])

    return {
        "total": total,
        "available": available
    }


# GET book by ID
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(status_code=404, detail="Book not found")


# POST add a new book
@app.post("/books")
def add_book(book: BookCreate):
    for existing_book in books:
        if existing_book["title"].lower() == book.title.lower():
            raise HTTPException(
                status_code=400,
                detail="Book already exists"
            )

    new_book = book.model_dump()
    books.append(new_book)

    return {
        "message": "Book added successfully",
        "book": new_book
    }