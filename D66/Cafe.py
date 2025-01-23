from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Cafe(Base):
    __tablename__ = 'cafe'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(nullable=False)
    has_wifi: Mapped[bool] = mapped_column(nullable=False)
    has_sockets: Mapped[bool] = mapped_column(nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(nullable=False)
    coffee_price: Mapped[str | None] = mapped_column(
        String(250), nullable=True)

    def to_dict(self):
        dict = {}
        for col in self.__table__.columns:
            dict[col.name] = getattr(self, col. name)
        return dict
