from pydantic import BaseModel


class Book(BaseModel):
    # pydantic model
    id: int
    title: str
    category: str
    borrower_name: str
