from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine,table, Column, Integer, String, Text
from sqlalchemy.orm import declerative_base, sessionmaker

engine = create_engine('sqlite:///tasks_db.db', echo = True)

Base = declerative_base()

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key = True)
    Title = Column(String(20), nullable = False)
    Description = Column(String(100), nullable = False)

Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)