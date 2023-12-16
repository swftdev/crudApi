from sqlalchemy import Column, String, Integer
from models.base import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

    def __repr__(self):
        return f"<Book id={self.id}, title={self.title}, author={self.author}>"
