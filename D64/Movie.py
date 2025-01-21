from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[int] = mapped_column(nullable=False)
    ranking: Mapped[float] = mapped_column(nullable=False)
    review: Mapped[str] = mapped_column(nullable=False)
    image_url: Mapped[str] = mapped_column(nullable=False)
