from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Session
from sqlalchemy import String
from sqlalchemy import create_engine
from app import db

class Products(db.Model):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    img: Mapped[str] = mapped_column(String(100))
    # brand: Mapped[str] = mapped_column(String(100))
    # type: Mapped[str] = mapped_column(String(100))
    # section: Mapped[str] = mapped_column(String(100))
    # collection: Mapped[str] = mapped_column(String(100))
    # scolor: Mapped[str] = mapped_column(String(100))

    def __repr__(self):
        return f"<Product {self.name}>"

# def create_database():
#     Base.metadata.create_all(engine)