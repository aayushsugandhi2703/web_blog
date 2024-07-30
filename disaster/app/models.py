from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

engine = create_engine("sqlite:///database.db")
Base = declarative_base()

class UserData(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(60), nullable=False)
    posts = relationship('PostData', back_populates='user')

class PostData(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(1000), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('UserData', back_populates='posts')

Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
