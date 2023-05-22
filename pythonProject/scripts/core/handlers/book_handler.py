from schemas.models import Book
from scripts.core.db.mongodb import book_1
from scripts.exceptions.exception_codes import Book_handling_exceptions
from scripts.logging.logger import logger


# creating new book mongodb collection
def create_book(book: Book):
    try:
        logger.info("handler: creating a book")
        book_1.insert_one(book.dict())
        return {"message": "Book created successfully"}
    except Exception as e:
        logger.error(Book_handling_exceptions.Ex01.format(error=str(e)))
        return {"Failed to create book"}


# getting books from the collection
def read_all():
    try:
        logger.info("Handler: Reading all books")
        books = book_1.find()
        all_books = []
        for new_book in books:
            del new_book["_id"]
            all_books.append(new_book)
        return all_books
    except Exception as e:
        logger.error(Book_handling_exceptions.Ex02.format(error=str(e)))
        return {"error: Failed to get book"}


def read_book(book_id: int):
    try:
        logger.info("Handler: Getting a specific book")
        book = book_1.find_one({"id": book_id})
        if book:
            del book["_id"]
            return book
        else:
            return {"message": "Book not found"}
    except Exception as e:
        logger.error(Book_handling_exceptions.Ex03.format(error=str(e)))
        return {"error": "Failed to get book"}


# updating the existing books in the collection
def update_book(book_id: int, book: Book):
    try:
        logger.info("Handler: Updating books")
        book_1.update_one({'book_id': book_id}, {'$set': book.dict()})
        return {"message": "Book updated successfully"}
    except Exception as e:
        logger.error(Book_handling_exceptions.Ex04.format(error=str(e)))
        return {"error: Failed to update the book"}


# deletes book from the collection
def delete_book(book_id: int):
    try:
        logger.info("Handler: Deleting books")
        book_1.delete_one({'book_id': book_id})
        return {"message": "Book deleted successfully"}
    except Exception as e:
        logger.error(Book_handling_exceptions.Ex05.format(error=str(e)))
        return {"error: Failed to delete the book"}


def pipeline_agg():
    logger.info("Handler: Creating pipeline")
    pipeline = [
        {
            '$addFields': {
                'Total_price': {
                    '$multiply': [
                        '$quantity', '$cost'
                    ]
                }
            }
        }, {
            '$group': {
                '_id': None,
                'Sum_of_all_price': {
                    '$sum': '$Total_price'
                }
            }
        }, {
            '$project': {
                '_id': 0
            }
        }
    ]
    data = book_1.aggregate(pipeline)
    data = list(data)
    print(data)
    return {"Total_price": data[0]['Sum_of_all_price']}
