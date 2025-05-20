from fastapi import FastAPI,status
from pydantic import BaseModel
from typing import List
from fastapi.exceptions import HTTPException


books = [
  {
    "id": 1,
    "title": "Think Python",
    "author": "Allen B. Downey",
    "publisher": "O'Reilly Media",
    "published_date": "2021-01-01",
    "page_count": 1234,
    "language": "English"
  },
  {
    "id": 2,
    "title": "Django By Example",
    "author": "Antonio Mele",
    "publisher": "Packt Publishing Ltd",
    "published_date": "2022-01-19",
    "page_count": 1023,
    "language": "English"
  },
  {
    "id": 3,
    "title": "JavaScript: The Good Parts",
    "author": "Douglas Crockford",
    "publisher": "O'Reilly Media",
    "published_date": "2008-05-01",
    "page_count": 176,
    "language": "English"
  },
  {
    "id": 4,
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "publisher": "Prentice Hall",
    "published_date": "2008-08-01",
    "page_count": 464,
    "language": "English"
  },
  {
    "id": 5,
    "title": "Introduction to Algorithms",
    "author": "Thomas H. Cormen",
    "publisher": "MIT Press",
    "published_date": "2009-07-31",
    "page_count": 1312,
    "language": "English"
  },
  {
    "id": 6,
    "title": "You Don't Know JS",
    "author": "Kyle Simpson",
    "publisher": "O'Reilly Media",
    "published_date": "2015-12-27",
    "page_count": 278,
    "language": "English"
  },
  {
    "id": 7,
    "title": "Eloquent JavaScript",
    "author": "Marijn Haverbeke",
    "publisher": "No Starch Press",
    "published_date": "2018-12-04",
    "page_count": 472,
    "language": "English"
  },
  {
    "id": 8,
    "title": "Cracking the Coding Interview",
    "author": "Gayle Laakmann McDowell",
    "publisher": "CareerCup",
    "published_date": "2015-07-01",
    "page_count": 687,
    "language": "English"
  },
  {
    "id": 9,
    "title": "Python Crash Course",
    "author": "Eric Matthes",
    "publisher": "No Starch Press",
    "published_date": "2019-05-03",
    "page_count": 544,
    "language": "English"
  },
  {
    "id": 10,
    "title": "The Pragmatic Programmer",
    "author": "Andrew Hunt",
    "publisher": "Addison-Wesley",
    "published_date": "2019-09-13",
    "page_count": 352,
    "language": "English"
  }
  
]


app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

class BookUpdateModel(BaseModel):
    
    title: str
    author: str
    publisher: str
    page_count: int
    language: str


@app.get("/books", response_model=List[Book])
async def get_books():
    return books

@app.post("/create_book",status_code=status.HTTP_201_CREATED)
async def create_book(book_data:Book)->dict:
    new_book = book_data.model_dump()
    books.append(new_book)

    return new_book


@app.get("/book/{book_id}")
async def get_book(book_id: int)->dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.patch("/book/{book_id}")
async def update_book(book_id: int, book_update_data: BookUpdateModel) -> dict:
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_update_data.title
            book["author"] = book_update_data.author
            book["publisher"] = book_update_data.publisher
            book["page_count"] = book_update_data.page_count
            book["language"] = book_update_data.language
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete(".book/{book_id} , status_code = status.HTTP_204_NO_CONTENT")
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return
    raise HTTPException(status_code=404, detail="Book not found")