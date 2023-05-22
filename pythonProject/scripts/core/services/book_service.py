from fastapi import APIRouter
from schemas.models import Email
from scripts.core.handlers.book_handler import *
from scripts.core.handlers.email_handler import send_email

app = APIRouter()


@app.post("/book/{book_id}")
def create(book: Book):
    return create_book(book)


@app.get("/get_all")
def read():
    return read_all()


@app.get("/books/{book_id}")
def read_book(_id: int):
    return read_book()


@app.put("/books/{book_id}")
def update(book_id: int, book: Book):
    return update_book(book_id, book)


@app.delete("/books/{book_id}")
def delete(book_id: int):
    return delete_book(book_id)


@app.post("/send_email")
def fun(email: Email):
    return send_email(email)


@app.get("/Total_price")
def pipe():
    return pipeline_agg()
