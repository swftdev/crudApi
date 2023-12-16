from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from flask import g
from models.book import Book
from models.base import Base

engine = create_engine("sqlite:///data/main.sqlite", echo=True)

def get_db():
    if 'db' not in g:
        g.db = Session(engine)

    return g.db

def close_db(_):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app):
    # TODO: we should only do this and migrations in certain cases
    Base.metadata.create_all(engine, checkfirst=True)
    # TODO: we should eventually "seed" the database somewhere

    app.teardown_appcontext(close_db)

