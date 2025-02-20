from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Text, Column, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from flask_login import UserMixin


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class BlogPost(db.Model):  # child class
    __tablename__ = 'blogpost'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(
        String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    # relation with user
    parent_id = Column(Integer, ForeignKey('user.id'))
    author = relationship("User", back_populates="posts")
    # relation with comment
    comments = relationship("Comment", back_populates="parent_post")


class User(db.Model, UserMixin):  # parent class
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(250),  nullable=False)
    email: Mapped[str] = mapped_column(
        String(250), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship('Comment', back_populates='comment_author')

    def get_id(self):
        return str(self.id)


class Comment(db.Model):  # child class
    __tablename__ = 'comment'
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)

    author_id = Column(Integer, ForeignKey('user.id'))
    comment_author = relationship('User', back_populates='comments')
    post_id = mapped_column(Integer, db.ForeignKey("blogpost.id"))
    parent_post = relationship("BlogPost", back_populates="comments")
