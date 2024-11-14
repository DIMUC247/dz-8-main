from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String

from app.db.base import Base


class Pizza(Base):
    __tablename__ = "pizzas"

    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[float] = mapped_column()
    name: Mapped[str] = mapped_column(String())







